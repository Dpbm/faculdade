from abc import ABC, abstractmethod

class Job:
    def __init__(self, id, data, status):
        self.id = id
        self.data = data
        self.status = status

    def show(self):
        print(f"id={self.id}, data={self.data}, status={self.status}")

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass


class AddJob(Command):
    def __init__(self, queue, job):
        self.job = job
        self.queue = queue
    
    def execute(self):
        self.queue.add_job(self.job)

    def undo(self):
        self.queue.remove_job(self.job)

class RemoveJob(Command):
    def __init__(self, queue, job):
        self.job = job
        self.queue = queue
    
    def execute(self):
        self.queue.remove_job(self.job)

    def undo(self):
        self.queue.add_job(self.job)

class CancelAll(Command):
    def __init__(self,queue):
        self.status = [ job.status for job in queue._jobs ]
    
    def execute(self):
        for job in queue._jobs:
            job.


class Queue:
    def __init__(self):
        self._jobs = []

    def add_job(self, job):
        self._jobs.append(job)

    def remove_job(self, job):
        self._jobs.remove(job)

    def cancel_job(self):
        

    def show(self):
        print("---jobs in queue---")
        for job in self._jobs:
            job.show()


class History:
    def __init__(self):
        self._redo = []
        self._undo = []

    def execute(self, command):
        self._undo.append(command)
        command.execute()

    def undo(self):
        if self._undo:
            command = self._undo.pop()
            self._redo.append(command)
            command.undo()

    def redo(self):
        if self._redo:
            command = self._redo.pop()
            self._undo.append(command)
            command.execute()
            


if __name__ == "__main__":
    queue = Queue()
    history = History()
    
    common_job = Job(3, "3", "running")
    history.execute(AddJob(queue, Job(1, "test", "running")))
    history.execute(AddJob(queue, Job(2, "18", "waiting")))
    history.execute(AddJob(queue, common_job))
    history.execute(RemoveJob(queue, common_job))
    queue.show()

    history.undo()
    queue.show()
    
    history.undo()
    queue.show()
    
    history.redo()
    queue.show()