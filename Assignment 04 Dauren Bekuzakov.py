from abc import ABC, abstractmethod

class Toyota(ABC):
    @abstractmethod
    def toyota_method(self):
        pass

class Camry(Toyota):
    def toyota_method(self):
        return "V8 Engine"

class Corolla(Toyota):
    def toyota_method(self):
        return "V6 Engine"

class ToyotaFactory:
    def create_toyota(self, toyota_type):
        if toyota_type == "Camry":
            return Camry()
        elif toyota_type == "Corolla":
            return Corolla()
        else:
            raise ValueError("Такого нету")

if __name__ == "__main__":
    factory = ToyotaFactory()

    camry = factory.create_toyota("Camry")
    corolla = factory.create_toyota("Corolla")

    print(camry.toyota_method())
    print(corolla.toyota_method())