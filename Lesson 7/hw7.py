import math

class Vector:
    def __init__(self, *components):
        if not components:
            raise ValueError("Vector must have at least one component")
        self.components = tuple(components)

    def __len__(self):
        return len(self.components)

    def __str__(self):
        return f"Vector{self.components}"

    def __repr__(self):
        return self.__str__()

    def _check_dimension(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")

    # Vector addition
    def __add__(self, other):
        self._check_dimension(other)
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    # Vector subtraction
    def __sub__(self, other):
        self._check_dimension(other)
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    # Dot product OR scalar multiplication
    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        else:
            raise TypeError("Unsupported operand")

    # Scalar multiplication from left side (e.g. 3 * v)
    def __rmul__(self, scalar):
        return self * scalar

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(*(round(a / mag, 3) for a in self.components))


class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    def to_file(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}\n"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        open(self.FILE_NAME, "a").close()

    def _read_all(self):
        employees = []
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                eid, name, pos, sal = line.strip().split(",")
                employees.append(Employee(eid, name, pos, float(sal)))
        return employees

    def _write_all(self, employees):
        with open(self.FILE_NAME, "w") as file:
            for emp in employees:
                file.write(emp.to_file())

    def add_employee(self, employee):
        employees = self._read_all()
        if any(emp.employee_id == employee.employee_id for emp in employees):
            print("Employee ID already exists!")
            return
        with open(self.FILE_NAME, "a") as file:
            file.write(employee.to_file())
        print("Employee added successfully!")

    def view_all(self):
        employees = self._read_all()
        if not employees:
            print("No records found.")
        for emp in employees:
            print(emp)

    def search_employee(self, employee_id):
        for emp in self._read_all():
            if emp.employee_id == employee_id:
                print("Employee Found:")
                print(emp)
                return
        print("Employee not found.")

    def update_employee(self, employee_id):
        employees = self._read_all()
        for emp in employees:
            if emp.employee_id == employee_id:
                emp.name = input("Enter new name: ")
                emp.position = input("Enter new position: ")
                emp.salary = float(input("Enter new salary: "))
                self._write_all(employees)
                print("Employee updated successfully!")
                return
        print("Employee not found.")

    def delete_employee(self, employee_id):
        employees = self._read_all()
        new_list = [emp for emp in employees if emp.employee_id != employee_id]
        if len(new_list) == len(employees):
            print("Employee not found.")
        else:
            self._write_all(new_list)
            print("Employee deleted successfully!")


def main():
    manager = EmployeeManager()

    while True:
        print("\n1. Add employee")
        print("2. View all employees")
        print("3. Search employee")
        print("4. Update employee")
        print("5. Delete employee")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            emp = Employee(
                input("ID: "),
                input("Name: "),
                input("Position: "),
                float(input("Salary: "))
            )
            manager.add_employee(emp)

        elif choice == "2":
            manager.view_all()

        elif choice == "3":
            manager.search_employee(input("Enter ID: "))

        elif choice == "4":
            manager.update_employee(input("Enter ID: "))

        elif choice == "5":
            manager.delete_employee(input("Enter ID: "))

        elif choice == "6":
            print("Goodbye!")
            break


class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, tasks): pass

    @abstractmethod
    def load(self): pass


import json

class JSONStorage(Storage):
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w") as file:
            json.dump([task.__dict__ for task in tasks], file, indent=4)

    def load(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Task(**item) for item in data]
        except FileNotFoundError:
            return []


class ToDoApp:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = storage.load()

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("New title: ")
                task.description = input("New description: ")
                task.status = input("New status: ")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.task_id != task_id]

    def filter_by_status(self, status):
        for task in self.tasks:
            if task.status == status:
                print(task)

    def save(self):
        self.storage.save(self.tasks)


