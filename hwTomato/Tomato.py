class Tomato:

    # Стадии созревания помидора
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Переход к следующей стадии созревания
    def grow(self):
        self._change_state()

    # Проверка, созрел ли томат
    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    # Защищенные(protected) методы

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print("Tomato", self._index, "is", Tomato.states[self._state])

class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = self._generate_tomatos(num)
        # self.tomatoes = [Tomato(index) for index in range(0, num-1)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        # return all([tomato.is_ripe() for tomato in self.tomatoes])
        ripe_tomatoes = 0
        for tomato in self.tomatoes:
            if tomato.is_ripe():
                ripe_tomatoes += 1
        if ripe_tomatoes == len(self.tomatoes):
            return True
        return False


    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []

    def _generate_tomatos(self, num):
        list = []
        for i in range(1,num+1):
            tomato = Tomato(i)
            list.append(tomato)
        return list

class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Gardener finished')

    # Собираем урожай
    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early! Your plant is green and not ripe.')

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''Harvest time for tomatoes should ideally occur
when the fruit is a mature green and
then allowed to ripen off the vine.
This prevents splitting or bruising
and allows for a measure of control over the ripening process.''')

kust1 = TomatoBush(5)

g = Gardener("Sadovnik", kust1)

g.work()
kust1.tomatoes[1].grow()
g.work()
print(kust1.all_are_ripe())