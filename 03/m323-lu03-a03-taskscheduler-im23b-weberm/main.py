"""
task
"""
import time


def task1():
    """
    Eine einfache Funktion, die eine Meldung ausgibt, um zu signalisieren, dass Task 1 ausgeführt wurde.
    """
    print("task1")


def task2():
    """
    Eine einfache Funktion, die eine Meldung ausgibt, um zu signalisieren, dass Task 2 ausgeführt wurde.
    """
    print("task2")


def task_scheduler(tasks2, delay2):
    """
    Führt eine Liste von Tasks mit einer festen Zeitverzögerung zwischen jedem Task aus.

    Args:
    tasks (list): Eine Liste von Funktionen, die ausgeführt werden sollen.
    delay (int): Die Zeitverzögerung in Sekunden zwischen den einzelnen Tasks.

    Returns:
    None
    """
    for i in tasks2:
        i()
        time.sleep(delay2)


def task_scheduler_expert(tasks1, delays1):
    """
    Führt eine Liste von Tasks mit unterschiedlichen Zeitverzögerungen zwischen jedem Task aus.

    Args:
    tasks (list): Eine Liste von Funktionen, die ausgeführt werden sollen.
    delays (list): Eine Liste von Zeitverzögerungen in Sekunden für die jeweiligen Tasks.

    Returns:
    None
    """
    for task, delay1 in zip(tasks1, delays1):
        task()
        time.sleep(delay1)


if __name__ == "__main__":
    tasks = [task1, task2]
    delay = 2
    delays = [2, 3]
    task_scheduler(tasks, delay)
    task_scheduler_expert(tasks, delays)
