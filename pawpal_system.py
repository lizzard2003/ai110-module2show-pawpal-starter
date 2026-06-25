class Owner:
    name: str
    pets: list  # List of PetInformation objects

    def __init__(self, name: str):
        """Initialize owner with a name and empty pet list."""
        self.name = name
        self.pets = []

    def getOwnerName(self) -> str:
        """Return the owner's name."""
        return self.name

    def addPet(self, pet: 'PetInformation') -> None:
        """Add a pet to the owner's collection."""
        self.pets.append(pet)

    def removePet(self, pet: 'PetInformation') -> None:
        """Remove a pet from the owner's collection."""
        self.pets.remove(pet)

    def getPets(self) -> list:
        """Return the list of pets owned by this owner."""
        return self.pets

    def getPetCount(self) -> int:
        """Return the number of pets the owner has."""
        return len(self.pets)

    def getAllTasks(self) -> list:
        """Collect and return all tasks from every pet."""
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.getTasks())
        return tasks

    def getTotalTaskCount(self) -> int:
        """Return the total number of tasks across all pets."""
        return len(self.getAllTasks())


class Scheduler:
    owner: 'Owner'

    def __init__(self, owner: 'Owner'):
        """Initialize the scheduler with an owner."""
        self.owner = owner

    def getAllTasks(self) -> list:
        """Return all tasks belonging to the owner."""
        return self.owner.getAllTasks()

    def getTasksByFrequency(self, frequency: str) -> list:
        """Return tasks matching a specific frequency."""
        return [task for task in self.getAllTasks() if task.frequency == frequency]

    def getTasksByTime(self, time: str) -> list:
        """Return tasks scheduled at a given time."""
        return [task for task in self.getAllTasks() if task.time == time]

    def getTasksByPet(self, pet: 'PetInformation') -> list:
        """Return all tasks for a single pet."""
        return pet.getTasks()

    def getCompletedTasks(self) -> list:
        """Return tasks that have been completed."""
        return [task for task in self.getAllTasks() if task.completion_status]

    def getIncompleteTasks(self) -> list:
        """Return tasks that are not yet complete."""
        return [task for task in self.getAllTasks() if not task.completion_status]

    def sortTasksByTime(self) -> list:
        """Return tasks sorted by time."""
        return sorted(self.getAllTasks(), key=lambda task: task.time)

    def sortTasksByFrequency(self) -> list:
        """Return tasks sorted by frequency."""
        return sorted(self.getAllTasks(), key=lambda task: task.frequency)

    def markTaskComplete(self, task: 'Task') -> None:
        """Mark a task as complete."""
        task.markComplete()

    def resetAllTasks(self) -> None:
        """Reset completion status for all tasks."""
        for task in self.getAllTasks():
            task.resetTask()

    def getScheduleForDay(self, day: str) -> list:
        """Return the schedule for a given day or daily tasks."""
        if day.lower() in ("today", "daily"):
            return [task for task in self.getAllTasks() if task.frequency == "daily"]
        return [task for task in self.getAllTasks() if task.frequency.lower() == day.lower()]


class Task:
    description: str
    time: str
    frequency: str
    completion_status: bool

    def __init__(self, description: str, time: str, frequency: str):
        """Initialize task details and set completion status false."""
        self.description = description
        self.time = time
        self.frequency = frequency
        self.completion_status = False

    def getDescription(self) -> str:
        """Return the task description."""
        return self.description

    def getTime(self) -> str:
        """Return the task time."""
        return self.time

    def getFrequency(self) -> str:
        """Return the task frequency."""
        return self.frequency

    def getCompletionStatus(self) -> bool:
        """Return whether the task is completed."""
        return self.completion_status

    def markComplete(self) -> None:
        """Mark the task as completed."""
        self.completion_status = True

    def mark_complete(self) -> None:
        """Alias to mark the task as complete."""
        self.markComplete()

    def resetTask(self) -> None:
        """Reset the task to incomplete."""
        self.completion_status = False


class PetInformation:
    name: str
    age: int
    breed: str
    color: str
    tasks: list  # List of Task objects

    def __init__(self, name: str, age: int, breed: str, color: str):
        """Initialize pet details and empty task list."""
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.tasks = []

    def getPetName(self) -> str:
        """Return the pet's name."""
        return self.name

    def getAge(self) -> int:
        """Return the pet's age."""
        return self.age

    def getBreed(self) -> str:
        """Return the pet's breed."""
        return self.breed

    def getColor(self) -> str:
        """Return the pet's color."""
        return self.color

    def addTask(self, task: 'Task') -> None:
        """Add a task to the pet."""
        self.tasks.append(task)

    def removeTask(self, task: 'Task') -> None:
        """Remove a task from the pet."""
        self.tasks.remove(task)

    def getTasks(self) -> list:
        """Return the pet's task list."""
        return self.tasks

    def getTaskCount(self) -> int:
        """Return how many tasks the pet has."""
        return len(self.tasks)


class PetTasks:
    timeConstraint: 'TimeConstraint'

    def __init__(self, timeConstraint: 'TimeConstraint'):
        ...

    def feedPet(self) -> str:
        ...

    def walkPet(self) -> str:
        ...

    def petSit(self) -> str:
        ...


class TimeConstraint:
    taskDuration: int
    availability: int
    repetition: str

    def __init__(self, taskDuration: int, availability: int, repetition: str):
        ...

    def getTaskDuration(self) -> int:
        ...

    def getAvailability(self) -> int:
        ...

    def getRepetition(self) -> str:
        ...
