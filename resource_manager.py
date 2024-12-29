class ResourceManager:
    def __init__(self, total_cpu, total_memory):
        self.total_cpu = total_cpu
        self.total_memory = total_memory
        self.available_cpu = total_cpu
        self.available_memory = total_memory

    def allocate_resources(self, job):
        if job.required_cpu <= self.available_cpu and job.required_memory <= self.available_memory:
            self.available_cpu -= job.required_cpu
            self.available_memory -= job.required_memory
            return True
        return False

    def release_resources(self, job):
        self.available_cpu += job.required_cpu
        self.available_memory += job.required_memory
