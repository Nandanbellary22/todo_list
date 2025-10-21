from time import sleep


def add_task(task_list, task):
    """Add a task to the task list."""
    task_list.append(task)
    return task_list

def remove_task_by_index(task_list, index):
    """Remove a task by its index in the list. Returns the removed task or None.

    Index must be a valid integer between 0 and len(task_list)-1.
    """
    if index < 0 or index >= len(task_list):
        return None
    return task_list.pop(index)


def view_tasks(task_list):
    """Return all tasks from the task list."""
    return list(task_list)

def save_tasks(task_list, filename):
    """Save the full list of tasks to a file (overwrites).

    Writes each task on its own line. Uses UTF-8 encoding.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for task in task_list:
            file.write(task.rstrip('\n') + '\n')


def load_tasks(filename):
    """Load tasks from a file and return a list of tasks.

    If the file doesn't exist an empty list is returned.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.rstrip('\n') for line in f if line.strip()]
    except FileNotFoundError:
        return []


def main_loop():
    filename = 'tasks.txt'
    task_list = load_tasks(filename)

    while True:
        print('\nTo-Do List Manager')
        sleep(0.3)
        print('1. Add Task')
        sleep(0.3)
        print('2. Remove Task')
        sleep(0.3)
        print('3. View Tasks')
        sleep(0.3)
        print('4. Exit')
        sleep(0.3)
        choice = input('Choose an option (1-4): ').strip()
        if choice == '4':
            sleep(0.5)
            print('Exiting the To-Do List Manager. Goodbye!')
            break
        elif choice == '1':
            task = input('Enter the task to add: ').strip()
            if task:
                add_task(task_list, task)
                save_tasks(task_list, filename)
                sleep(0.5)
                print(f"Task '{task}' added.")
            else:
                print('No task entered; nothing added.')
        elif choice == '2':
            # show numbered tasks first
            if not task_list:
                print('No tasks to remove.')
            else:
                sleep(0.3)
                print('Current Tasks:')
                for i, t in enumerate(task_list):
                    print(f'{i+1}: {t}')
                    sleep(0.2)
                idx_str = input('Enter the index of the task to remove: ').strip()
                try:
                    idx = int(idx_str)
                except ValueError:
                    print('Invalid index. Please enter a number.')
                else:
                    removed = remove_task_by_index(task_list, idx-1)
                    if removed is None:
                        print('Index out of range.')
                    else:
                        save_tasks(task_list, filename)
                        sleep(0.5)
                        print(f"Removed task: '{removed}'")
        elif choice == '3':
            tasks = view_tasks(task_list)
            if not tasks:
                print('No tasks found.')
            else:
                print('Current Tasks:')
                for t in tasks:
                    sleep(0.2)
                    print(f'- {t}')
        else:
            print('Invalid choice. Please select a valid option.')
        sleep(1)


if __name__ == '__main__':
    main_loop()