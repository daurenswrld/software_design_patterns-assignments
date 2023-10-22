from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class Music(Device):
    def turn_on(self):
        print("Музыка включена")

    def turn_off(self):
        print("Музыка отключена")

class Computer(Device):
    def turn_on(self):
        print("Компьютер включен")

    def turn_off(self):
        print("Компьютер отключен")

class MusicAdapter(Device):
    def __init__(self, music):
        self.music = music

    def turn_on(self):
        self.music.turn_on()

    def turn_off(self):
        self.music.turn_off()

class ComputerAdapter(Device):
    def __init__(self, computer):
        self.computer = computer

    def turn_on(self):
        self.computer.turn_on()

    def turn_off(self):
        self.computer.turn_off()

class SmartHome:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def turn_on_all_devices(self):
        for device in self.devices:
            device.turn_on()

    def turn_off_all_devices(self):
        for device in self.devices:
            device.turn_off()

if __name__ == '__main__':
    music = Music()
    computer = Computer()

    music_adapter = MusicAdapter(music)
    computer_adapter = ComputerAdapter(computer)

    smart_home = SmartHome()
    smart_home.add_device(music_adapter)
    smart_home.add_device(computer_adapter)

    smart_home.turn_on_all_devices()
    smart_home.turn_off_all_devices()
    smart_home.turn_on_all_devices()
