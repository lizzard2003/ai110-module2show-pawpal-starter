class PetInformation:
    name: str
    age: int
    breed: str
    color: str

    def getPetName(self) -> str:
        ...

    def getAge(self) -> int:
        ...

    def getBreed(self) -> str:
        ...

    def getColor(self) -> str:
        ...


class PetTasks:
    def feedPet(self) -> str:
        ...

    def walkPet(self) -> str:
        ...

    def petSit(self) -> str:
        ...


class TimeConstraint:
    taskDuration: str
    availability: str
    repetition: str

    def getTaskDuration(self) -> int:
        ...

    def getAvailability(self) -> int:
        ...

    def getRepetition(self) -> str:
        ...
