from dataclasses import dataclass
#  lab 4

@dataclass
class Person:
    name: str
    surname: str
    age: int



    def __str__(self) -> str:
        return f' name: {self.name} \n surname: {self.surname} \n age: {self.age} \n '

# Класс Driver содержит поля - ФИО, стаж вождения.(from Person class)
@dataclass
class Driver(Person):
    experience: int

    def __str__(self) -> str:
        return super().__str__() + f'experience: {self.experience}'


# Класс Engine содержит поля - мощность, производитель.
@dataclass()
class Engine:
    power: int
    company: str

    def __str__(self) -> str:
        return f' power: {self.power} \n company: {self.company}'

# Класс Car содержит поля - марка автомобиля, класс автомобиля, вес, водитель типа Driver, мотор типа Engine.
@dataclass()
class Car:
    driver: Driver
    mark: str
    weight: float
    car_class: str
    engine: Engine

    # Метод start()
    def start(self) -> None:
        print("Gooooo")
    # Метод stop()
    def stop(self) -> None:
        print("Stoooop")
    # Метод turnRight()
    def turn_right(self) -> None:
        print("Turn right")
    # Метод turnLeft()
    def turn_left(self) -> None:
        print("Turn left")
    # метод toString() or __str__(), который выводит полную информацию об автомобиле, ее водителе и моторе.
    # __str__() method returns a more human-readable format
    def __str__(self) -> str:
        return f' driver full name: {self.driver.name} {self.driver.surname} \n class: {self.car_class} \n engine power: {self.engine.power}\n company: {self.engine.company} \n mark: {self.mark} \n weight: {self.weight}'

# Создать производный от Car класс  - Lorry (грузовик), характеризуемый также грузоподъемностью кузова.
@dataclass
class Lorry(Car):
    body_load_capacity: int

    def __str__(self) -> str:
        return super().__str__() + f'\n body load capacity: {self.body_load_capacity}'

# Создать производный от Car класс - SportCar, характеризуемый также предельной скоростью.
@dataclass
class SportCar(Car):
    top_speed: float

    def __str__(self) -> str:
        return super().__str__() + f'\n top speed: {self.top_speed}'

# EXAMPLE!!!
driver = Driver(name="James", surname="Bond", age=42, experience=20)
engine = Engine(power=250, company="Ferrari")
car = Car(car_class="Luxury", engine=engine, driver=driver, mark="488 GTB", weight=400)
print(f'Driver info:\n{driver}')
print(f'Engine info:\n{engine}')
print(f'Car info:\n{car}')
car.start()
car.stop()
car.turn_left()
car.turn_right()


lorry = Lorry(car_class="Luxury", engine=engine, driver=driver, mark="488 GTB", weight=400, body_load_capacity=1000)
print(f'Lorry info:\n{lorry}')
lorry.start()
sport_car = SportCar(car_class="Luxury", engine=engine, driver=driver, mark="488 GTB", weight=400, top_speed=310)
print(f'Sport car info:\n{sport_car}')
sport_car.stop()