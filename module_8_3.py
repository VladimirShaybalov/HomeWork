class IncorrectVinNumber(Exception):
    def __init__ (self,message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__ (self,message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

        if not self.__is_valid_vin(self.__vin):
            raise IncorrectVinNumber ('Некоректный тип vin номер') # Выбрасываем исключенеие, если VIN некорретен

        if not self.__is_valid_numbers(self.__numbers):
            raise IncorrectCarNumbers ('Некорректный тип данных для номеров') # Выбрасываем исключения если номера не корректны

        # Приватный метод, для проверки корректности VIN
    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int): # Проверка на целое число
            raise IncorrectVinNumber('Некорректный тип vin номер') # Выбрасываем исключение, если тип некорректен

        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber ('Неверный диапазон для VIN номера') # Выбрасываем исключение, если номер вне диапазона

        return True # Если проверки пройдены возвращаем True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров') # Выбрасываем исключение если тип некорректен

        if len(numbers) !=6: #Проверка на длину строки
            raise IncorrectCarNumbers ('Неверная длинна номера') # Выбрасываем исключение если длинна некорректна

        return True # Возвращаем True если проверки пройдены

# Примеры использования классов и обработки исключений
try:
    first = Car('Model1', 1000000, 'f123dj')  # Создаем объект Car с корректными данными
except IncorrectVinNumber as exc:
    print(exc.message)  # Если возникло исключение IncorrectVinNumber, выводим сообщение об ошибке
except IncorrectCarNumbers as exc:
    print(exc.message)  # Если возникло исключение IncorrectCarNumbers, выводим сообщение об ошибке
else:
    print(f'{first.model} успешно создан')  # Если объект создан успешно, выводим сообщение

try:
    second = Car('Model2', 300, 'т001тр')  # Создаем объект Car с некорректным VIN номером
except IncorrectVinNumber as exc:
    print(exc.message)  # Выводим сообщение об ошибке для некорректного VIN номера
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')  # Создаем объект Car с некорректными номерами
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

