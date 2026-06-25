class PetInformation:
    name: str
    age: int
    breed: str
    color: str
    tasks: list  # List of PetTasks

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
