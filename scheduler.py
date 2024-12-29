import time

class Scheduler:
    def __init__(self):
        self.job_queue = []  # List to manage jobs
        self.completed_jobs = []  # List of completed jobs

    def add_job(self, job):
        self.job_queue.append(job)
        self.job_queue.sort(key=lambda x: x.priority)  # Sort by priority

    def schedule_jobs(self, resource_manager):
        for job in self.job_queue:
            if resource_manager.allocate_resources(job):
                job.state = 'running'
                job.start_time = time.time()
                print(f"Running Job: {job.job_id}")
                time.sleep(job.execution_time)  # Simulate job execution
                job.state = 'completed'
                job.end_time = time.time()
                print(f"Completed Job: {job.job_id}")
                resource_manager.release_resources(job)
                self.completed_jobs.append(job)
            else:
                job.state = 'failed'
                print(f"Failed to Run Job: {job.job_id} (Insufficient Resources)")
