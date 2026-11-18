# Student Task Manager

A Python-based Student Task Manager developed using Git and GitHub for version control.

**Project Status:** Completed

## Features

- Add new tasks with title validation.
- View all tasks.
- Mark tasks as completed using their task ID.
- Delete tasks using their task ID.
- Validate user input and task IDs.
- Automated unit testing using Python unittest.
- GitHub Actions workflow for continuous integration.

## Technologies Used

- Python
- Git
- GitHub
- Python unittest
- GitHub Actions

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ManalRehman/studenttaskmanager.git
```

### 2. Open the Project Folder

```bash
cd studenttaskmanager
```

### 3. Run the Application

```bash
python3 main.py
```

## Running Tests

Run the following command from the project directory:

```bash
python3 -m unittest discover -s tests -v
```

The test suite checks task creation, task completion, and task deletion.

## GitHub Actions

This project uses GitHub Actions to automatically run unit tests whenever code is pushed to the `main` branch or a pull request is created for `main`.

## Repository

[Student Task Manager on GitHub](https://github.com/ManalRehman/studenttaskmanager)