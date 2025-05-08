class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= items * 10


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self._fuelRate = min(max(fuelRate, 0), 100)
        self._velocity = min(max(velocity, 0), 200)

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        self._fuelRate = min(max(value, 0), 100)

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = min(max(value, 0), 200)

    def run(self, velocity, distance):
        self.velocity = velocity
        fuel_needed = distance / 10  
        if self.fuelRate >= fuel_needed:
            self.fuelRate -= fuel_needed
            self.stop(0)
        else:
            travel_distance = self.fuelRate * 10
            self.fuelRate = 0
            self.stop(distance - travel_distance)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"Stopped! You have {remaining_distance}km left to reach your destination.")
        else:
            print("You arrived at your destination.")


class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def drive(self, distance):
        self.car.run(self.car.velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount
        if self.car.fuelRate > 100:
            self.car.fuelRate = 100

    def send_mail(self, to, subject, body):
        print(f"Sending mail to: {to}\nSubject: {subject}\nBody: {body}")


class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.id != emp_id]
        Office.employeesNum -= 1

    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= deduction

    def reward(self, emp_id, reward):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += reward

    def check_lateness(self, emp_id, moveHour):
        emp = self.get_employee(emp_id)
        if not emp:
            print("Employee not found.")
            return
        is_late = Office.calculate_lateness(9, moveHour, emp.distanceToWork, emp.car.velocity)
        if is_late:
            self.deduct(emp_id, 10)
        else:
            self.reward(emp_id, 10)
        

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):

        if velocity == 0:
                print("Can't calculate lateness: velocity is zero!")
                return True  
        arrivalTime = moveHour + (distance / velocity)
        return arrivalTime > targetHour




    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

my_car = Car(name="Toyota", fuelRate=80, velocity=100)

employee1 = Employee(
    name="Ali",
    money=1000,
    mood="Neutral",
    healthRate=75,
    emp_id=1,
    car=my_car,
    email="ali@example.com",
    salary=5000,
    distanceToWork=30  
)

my_office = Office("TechCorp")
my_office.hire(employee1)

employee1.sleep(6)
print(f"{employee1.name}'s mood after sleep: {employee1.mood}")

employee1.eat(2)
print(f"{employee1.name}'s healthRate after eating: {employee1.healthRate}%")

employee1.buy(3)
print(f"{employee1.name}'s money after buying 3 items: {employee1.money} L.E")

employee1.drive(employee1.distanceToWork)

my_office.check_lateness(emp_id=1, moveHour=8)  

print(f"{employee1.name}'s salary after lateness check: {employee1.salary} L.E")

print("All Employees:")
for emp in my_office.get_all_employees():
    print(f"- {emp.name} (ID: {emp.id})")
