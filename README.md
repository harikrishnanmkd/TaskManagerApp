# Task Manager App

A full-stack Task Manager web application built using **Python Django** and **Bootstrap 5**. The application allows users to register, log in, and manage their personal tasks securely.

---

## Features

* User Registration
* User Login & Logout
* Create Tasks
* Edit Tasks
* Delete Tasks
* Mark Tasks as Completed
* Filter Tasks (All, Completed, Pending)
* User-specific task management
* Responsive Bootstrap 5 UI

---

## Technologies Used

### Backend

* Python 3.x
* Django

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Database

* SQLite

---

## Project Structure

```
TaskManager/
│
├── taskmanager/
├── users/
├── tasks/
├── templates/
├── static/
├── db.sqlite3
├── manage.py
└── README.md
```

---

## Installation & Setup

### Step 1: Clone the Repository

```bash
git clone <repository-url>
```

Or download and extract the ZIP file.

---

### Step 2: Open the Project Folder

```bash
cd TaskManager
```

---

### Step 3: Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Linux / macOS

```bash
python3 -m venv venv
```

---

### Step 4: Activate the Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### Step 5: Install Dependencies

```bash
pip install django pillow
```

If you are using Django REST Framework, install it as well:

```bash
pip install djangorestframework
```

---

### Step 6: Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 7: Create an Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to enter:

* Username
* Email
* Password

---

### Step 8: Run the Development Server

```bash
python manage.py runserver
```

---

### Step 9: Open the Application

Application

```
http://127.0.0.1:8000/
```

Register

```
http://127.0.0.1:8000/register/
```

Login

```
http://127.0.0.1:8000/login/
```

Admin Panel

```
http://127.0.0.1:8000/admin/
```

---

## Usage

1. Register a new account.
2. Log in using your credentials.
3. Add a new task.
4. Edit or delete tasks.
5. Mark tasks as completed.
6. Filter tasks using **All**, **Completed**, and **Pending**.

---

## Default Admin

Create your own administrator account using:

```bash
python manage.py createsuperuser
```

---


## Author

Harikrishnan K
