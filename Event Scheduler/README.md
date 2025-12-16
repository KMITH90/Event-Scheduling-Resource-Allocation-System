Event Scheduling & Resource Allocation System

📌 Project Overview
This project is a Flask-based web application developed as part of a Flask Hiring Test assignment. The application allows organizations such as colleges, training centers, and offices to schedule events (seminars, workshops, classes, meetings) and allocate shared resources (rooms, instructors, equipment) while ensuring that no resource conflicts occur.
The system validates time overlaps and edge cases during event creation and resource allocation so that the same resource is never double-booked.

🎯 Objectives
•	Create and manage events with start and end times
•	Create and manage shared resources
•	Allocate resources to events
•	Detect and prevent scheduling conflicts
•	Handle edge cases in time overlap logic
•	Generate a resource utilization report for a selected date range

🛠️ Technologies Used
•	Python
•	Flask – Web framework
•	SQLite – Database
•	HTML & CSS – Frontend UI

📂 Project Structure
EventSchedulingResourceAllocationSystem/
│
├── app.py
├── requirements.txt
├── database.db
│
├── templates/
│   ├── base.html
│   ├── events.html
│   ├── resources.html
│   ├── allocate.html
│   ├── conflicts.html
│   └── report.html
│
├── static/
│   └── style.css
│
├── screenshots/
│   ├── events.png
│   ├── resources.png
│   ├── allocation.png
│   ├── conflict.png
│   └── report.png
│
└── README.md

🗄️ Database Design
1. Event Table
•	event_id (Primary Key)
•	title
•	start_time
•	end_time
•	description
2. Resource Table
•	resource_id (Primary Key)
•	resource_name
•	resource_type (Room / Instructor / Equipment)
3. EventResourceAllocation Table
•	allocation_id (Primary Key)
•	event_id (Foreign Key → Event)
•	resource_id (Foreign Key → Resource)

🔑 Features Implemented
* Add / Edit / View Events
* Add / Edit / View Resources
* Allocate Resources to Events
* Conflict Detection (No double booking)
* Edge Case Handling (Exact match, partial overlap, nested events)
* Resource Utilization Report (based on date range)

⚙️ How to Run the Project
Step 1: Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Step 2: Install Dependencies
pip install -r requirements.txt
Step 3: Run the Flask Application
python app.py
Step 4: Open in Browser
http://127.0.0.1:5000/

🔁 How to Re-run the Project After Closing
1.	Open the project folder
2.	Activate the virtual environment (if used)
3.	Run:
python app.py
4.	Open the browser and go to:
http://127.0.0.1:5000/

📊 Use Case Demonstration
•	Create 3–4 resources (rooms, instructors, equipment)
•	Create 3–4 events with overlapping time slots
•	Allocate resources to events
•	Observe conflict error messages when overlaps occur
•	Generate a resource utilization report for a chosen date range

📸 Screenshots
Screenshots of the application are available in the screenshots/ folder:
•	Event Management Page
•	Resource Management Page
•	Resource Allocation Page
•	Dashboard Page
•	Resource Utilization Report Page

🎥 Demo Video
A screen-recorded demo video demonstrating all features of the application is included via an external link:
🔗 Demo Video Link: https://drive.google.com/drive/folders/1vr5QdZ0SC3AZIsLG6SsWfThzFRVQCtXe

🚀 Future Enhancements
•	User authentication and role-based access
•	Calendar-based event view
•	Email notifications for conflicts
•	Export reports to PDF or Excel
•	Improved UI styling and responsiveness

👤 Author
Name: Mitra K
Project Type: Flask Hiring Test Assignment
