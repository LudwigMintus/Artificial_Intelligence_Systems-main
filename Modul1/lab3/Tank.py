class Tank:

    def __init__(self, nation=None, gun=None, camouflage=None, engine=None, type=None, driver=None, guner=None,
                 commander=None, crew=None, atackSpeed=None, name=None):
        self.__nation: list[str] = nation
        self.__gun: list[str] = gun
        self.__camouflage: list[str] = camouflage
        self.__engine: list[str] = engine
        self.__type: list[str] = type
        self.__guner: list[str] = guner
        self.__commander: list[str] = commander
        self.__driver: list[str] = driver
        self.__crew: list[str] = crew
        self.__atackSpeed: list[str] = atackSpeed
        self.__name: str = name

    def getNation(self):
        return self.__nation

    def setNation(self, nation):
        self.__nation = nation

    def getGun(self):
        return self.__gun

    def setGun(self, gun):
        self.__gun = gun

    def getCamouflage(self):
        return self.__camouflage

    def setCamouflage(self, camouflage):
        self.__camouflage = camouflage

    def getType(self):
        return self.__type

    def setTypes(self, type):
        self.__type = type

    def getEngine(self):
        return self.__engine

    def setEngine(self, engine):
        self.__engine = engine

    def getCrew(self):
        return self.__crew

    def setCrew(self, type):
        self.__crew = type

    def getAtackSpeed(self):
        return self.__atackSpeed

    def setAtackSpeed(self, atackSpeed):
        self.__atackSpeed = atackSpeed

    def getName(self):
        return self.__name

    def setAtackSpeed(self, name):
        self.__name = name

    def __str__(self):
        return (
            f"Название: {self.__name} \n"
            f"НАЦИЯ: {self.__nation} \n"
            f"\tВозможная модификация пушки: {self.__gun if self.__gun is not None else 'Нет пушки по лучше:('}\n"
            f"\tВозможная модификация камуфляжа: {self.__camouflage if self.__camouflage is not None else 'Краску продали на рынке'}\n"
            f"\tВозможная модификация двигателя: {self.__engine if self.__engine is not None else 'Майор Поставил в свой жигуль'}\n"
            f"\tЕкипаж:\nВодитель {self.__driver if self.__driver is not None else ' Водитель танка в запое'}\n"
            f"\tКомандир{self.__commander if self.__commander is not None else ' Командир танка в запое'}\n"
            f"\tЗаряжающий{self.__gun if self.__gun is not None else ' Заряжающий танка в запое'}\n"
            f"\tСкорость атаки: {self.__atackSpeed if self.__atackSpeed is not None else 'Стрелять не научили'}\n")
