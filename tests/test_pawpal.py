from pawpal_system import Task


def test_task_completion_changes_status():
    task = Task("Feed dog", "08:00", "daily")
    assert task.getCompletionStatus() is False

    task.mark_complete()

    assert task.getCompletionStatus() is True
