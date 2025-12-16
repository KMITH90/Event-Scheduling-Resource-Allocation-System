from flask import Flask, render_template, redirect, url_for, request
from config import Config
from models import db, Event, Resource, Allocation
from forms import EventForm, ResourceForm, AllocationForm
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# ---------------- HELPER FUNCTION ---------------- #

def has_conflict(resource_id, start_time, end_time):
    allocations = Allocation.query.filter_by(resource_id=resource_id).all()

    for alloc in allocations:
        event = Event.query.get(alloc.event_id)
        if start_time < event.end_time and end_time > event.start_time:
            return True
    return False


# ---------------- HOME / DASHBOARD ---------------- #

@app.route('/')
def home_page():
    stats = {
        'events': Event.query.count(),
        'resources': Resource.query.count(),
        'allocations': Allocation.query.count()
    }
    return render_template('home.html', stats=stats)


# ---------------- EVENTS ---------------- #

@app.route('/events')
def list_events():
    events = Event.query.all()
    return render_template('events.html', events=events)

@app.route('/events/add', methods=['GET', 'POST'])
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            description=form.description.data
        )
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('list_events'))
    return render_template('add_event.html', form=form)


# ---------------- RESOURCES ---------------- #

@app.route('/resources')
def list_resources():
    resources = Resource.query.all()
    return render_template('resources.html', resources=resources)

@app.route('/resources/add', methods=['GET', 'POST'])
def add_resource():
    form = ResourceForm()
    if form.validate_on_submit():
        resource = Resource(
            name=form.name.data,
            type=form.type.data
        )
        db.session.add(resource)
        db.session.commit()
        return redirect(url_for('list_resources'))
    return render_template('add_resource.html', form=form)


# ---------------- ALLOCATION ---------------- #

@app.route('/allocate', methods=['GET', 'POST'])
def allocate_resource():
    form = AllocationForm()

    form.event_id.choices = [(e.id, e.title) for e in Event.query.all()]
    form.resource_id.choices = [(r.id, f"{r.name} ({r.type})") for r in Resource.query.all()]

    if form.validate_on_submit():
        event = Event.query.get(form.event_id.data)

        if has_conflict(form.resource_id.data, event.start_time, event.end_time):
            return render_template(
                'conflicts.html',
                message="Resource already booked for this time slot."
            )

        allocation = Allocation(
            event_id=event.id,
            resource_id=form.resource_id.data
        )
        db.session.add(allocation)
        db.session.commit()
        return redirect(url_for('list_events'))

    return render_template('allocate.html', form=form)


# ---------------- REPORT ---------------- #

@app.route('/report', methods=['GET', 'POST'])
def resource_report():
    report_data = []

    if request.method == 'POST':
        start = datetime.strptime(request.form['start'], '%Y-%m-%d')
        end = datetime.strptime(request.form['end'], '%Y-%m-%d')

        for resource in Resource.query.all():
            total_hours = 0
            upcoming = []

            allocations = Allocation.query.filter_by(resource_id=resource.id).all()

            for alloc in allocations:
                event = Event.query.get(alloc.event_id)

                overlap_start = max(event.start_time, start)
                overlap_end = min(event.end_time, end)

                if overlap_start < overlap_end:
                    total_hours += (overlap_end - overlap_start).seconds / 3600

                if event.start_time > datetime.now():
                    upcoming.append(event.title)

            report_data.append({
                'resource': f"{resource.name} ({resource.type})",
                'hours': round(total_hours, 2),
                'upcoming': upcoming
            })

    return render_template('report.html', report_data=report_data)

@app.route('/events/edit/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    form = EventForm(obj=event)

    if form.validate_on_submit():
        event.title = form.title.data
        event.start_time = form.start_time.data
        event.end_time = form.end_time.data
        event.description = form.description.data
        db.session.commit()
        return redirect(url_for('list_events'))

    return render_template('add_event.html', form=form)

@app.route('/events/delete/<int:event_id>')
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)

    # Remove related allocations first
    Allocation.query.filter_by(event_id=event.id).delete()

    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('list_events'))

@app.route('/resources/edit/<int:resource_id>', methods=['GET', 'POST'])
def edit_resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    form = ResourceForm(obj=resource)

    if form.validate_on_submit():
        resource.name = form.name.data
        resource.type = form.type.data
        db.session.commit()
        return redirect(url_for('list_resources'))

    return render_template('add_resource.html', form=form)

@app.route('/resources/delete/<int:resource_id>')
def delete_resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)

    Allocation.query.filter_by(resource_id=resource.id).delete()

    db.session.delete(resource)
    db.session.commit()
    return redirect(url_for('list_resources'))

# ---------------- RUN APP ---------------- #

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
