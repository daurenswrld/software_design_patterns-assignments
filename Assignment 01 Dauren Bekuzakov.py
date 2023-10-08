class ToDoList:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ToDoList, cls).__new__(cls)
            cls._instance.tasks = []
        return cls._instance

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks

todo_list = ToDoList()

todo_list.add_task("Смотреть матч")
todo_list.add_task("Кататься на машине")
todo_list.add_task("Учить новый язык")

tasks = todo_list.get_tasks()
print("Список задач:")
for task in tasks:
    print(task)

todo_list.remove_task("Учить новый язык")

tasks = todo_list.get_tasks()
print("\nОбновленный список задач:")
for task in tasks:
    print(task)
