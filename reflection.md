# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
  My initial design is to have 3 different classes :
  Pet information
  Pet tasks
  Time Constraint
- What classes did you include, and what responsibilities did you assign to each?
  Classes : |Attributes :
  Pet information |Pet breed, name, pet age
  Pet tasks | Walks, feedings, pet sitting
  Time Constraints | avaliability , duration of tasks, repetition

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
  After I asked Claude about relationships and bottle necks. It gave me feedback on my skeleton not being connected to one another. A task list attribute was added to pet information to list tasks needed for that specific pet. All 3 classes have been added a **init** constructor and corrections have been made to return data types.
  On the diagram it was updated by adding a relationship where Petinformation manages PetTasks and PetTasks has TimeConstraints.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)? It considers time .
- How did you decide which constraints mattered most? The constraint matter the most because if you have 2 tasks at the same time they will intervine with one another and cause bad customer service.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
  The redundant sort was a trade off. It would sort time over and over on each run. The other problem was that time was constraining it self with one another. This would be because we didnt know if it was 9:00 am pr 9:00 pm. That was fixed by doing a military time change.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

# 6. Smart Scheduling

a. Sorting Behaviors -
sort_by_time() - Orders tasks chronologically earliest first,
sortTaskVyFrequency - Groups tasls by frequency alphabetachally : daily , monthly, weekly
detectConflicts()= Acompound (tuple) sort: conflicts are ordered by due date first then by time within a date.

b. Filtering Behaviors -
GetScheduleForDay()= first filters out frequency then sorts the time.

c. Conflict Detection =
detectConflicts()= Acompound (tuple) sort: conflicts are ordered by due date first then by time within a date.

d. Reoccurance-
Tasks are set to reoccure it is a repetitive task that is daily or weekly.
The app also pushes to next task on the list at Task.next_occurance.
Another trigger is completion. Once a task is marked as complete then it does not keep reoccuring meaning it will prevent outliers.
