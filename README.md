# Task Manager Application  

## Overview  
The Task Manager Application is a Python-based command-line tool designed to help small businesses manage tasks assigned to their team members. This project leverages file handling, string manipulation, and user authentication to track tasks, assign them to users, and monitor completion status.  

## Features  
- **User Management**  
  - Admin can register new users.  
  - User login with validation against stored credentials.  

- **Task Management**  
  - Add tasks with details like title, description, due date, and assigned user.  
  - View all tasks or tasks specific to the logged-in user.  

- **Task Tracking**  
  - Tracks task completion status.  
  - Displays task statistics (for admin).  

- **File Management**  
  - User credentials and tasks are stored in `user.txt` and `tasks.txt` respectively.  
  - Task data is formatted for easy readability and manipulation.  

## Project Structure  
```
├── task_manager.py                   # Main application file
├── task_template.py                  # Starter template for development
├── tasks.txt                         # Stores all task information
└── user.txt                          # Stores user credentials
```

## Installation and Setup  

1. **Clone the Repository**  
```
git clone https://github.com/negin-mgdm/task-manager-app.git
cd task-manager-app
```
2. **Run the Application**
```
python task_manager.py
```
3. **Login Information**
   
  Default Admin Credentials:
```
Username: admin  
Password: adm1n  
```
The admin user can register additional users through the application.

## Usage

1. **Login**

- Upon running the program, users are prompted to log in using their credentials from `user.txt`.

2. **Menu Options (Post Login)**

```
r  - Register a user (Admin only)  
a  - Add a task  
va - View all tasks  
vm - View my tasks  
s  - Show statistics (Admin only)  
e  - Exit  
```
- Users can add tasks or view their own tasks.
- Admin users have access to register new users and view task/user statistics.

