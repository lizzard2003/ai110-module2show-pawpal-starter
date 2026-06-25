# import classes from pawpal_system
from pawpal_system import Owner, Scheduler, PetInformation, Task, PetTasks, TimeConstraint

owner = Owner("John Doe")

pet1 = PetInformation("Toby", 3, "Australian Shepherd", "black and white")
pet2 = PetInformation("Mittens", 2, "Tortoiseshell", "multicolor")

owner.addPet(pet1)
owner.addPet(pet2)

# Three tasks at different times for the pets
breakfast_task = Task("Feed Toby breakfast", "09:00", "daily")
walk_task = Task("Walk Mittens", "12:30", "daily")
dinner_task = Task("Feed Toby dinner", "18:00", "daily")

pet1.addTask(breakfast_task)
pet2.addTask(walk_task)
pet1.addTask(dinner_task)

scheduler = Scheduler(owner)
today_schedule = scheduler.getScheduleForDay("today")

print("Today's schedule:")
for task in today_schedule:
    print(f"- {task.time} | {task.description} ({task.frequency})")