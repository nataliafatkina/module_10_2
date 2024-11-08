import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self, enemy = 100):
        print(f'{self.name}, на нас напали!')
        count = 0
        while enemy > 0:
            sleep(1)
            enemy -= self.power
            count += 1
            print(f'{self.name} сражается {count} день(дня), осталось {enemy} воинов.')
        print(f'{self.name} одержал победу спустя {count} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')