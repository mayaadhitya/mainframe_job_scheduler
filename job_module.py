__all__ = ["Job"]
class Job:
    def __init__(self, job_id, priority, required_cpu, required_memory, execution_time):
        self.job_id = job_id
        self.priority = priority
        self.required_cpu = required_cpu
        self.required_memory = required_memory
        self.execution_time = execution_time
        self.state = 'waiting'  # States: waiting, running, completed, failed
        self.start_time = None
        self.end_time = None

