from owlready2 import *

import Tank


class Ontology:

    def __init__(self, path=r"file://ontology/TANK5.owl"):
        self.__ontology = get_ontology(path).load()
        owlready2.sync_reasoner()

    def getOntology(self):
        return self.__ontology

    def getClasses(self):
        return list(self.__ontology.classes())

    def getNation(self):
        return self.__ontology.search(type=self.__ontology.Nation)

    def getTank(self):
        return self.__ontology.search(type=self.__ontology.Tank)

    def getGun(self):
        return self.__ontology.search(type=self.__ontology.Gun)

    def getСamouflage(self):
        return self.__ontology.search(type=self.__ontology.Сamouflage)

    def getEngine(self):
        return self.__ontology.search(type=self.__ontology.Engine)

    def getCrew(self):
        return self.__ontology.search(type=self.__ontology.Crew)

    def getDestroyer(self):
        return self.__ontology.search(type=self.__ontology.Destroyer)

    def getHavy(self):
        return self.__ontology.search(type=self.__ontology.Havy)

    def getMedium(self):
        return self.__ontology.search(type=self.__ontology.Medium)

    def getTypeTank(self):
        return self.__ontology.search(type=self.__ontology.Type_Tank)

    def getDriver(self):
        return self.__ontology.search(type=self.__ontology.Driver)

    def getGunner(self):
        return self.__ontology.search(type=self.__ontology.Gunner)

    def getCommander(self):
        return self.__ontology.search(type=self.__ontology.Commander)

    def choosePreferenceTank(self, tank):
        allTanks = self.getTank()
        if len(tank.getNation()) != 0:
            nations = tank.getNation()
            for _, tanks in enumerate(list(allTanks)):
                if tanks.Have_nation:
                    for _, nation in enumerate(tanks.Have_nation):
                        if not (nation.name in nations):
                            if tanks in allTanks:
                                allTanks.remove(tanks)
        print(allTanks)
        if len(tank.getGun()) != 0:
            guns = tank.getGun()
            for _, tanks in enumerate(list(allTanks)):
                if tanks.Have_Gun:
                    for _, gun in enumerate(tanks.Have_Gun):
                        if not (gun.name in guns):
                            if tanks in allTanks:
                                allTanks.remove(tanks)
        print(allTanks)
        if len(tank.getEngine()) != 0:
            engines = tank.getEngine()
            for _, tanks in enumerate(list(allTanks)):
                if tanks.Have_Engine:
                    for _, engine in enumerate(tanks.Have_Engine):
                        if not (engine.name in engines):
                            if tanks in allTanks:
                                allTanks.remove(tanks)
        print(allTanks)
        if len(tank.getCamouflage()) != 0:
            camouflages = tank.getCamouflage()
            for _, tanks in enumerate(list(allTanks)):
                if tanks.Have_Camouflage:
                    for _, camouflage in enumerate(tanks.Have_Camouflage):
                        if not (camouflage.name in camouflages):
                            if tanks in allTanks:
                                allTanks.remove(tanks)
        print(allTanks)
        if len(tank.getType()) != 0:
            types = tank.getType()
            print("-----------")
            print(types)
            print(len(types))
            print("-------------")
            if len(types) == 1:
                if types[0] == "Medium":
                    types.remove(types[0])
                    types.append("Нavy")
                    types.append("Destroyer")
                elif types[0] == "Нavy":
                    types.remove(types[0])
                    types.append("Medium")
                    types.append("Destroyer")
                elif types[0] == "Destroyer":
                    types.remove(types[0])
                    types.append("Нavy")
                    types.append("Medium")
                print(types)
                classes = self.getClasses()
                for i in range(len(classes)):
                    for j in range(len(types)):
                        if classes[i].name == types[j]:
                            for k in classes[i].instances():
                                print(k)
                                if (k in allTanks):
                                    allTanks.remove(k)
        print(allTanks)
        """
        if len(tank.getCrew()) != 0:
            crews = tank.getCrew()
            for _, tanks in enumerate(list(allTanks)):
                allCrew = tanks.Driver + tanks.Gunner + tanks.Commander + tanks.Have_staff;
                if tanks.Driver or tanks.Gunner or tanks.Commander or tanks.Have_staff:
                    for _, crew in enumerate(allCrew):
                        if not (crew.name in crews):
                            print(crew.name)
                            print(crews)
                            if tanks in allTanks:
                                allTanks.remove(tanks) """
        if len(tank.getCrew()) != 0:
            crews = tank.getCrew()
            for _, tanks in enumerate(list(allTanks)):
                allCrew = tanks.Driver + tanks.Gunner + tanks.Commander + tanks.Have_staff
                if any(crew.name not in crews for crew in allCrew):
                    allTanks.remove(tanks)
        print(allTanks)
        if tank.getAtackSpeed() is not None:
            atack_speads = tank.getAtackSpeed()
            for i, tanks in enumerate(list(allTanks)):
                if tanks.Atack_Spead == atack_speads:
                    if tanks in allTanks:
                        allTanks.remove(tanks)
        print(allTanks)
        #    def __init__(self, nation=None, gun=None, camouflage=None, engine=None, type=None, crew=None, atackSpeed = None,):

        for i, tanks in enumerate(allTanks):
            allTanks[i] = Tank.Tank(nation=tanks.Have_nation if tanks.Have_nation else None,
                                    gun=tanks.Have_Gun if tanks.Have_Gun else None,
                                    camouflage=tanks.Have_Camouflage if tanks.Have_Camouflage else None,
                                    engine=tanks.Have_Engine if tanks.Have_Engine else None,
                                    type=tanks.Have_Engine if tanks.Have_Engine else None,
                                    driver=tanks.Driver if tanks.Driver else None,
                                    guner=tanks.Gunner if tanks.Gunner else None,
                                    commander=tanks.Commander if tanks.Commander else None,
                                    atackSpeed=tanks.Atack_Spead if tanks.Atack_Spead else None,
                                    name=tanks.name
                                    )
        print(*allTanks)
