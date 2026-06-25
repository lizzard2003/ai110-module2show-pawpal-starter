class Owner:
    name: str
    pets: list  # List of PetInformation objects

    def __init__(self, name: str):
        ...

    def getOwnerName(self) -> str:
        ...

    def addPet(self, pet: 'PetInformation') -> None:
        ...

    def removePet(self, pet: 'PetInformation') -> None:
        ...

    def getPets(self) -> list:
        ...

    def getPetCount(self) -> int:
        ...

    def getAllTasks(self) -> list:
        ...

    def getTotalTaskCount(self) -> int:
        ...


class Scheduler:
    owner: 'Owner'

    def __init__(self, owner: 'Owner'):
        ...

    def getAllTasks(self) -> list:
        return self.owner.getAllTasks()

    def getTasksByFrequency(self, frequency: str) -> list:
        ...

    def getTasksByTime(self, time: str) -> list:
        ...

    def getTasksByPet(self, pet: 'PetInformation') -> list:
        ...

    def getCompletedTasks(self) -> list:
        ...

    def getIncompleteTasks(self) -> list:
        ...

    def sortTasksByTime(self) -> list:
        ...

    def sortTasksByFrequency(self) -> list:
        ...

    def markTaskComplete(self, task: 'Task') -> None:
        ...

    def resetAllTasks(self) -> None:
        ...

    def getScheduleForDay(self, day: str) -> list:
        ...


class Task:
    description: str
    time: str
    frequency: str
    completion_status: bool

    def __init__(self, description: str, time: str, frequency: str):
        ...

    def getDescription(self) -> str:
        ...

    def getTime(self) -> str:
        ...

    def getFrequency(self) -> str:
        ...

    def getCompletionStatus(self) -> bool:
        ...

    def markComplete(self) -> None:
        ...

    def resetTask(self) -> None:
        ...


class PetInformation:
    name: str
    age: int
    breed: str
    color: str
    tasks: list  # List of Task objects

    def __init__(self, name: str, age: int, breed: str, color: str):
        ...

    def getPetName(self) -> str:
        ...

    def getAge(self) -> int:
        ...

    def getBreed(self) -> str:
        ...

    def getColor(self) -> str:
        ...

    def addTask(self, task: 'Task') -> None:
        ...

    def removeTask(self, task: 'Task') -> None:
        ...

    def getTasks(self) -> list:
        ...

    def getTaskCount(self) -> int:
        ...


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
