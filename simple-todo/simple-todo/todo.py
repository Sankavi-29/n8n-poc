import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def main():
    tasks = load_tasks()

    while True:
        print("\n==== To-Do App ====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to remove: "))
                tasks.pop(num-1)
                save_tasks(tasks)
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
