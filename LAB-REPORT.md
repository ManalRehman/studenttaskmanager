# LAB REPORT
## Student Task Manager Development and Version Control Using Git and GitHub

**Course:** DevOps for Cloud Computing  
**Course Code:** CSC418  
**Student:** Manal Rehman  
**Program:** BS Software Engineering  
**Semester:** 7th  
**Batch:** FA23

---

### 1. Difference Between Git and GitHub; Purpose of Add, Commit and Push

Git is a version control system used to track changes in source code. GitHub is an online platform used to host Git repositories and collaborate with other developers.

- **git add:** Adds changed files to the staging area.
- **git commit:** Saves changes in the local repository.
- **git push:** Uploads local commits to GitHub.

### 2. Why Branches and Pull Requests Are Used; What Causes Merge Conflicts

Branches allow developers to work on different features separately without directly affecting the main branch.

Pull Requests allow developers to review changes before merging them into the main branch.

Merge conflicts occur when two branches contain different changes to the same part of a file, and Git cannot automatically combine them.

In this project, I deliberately changed the same project status line in two branches and resolved the resulting conflict manually.

### 3. Difference Between Fetch and Pull, and Between Merge and Rebase

- **Fetch:** Downloads changes from the remote repository without applying them to the current branch.
- **Pull:** Downloads and integrates remote changes into the current branch.
- **Merge:** Combines changes from two branches while preserving their commit history.
- **Rebase:** Reapplies commits on top of another branch to create a more linear history.

### 4. How GitHub Issues and Actions Help a Development Team

GitHub Issues help developers organize tasks, report problems, and track project progress.

GitHub Actions automates tasks such as running tests whenever code is pushed or a Pull Request is created.

In this project, four Issues were created and GitHub Actions was configured to automatically run Python unit tests.

### 5. One Difficulty Faced and How It Was Solved

One difficulty was a failed GitHub Actions test run. The error occurred because Matplotlib was imported in the main application but was not required by the project and was not installed in the testing environment.

I removed the unnecessary import, committed the correction, and pushed it to GitHub. The next automated test run completed successfully.

---

### Conclusion

This assignment helped me understand practical Git and GitHub workflows, including version control, branching, Pull Requests, merge conflict resolution, automated testing, GitHub Actions, and software documentation.