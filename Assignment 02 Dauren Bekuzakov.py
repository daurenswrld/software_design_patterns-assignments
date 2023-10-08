class Camry:
    def cost(self):
        return 2000 

class PanoramaDecorator:
    def __init__(self, camry):
        self._camry = camry

    def cost(self):
        return self._camry.cost() + 500

class AudioDecorator:
    def __init__(self, camry):
        self._camry = camry

    def cost(self):
        return self._camry.cost() + 200



camry = Camry()  
camry_with_panorama = PanoramaDecorator(camry)  
camry_with_audio = AudioDecorator(camry) 
camry_with_panorama_and_audio = AudioDecorator(camry_with_panorama)  

print("Цена Toyota Camry с базовой комплектацией: $", camry.cost())
print("Цена Toyota Camry с аудиосистемой JBL: $", camry_with_audio.cost())
print("Цена Toyota Camry с панорамной крышей: $", camry_with_panorama.cost())
print("Цена Toyota Camry с панорамой и аудиосистемой JBL: $", camry_with_panorama_and_audio.cost())