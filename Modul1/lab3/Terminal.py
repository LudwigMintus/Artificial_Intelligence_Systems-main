from Ontology import Ontology
from Tank import Tank
from exceptions.IncorrectValueException import IncorrectValueException
from validators.ArgsValidator import ArgsValidator

MAX_FOR_PARAMETER = 1
SEPARATOR = ','
typetank = ['Destroyer', 'Havy', 'Medium']
speedAtack = ['1', '2', '3']



class Terminal:

    def __init__(self):
        self.__tank = None
        self.__ontology = Ontology()

    def work(self):
        try:
            print('Добрый день! Данная программа поможет Вам найти подходящий танк:)')
            self.enterArguments()
            self.getPreferTank()
        except IncorrectValueException as ex:
            print(ex.message)
            return

    def enterArguments(self):
       print('Вам необходимо будет ввести информацию, чтобы мы подобрали танк, соответствующую именно Вам!')
       nation = self.__enterNation()
       gun = self.__enterGun()
       engine = self.__enterEngine()
       camouflag = self.__enterСamouflage()
       crew = self.__enterCrew()
       type = self.__enterType()
       speedAt = self.__attackSpeed()
       self.__tank = Tank(nation=nation, gun=gun, camouflage=camouflag, engine=engine, driver=None, guner=None,
                 commander=None, type=type, crew=crew,
                          atackSpeed=speedAt)

    def __enterNation(self):
        print(
            f'\nВведите нации, которые Вам подходят, через запятую. Если Вы не хотите учитывать данный параметр, '
            f'введите "-".')
        print(f'Список возможных жанров:')
        nation = [element.name for element in self.__ontology.getNation()]
        print(*nation, sep=SEPARATOR)
        try:
            return ArgsValidator.validateLists(input("Ваши данные:"), nation)
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__enterNation()

    def __enterGun(self):
        print(
            f'\nВведите пушек, которые Вам подходят, через запятую. Если Вы не хотите учитывать данный параметр, '
            f'введите "-".')
        print(f'Список возможных пушек:')
        gun = [element.name for element in self.__ontology.getGun()]
        print(*gun, sep=SEPARATOR)
        try:
            return ArgsValidator.validateLists(input("Ваши данные:"), gun)
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__enterGun()

    def __enterEngine(self):
        print(
            f'\nВведите двигатели, которые Вам подходят, через запятую. Если Вы не хотите учитывать данный параметр, '
            f'введите "-".')
        print(f'Список возможных двигателей:')
        engine = [element.name for element in self.__ontology.getEngine()]
        print(*engine, sep=SEPARATOR)
        try:
            return ArgsValidator.validateLists(input("Ваши данные:"), engine)
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__enterEngine()

    def __enterСamouflage(self):
        print(
            f'\nВведите камуфляжи, которые Вам подходят, через запятую. Если Вы не хотите учитывать данный параметр, '
            f'введите "-".')
        print(f'Список возможных камуфляжей:')
        camouflage = [element.name for element in self.__ontology.getСamouflage()]
        print(*camouflage, sep=SEPARATOR)
        try:
            return ArgsValidator.validateLists(input("Ваши данные:"), camouflage)
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__enterСamouflage()

    def __enterCrew(self):
        print(f'\nВведите членов экипажа, которые Вам подходят, через запятую. Если Вы не хотите '
              f'учитывать данный параметр, 'f'введите "-".')
        print(f'Список екипажа танков:')
        crew = [element.name for element in self.__ontology.getCrew()]
        print(*crew, sep=SEPARATOR)
        #for i in range(0, len(crew) - 1, 7):
        #    print(*crew[i:i + 6], sep=SEPARATOR)
        try:
            return ArgsValidator.validateLists(input("Ваши данные:"), crew)
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__enterCrew()

    def __enterType(self):
        print(f'\nВведите тип танка, которые Вам подходят только одно. Если Вы не хотите '
              f'учитывать данный параметр, 'f'введите "-".')
        print(f'Список типа танков:')
        print(*typetank, sep=SEPARATOR)
        try:
            return ArgsValidator.validateLists(input("Ваши данные:"), typetank)
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__enterType()

    def __attackSpeed(self):
        print(f'\nВведите скорость атаки, которые Вам подходят, через запятую. Если Вы не хотите '
              f'учитывать данный параметр, 'f'введите "-".')
        print(f'Список скоростей атаки:')
        print(*speedAtack, sep=SEPARATOR)
        try:
            return ArgsValidator.validateLists(input("Ваши данные:"), speedAtack)
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__attackSpeed()

    def getPreferTank(self):
         print(f'Итак, подобранные специально для Вас игры...\n')
         self.__ontology.choosePreferenceTank(self.__tank)