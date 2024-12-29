import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from job_module import Job
print("Job class imported successfully!")
from resource_manager import ResourceManager
from scheduler import Scheduler
from prettytable import PrettyTable

def display_jobs(jobs):
    table = PrettyTable()
    table.field_names = ["Job ID", "Priority", "State", "Required CPU", "Required Memory", "Execution Time"]
    for job in jobs:
        table.add_row([job.job_id, job.priority, job.state, job.required_cpu, job.required_memory, job.execution_time])
    print(table)

if __name__ == "__main__":
    # Initialize resources
    total_cpu = 8
    total_memory = 16
    resource_manager = ResourceManager(total_cpu, total_memory)

    # Initialize scheduler
    scheduler = Scheduler()

    # Create jobs
    job1 = Job(job_id="Job1", priority=1, required_cpu=2, required_memory=4, execution_time=2)
    job2 = Job(job_id="Job2", priority=2, required_cpu=3, required_memory=5, execution_time=3)
    job3 = Job(job_id="Job3", priority=1, required_cpu=4, required_memory=3, execution_time=1)
    job4 = Job(job_id="Job4", priority=3, required_cpu=5, required_memory=6, execution_time=4)

    # Submit jobs to scheduler
    scheduler.add_job(job1)
    scheduler.add_job(job2)
    scheduler.add_job(job3)
    scheduler.add_job(job4)

    # Display initial job states
    print("Initial Job States:")
    display_jobs([job1, job2, job3, job4])

    # Run scheduler
    print("\nRunning Scheduler...")
    scheduler.schedule_jobs(resource_manager)

    # Display final job states
    print("\nFinal Job States:")
    display_jobs(scheduler.completed_jobs)
