Mainframe Job Scheduler
A Python-based job scheduling system that efficiently manages resources for mainframe tasks by prioritizing and executing jobs based on defined constraints such as CPU, memory requirements, and priority levels.

Features
Job Modeling: Define jobs with attributes like priority, state, required CPU, required memory, and execution time.
Resource Management: Handle resource allocation to avoid conflicts and optimize utilization.
Scheduling: Execute jobs based on their priority and available resources.
PrettyTable Integration: Display job details in a structured table format.
Prerequisites
Before running the project, ensure you have the following installed:

Python 3.8 or later
PrettyTable library for tabular data visualization
Install required packages using:

bash
Copy code
pip install PrettyTable
File Structure
bash
Copy code
mainframe_job_scheduler/
├── job_module.py          # Defines the Job class and job attributes
├── resource_manager.py    # Handles resource allocation and deallocation
├── scheduler.py           # Implements the scheduling algorithm
├── main.py                # Main entry point of the application
└── README.md              # Project documentation
How to Run
1.Clone the repository:

git clone <repository_url>
cd mainframe_job_scheduler
Run the main.py file:

2.Run the main.py file:
python main.py

3.The job details and their scheduling statuses will be displayed in a formatted table.

Example Output

+---------+----------+----------+--------------+------------------+----------------+
| Job ID  | Priority |  State   | Required CPU | Required Memory  | Execution Time |
+---------+----------+----------+--------------+------------------+----------------+
|   101   |   High   | Running  |      4       |       512MB      |       5s       |
|   102   |  Medium  | Waiting  |      2       |       256MB      |       3s       |
+---------+----------+----------+--------------+------------------+----------------+

Troubleshooting
ImportError: If you face an import error, ensure the file names and imports are consistent.
ModuleNotFoundError: Run the script from the root directory of the project.

Contributing
Contributions are welcome! Feel free to fork the repository and create pull requests for improvements or bug fixes.
