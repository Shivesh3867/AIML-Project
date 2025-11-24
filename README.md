Project Information
Name: Shivesh Pratap Singh

Registration Number: 25BSA10131

Course: Bachelor of Technology (B.Tech)

Faculty: Dr. Santosh Kumar Sahoo

Institution: VIT Bhopal University

Introduction
This project is a console-based Hospital Patient Queue System implemented in Python. It prioritizes patient management by severity using a priority queue built with the heapq module. The system allows you to add patients with severity levels, serve the most critical patient first, and view the current patient queue ranked by severity.

Designed as part of academic submission for B.Tech coursework at VIT Bhopal University under the guidance of Dr. Santosh Kumar Sahoo, this system demonstrates practical use of heap data structures for priority management in healthcare.

Features
Add patients with a name and severity score (1 to 10, where 10 indicates highest severity).

Automatically manage queue priority to serve the most critical patient first.

Serve patients one by one in order of severity.

Display the current queue with patients sorted by severity.

Input validation for severity to ensure proper numeric data entry.

Intuitive menu-driven console interface.

Robust against invalid user inputs and maintains consistent queue state.

Technologies Used
Python 3.x

Built-in heapq module for priority queue management

Console input/output for user interaction

Installation
Ensure Python 3.x is installed on your system.

Save the script file as hospital_queue.py.

No external libraries are required beyond Python standard libraries.

How to Run
Open a terminal or command prompt.

Navigate to the directory containing hospital_queue.py.

Run the program using the command:

text
python hospital_queue.py
Follow on-screen menu options to add patients, serve patients, view queue, or exit.

User Guide and Menu
After starting the program, you'll be presented with the following menu:

text
1. Add patient
2. Serve next patient
3. Show patient queue
4. Exit
Option 1: Input patient's name and severity to add to the queue.

Option 2: Serve the patient with the highest severity currently in the queue.

Option 3: View all patients in the queue sorted by severity.

Option 4: Exit the program gracefully.

Detailed Workflow and Flowchart
Workflow
Launch program.

Show menu.

User chooses option.

Based on selection:

Add Patient:

Prompt for name and severity.

Validate severity input.

Add patient to priority queue (max-heap simulation using negative severity).

Confirm addition.

Serve Next Patient:

Pop patient with highest severity.

Display served patient details.

Handle empty queue case.

Show Patient Queue:

Display all patients in descending order of severity.

Handle empty queue case.

Exit Program:

Thank user and terminate.

Invalid Input:

Notify user and re-display menu.

Flowchart
text
flowchart TD
    Start[Start Program]
    Start --> Menu[Display Menu Options]
    Menu --> Choice{User Choice}
    
    Choice -->|1| AddPatient[Add Patient]
    AddPatient --> InputName[Input Patient Name]
    InputName --> InputSeverity[Input Patient Severity]
    InputSeverity --> ValidateSeverity{Is severity number?}
    ValidateSeverity -->|No| ErrorInvalid[Show invalid input message]
    ValidateSeverity -->|No| Menu
    ValidateSeverity -->|Yes| AddToQueue[Add patient to priority queue]
    AddToQueue --> ConfirmAdd[Print confirmation message]
    ConfirmAdd --> Menu
    
    Choice -->|2| ServePatient[Serve Next Patient]
    ServePatient --> CheckEmpty{Is queue empty?}
    CheckEmpty -->|Yes| ShowEmpty[Show 'Queue empty' message]
    ShowEmpty --> Menu
    CheckEmpty -->|No| PopPatient[Pop highest severity patient]
    PopPatient --> ShowPatient[Display patient served]
    ShowPatient --> Menu
    
    Choice -->|3| ShowQueue[Show entire patient queue]
    ShowQueue --> CheckEmpty2{Is queue empty?}
    CheckEmpty2 -->|Yes| ShowEmpty2[Show 'Queue empty' message]
    ShowEmpty2 --> Menu
    CheckEmpty2 -->|No| DisplayAll[Display patients with severity]
    DisplayAll --> Menu
    
    Choice -->|4| Exit[Exit Program]
    Exit --> End[End]
    
    Choice -->|Invalid| InvalidChoice[Show invalid choice message]
    InvalidChoice --> Menu
Error Handling
Severity input is validated to accept only integer values.

Invalid menu choices prompt an error message without program crash.

Empty queue conditions are handled gracefully showing appropriate messages when serving or displaying patients.

Possible Enhancements
Persist patient data to persistent storage (file or database) to maintain state between runs.

Allow updating patient severity or removing specific patients manually.

Provide GUI interface for easier interaction.

Add timestamps for arrival time and waiting time statistics.

Improve input system by adding validations (e.g., severity range check).

Acknowledgements
Thanks to Dr. Santosh Kumar Sahoo for guidance and support throughout this project.

Python documentation and community resources for data structures and heap operations.

Conclusion
This Hospital Patient Queue System project effectively demonstrates how priority queues can be applied in real-world scenarios. The use of Python's heapq implements a max-priority queue by pushing negative severity values to always serve the most critical patient first. Its intuitive interface and handling of edge cases make it a practical tool for understanding priority-based scheduling.
