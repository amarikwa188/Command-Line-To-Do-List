import sys

to_do: dict[str:str] = {}


def print_list() -> None:
    """
    Print out the to-do list.
    """
    print("To-Do List:")
    if not to_do:
        print("Empty\n")
        return None
    for idx, task in enumerate(to_do, 1):
        print(f"({idx}) {task}...{to_do.get(task)}")
    print()


def add_task(task: str) -> None:
    """
    Add a task to the to-do list.\n
    :param task: task to be added
    """
    if task == '/cancel':
        print()
        return None
    if task not in to_do:
        to_do[task] = "not completed"
        print(f"Adding '{task}' to the to-do list.\n")
    else:
        print(f"'{task}' is already on the to-do list.\n")


def delete_task(number: int) -> None:
    """
    Delete a task from the to-do list.\n
    :param number: task number
    """
    if number > len(to_do) or number < 0:
        print(f"Invalid input: Task number {number} does not exist.\n")
        return None

    for idx, task in enumerate(to_do, 1):
        if idx == number:
            del to_do[task]
            print(f"Removing '{task}' from the to-do list.\n")
            return None


def clear_list() -> None:
    """
    Clear all tasks from the to-do list.
    """
    if to_do:
        to_do.clear()
        print("Clearing all tasks from list\n")
    else:
        print("To-Do list is already empty.\n")


def mark_as_complete(number: int) -> None:
    """
    Mark a task as complete.\n
    :param number: task number
    """
    if number > len(to_do) or number < 0:
        print(f"Invalid input: Task number {number} does not exist.\n")
        return None

    for idx, task in enumerate(to_do, 1):
        if idx == number:
            if to_do[task] == 'completed!':
                print(f"'{task}' is already marked as completed.\n")
                return None
            to_do[task] = 'completed!'
            print(f"Marking '{task}' as completed...\n")
            return None


def print_commands() -> None:
    """
    Print all program commands.
    """
    print("To-Do List Command Options: \n"
          "# - COMMAND \n"
          "------------------------ \n"
          "1 - Print List \n"
          "2 - Add Task \n"
          "3 - Mark Task As Done \n"
          "4 - Delete Task \n"
          "5 - Clear List \n"
          "6 - Print List Commands \n"
          "0 - Exit \n"
          "------------------------\n"
          "Type '/cancel' to cancel a command.\n")


def close_list() -> None:
    """
    Close the to-do list and terminate the program.
    """
    print(f"Closing to-do list...")
    sys.exit()


if __name__ == '__main__':
    print_commands()
    com: str = input("Enter a command(#):\n>").strip()
    while com != '0':
        match com:
            case '1':
                print("[PRINT LIST]")
                print_list()
            case '2':
                print("[ADD TASK]")
                add_task(input("Enter task: "))
            case '3':
                print("[MARK TASK AS DONE]")
                action = input("Enter task number(#): ").strip()
                try:
                    mark_as_complete(int(action))
                except ValueError:
                    if action == '/cancel':
                        print()
                        com = input("Enter a command(#):\n>").strip()
                        continue
                    print("Invalid task number\n")
            case '4':
                print("[DELETE TASK]")
                action = input("Enter task number(#): ").strip()
                try:
                    delete_task(int(action))
                except ValueError:
                    if action == '/cancel':
                        print()
                        com = input("Enter a command(#):\n>").strip()
                        continue
                    print("Invalid task number\n")
            case '5':
                print("[CLEAR LIST]")
                clear_list()
            case '6':
                print("[PRINT COMMANDS]")
                print_commands()
            case _:
                print("Invalid command.\n")

        com = input("Enter a command(#):\n>").strip()

    print("[EXIT]")
    close_list()
