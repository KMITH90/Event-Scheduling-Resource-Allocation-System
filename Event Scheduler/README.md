## **Event Scheduling & Resource Allocation System<br><br>**

### **📌 Project Overview<br>**
This project is a Flask-based web application developed as part of a Flask Hiring Test assignment. The application allows organizations such as colleges, training centers, and offices to schedule events (seminars, workshops, classes, meetings) and allocate shared resources (rooms, instructors, equipment) while ensuring that no resource conflicts occur.
The system validates time overlaps and edge cases during event creation and resource allocation so that the same resource is never double-booked.<br><br>

### **🎯 Objectives<br>**
•	Create and manage events with start and end times<br>
•	Create and manage shared resources<br>
•	Allocate resources to events<br>
•	Detect and prevent scheduling conflicts<br>
•	Handle edge cases in time overlap logic<br>
•	Generate a resource utilization report for a selected date range<br><br>

### **🛠️ Technologies Used<br>**
•	Python<br>
•	Flask – Web framework<br>
•	SQLite – Database<br>
•	HTML & CSS – Frontend UI<br><br>

### **📂 Project Structure<br>**
EventSchedulingResourceAllocationSystem/<br>
│<br>
├── app.py<br>
├── requirements.txt<br>
│<br>
├── templates/<br>
│   ├── base.html<br>
│   ├── events.html<br>
│   ├── resources.html<br>
│   ├── allocate.html<br>
│   ├── conflicts.html<br>
│   └── report.html<br>
│<br>
├── static/<br>
│   └── style.css<br>
│<br>
├── screenshots/<br>
│   ├── events.png<br>
│   ├── resources.png<br>
│   ├── allocation.png<br>
│   ├── conflict.png<br>
│   └── report.png<br>
│<br>
└── README.md<br><br>

### **🗄️ Database Design<br>**
**1. Event Table<br>**
•	event_id (Primary Key)<br>
•	title<br>
•	start_time<br>
•	end_time<br>
•	description<br>
**2. Resource Table<br>**
•	resource_id (Primary Key)<br>
•	resource_name<br>
•	resource_type (Room / Instructor / Equipment)<br>
**3. EventResourceAllocation Table<br>**
•	allocation_id (Primary Key)<br>
•	event_id (Foreign Key → Event)<br>
•	resource_id (Foreign Key → Resource)<br><br>

### **🔑 Features Implemented<br>**
* Add / Edit / View Events<br>
* Add / Edit / View Resources<br>
* Allocate Resources to Events<br>
* Conflict Detection (No double booking)<br>
* Edge Case Handling (Exact match, partial overlap, nested events)<br>
* Resource Utilization Report (based on date range)<br><br>

### **⚙️ How to Run the Project<br>**
Step 1: Create a Virtual Environment (Optional but Recommended)<br>
python -m venv venv<br>
source venv/bin/activate   # On Windows: venv\Scripts\activate<br>
Step 2: Install Dependencies<br>
pip install -r requirements.txt<br>
Step 3: Run the Flask Application<br>
python app.py<br>
Step 4: Open in Browser<br>
http://127.0.0.1:5000/<br><br>

### **🔁 How to Re-run the Project After Closing<br>**
1.	Open the project folder<br>
2.	Activate the virtual environment (if used)<br>
3.	Run:<br>
python app.py<br>
4.	Open the browser and go to:<br>
http://127.0.0.1:5000/<br><br>

### **📊 Use Case Demonstration<br>**
•	Create 3–4 resources (rooms, instructors, equipment)<br>
•	Create 3–4 events with overlapping time slots<br>
•	Allocate resources to events<br>
•	Observe conflict error messages when overlaps occur<br>
•	Generate a resource utilization report for a chosen date range<br><br>

### **📸 Screenshots<br>**
Screenshots of the application are available in the screenshots/ folder:<br>
•	Event Management Page<br>
•	Resource Management Page<br>
•	Resource Allocation Page<br>
•	Dashboard Page<br>
•	Resource Utilization Report Page<br><br>

### **🎥 Demo Video<br>**
A screen-recorded demo video demonstrating all features of the application is included via an external link:<br>
**🔗 Demo Video Link:** https://drive.google.com/drive/folders/1vr5QdZ0SC3AZIsLG6SsWfThzFRVQCtXe<br><br>

### **🚀 Future Enhancements<br>**
•	User authentication and role-based access<br>
•	Calendar-based event view<br>
•	Email notifications for conflicts<br>
•	Export reports to PDF or Excel<br>
•	Improved UI styling and responsiveness<br><br>

### **👤 Author<br>**
**Name:** Mitra K<br>
**Project Type:** Flask Hiring Test Assignment<br>

