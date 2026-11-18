# Student Task Manager - User Guide

## Introduction

The Student Task Manager is a Python console application that helps students organize and manage their academic tasks.

## Starting the Application

Open the project folder in Terminal and run:

```bash
python3 main.py
```

The application displays a menu of available operations.

## Available Operations

### 1. Add Task
Select the add-task option and enter a task title. The application validates the title before adding it.

### 2. View Tasks
Select the view-tasks option to display all saved tasks with their IDs and completion status.

### 3. Complete Task
Select the complete-task option and enter the ID of the task you want to mark as completed.

### 4. Delete Task
Select the delete-task option and enter the ID of the task you want to remove.

### 5. Exit
Select the exit option to close the application.

## Input Validation

- Task titles cannot be empty.
- Task titles must contain at least three characters.
- Task IDs must be valid positive numbers.
- Invalid task IDs are handled by the application.

## Running Unit Tests

To execute the automated tests, run:

```bash
python3 -m unittest discover -s tests -v
```

The tests cover adding, completing, and deleting tasks.