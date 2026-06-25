class Owner:
    name: str
    pets: list  # List of PetInformation objects

    def __init__(self, name: str):
        self.name = name
        self.pets = []

    def getOwnerName(self) -> str:
        return self.name

    def addPet(self, pet: 'PetInformation') -> None:
        self.pets.append(pet)

    def removePet(self, pet: 'PetInformation') -> None:
        self.pets.remove(pet)

    def getPets(self) -> list:
        return self.pets

    def getPetCount(self) -> int:
        return len(self.pets)

    def getAllTasks(self) -> list:
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.getTasks())
        return tasks

    def getTotalTaskCount(self) -> int:
        return len(self.getAllTasks())


class Scheduler:
    owner: 'Owner'

    def __init__(self, owner: 'Owner'):
        self.owner = owner

    def getAllTasks(self) -> list:
        return self.owner.getAllTasks()

    def getTasksByFrequency(self, frequency: str) -> list:
        return [task for task in self.getAllTasks() if task.frequency == frequency]

    def getTasksByTime(self, time: str) -> list:
        return [task for task in self.getAllTasks() if task.time == time]

    def getTasksByPet(self, pet: 'PetInformation') -> list:
        return pet.getTasks()

    def getCompletedTasks(self) -> list:
        return [task for task in self.getAllTasks() if task.completion_status]

    def getIncompleteTasks(self) -> list:
        return [task for task in self.getAllTasks() if not task.completion_status]

    def sortTasksByTime(self) -> list:
        return sorted(self.getAllTasks(), key=lambda task: task.time)

    def sortTasksByFrequency(self) -> list:
        return sorted(self.getAllTasks(), key=lambda task: task.frequency)

    def markTaskComplete(self, task: 'Task') -> None:
        task.markComplete()

    def resetAllTasks(self) -> None:
        for task in self.getAllTasks():
            task.resetTask()

    def getScheduleForDay(self, day: str) -> list:
        if day.lower() in ("today", "daily"):
            return [task for task in self.getAllTasks() if task.frequency == "daily"]
        return [task for task in self.getAllTasks() if task.frequency.lower() == day.lower()]


class Task:
    description: str
    time: str
    frequency: str
    completion_status: bool

    def __init__(self, description: str, time: str, frequency: str):
        self.description = description
        self.time = time
        self.frequency = frequency
        self.completion_status = False

    def getDescription(self) -> str:
        return self.description

    def getTime(self) -> str:
        return self.time

    def getFrequency(self) -> str:
        return self.frequency

    def getCompletionStatus(self) -> bool:
        return self.completion_status

    def markComplete(self) -> None:
        self.completion_status = True

    def resetTask(self) -> None:
        self.completion_status = False


class PetInformation:
    name: str
    age: int
    breed: str
    color: str
    tasks: list  # List of Task objects

    def __init__(self, name: str, age: int, breed: str, color: str):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.tasks = []

    def getPetName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return self.age

    def getBreed(self) -> str:
        return self.breed

    def getColor(self) -> str:
        return self.color

    def addTask(self, task: 'Task') -> None:
        self.tasks.append(task)

    def removeTask(self, task: 'Task') -> None:
        self.tasks.remove(task)

    def getTasks(self) -> list:
        return self.tasks

    def getTaskCount(self) -> int:
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
