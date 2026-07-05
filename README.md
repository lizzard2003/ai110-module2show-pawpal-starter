# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature           | Method(s) | Notes                             |
| ----------------- | --------- | --------------------------------- |
| Task sorting      |           | e.g., by priority, duration       |
| Filtering         |           | e.g., skip tasks if time runs out |
| Conflict handling |           | e.g., overlapping time slots      |
| Recurring tasks   |           | e.g., daily vs. weekly            |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or link to a demo video here -->

**Sample Output**

````Today's schedule:
- 09:00 | Feed Toby breakfast (daily)
- 18:00 | Feed Toby dinner (daily)
- 12:30 | Walk Mittens (daily)```
````

**Testing PawPal+**
run python3 -m pytest

TestTimeToMinutes — the time parser (13 tests)
Converts "HH:MM" to minutes-since-midnight. Checks midnight/typical/end-of-day values, that single-digit 9:00 equals 09:00, and that garbage input raises ValueError (wrong shape like "0800", out-of-range like "24:00"/"08:60", non-numeric like "ab:cd").

TestTask — a single task (19 tests)
Defaults (starts incomplete, due today), frequency lowercased, time/frequency validated at construction. Big focus on recurrence (next_occurrence): daily/weekly advance by a fixed interval; monthly advances a calendar month — keeping day-of-month (15th→15th), clamping short months (Jan 31→Feb 28), leap day (Jan 31 2024→Feb 29), and year rollover (Dec→Jan). Also confirms the follow-up is a fresh, incomplete copy and advances from the task's own due date, not today.

TestPetInformation / TestOwner — the data model (6 tests)
Getters, add/remove pets and tasks, counts, and that an owner aggregates tasks across all its pets.

TestSchedulerFiltering — querying tasks (9 tests)
Filter by pet (object or case-insensitive name, unknown name → empty), by frequency (case-insensitive), completed vs. incomplete, combined filters, and lookup by clock time.

TestSchedulerSorting — ordering (10 tests)
The chronological guarantees: output is non-decreasing, 9:00 sorts before 10:00 (not as text), ties are stable, the input list isn't mutated, and ordering is date-then-time (a task due sooner comes first even if its clock time is later). Plus getScheduleForDay mapping today→daily.

TestSchedulerConflicts — collision detection (8 tests)
No conflict when times differ; flags same-pet and cross-pet clashes; a 3-way collision reports all tasks but distinct pets; same time on different dates is not a conflict; conflicts come back chronologically; human-readable warnings; and conflict_warnings never raises even if detection blows up.

=================================================================== test session starts ====================================================================
platform darwin -- Python 3.11.1, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/liz/pawpalProject/ai110-module2show-pawpal-starter
plugins: anyio-4.14.1
collected 75 items

tests/test_pawpal.py ........................................................................... [100%]

==================================================================== 75 passed in 0.25s ====================================================================

**Confidence Level**
I am really confident that the test passed all test edge cases for a working app. 5 star confindence.
