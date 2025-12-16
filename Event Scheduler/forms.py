from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeLocalField, SubmitField, SelectField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    title = StringField('Event Title', validators=[DataRequired()])
    start_time = DateTimeLocalField('Start Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    end_time = DateTimeLocalField('End Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Save Event')


class ResourceForm(FlaskForm):
    name = StringField('Resource Name', validators=[DataRequired()])
    type = SelectField(
        'Resource Type',
        choices=[
            ('Room', 'Room'),
            ('Instructor', 'Instructor'),
            ('Equipment', 'Equipment')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Save Resource')

class AllocationForm(FlaskForm):
    event_id = SelectField('Event', coerce=int, validators=[DataRequired()])
    resource_id = SelectField('Resource', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Allocate Resource')
