import unittest

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def skip_if_frozen(func):
        def wrapper(*args, **kwargs):
            if args[0].is_frozen:
                print("Тесты в этом кейсе заморожены.")
                return unittest.skip("Тесты в этом кейсе заморожены.")(func)(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Тест", 5)
        runner.walk()
        self.assertEqual(runner.distance, 5)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Тест", 5)
        runner.run()
        self.assertEqual(runner.distance, 10)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Усэйн", 10)
        runner2 = Runner("Ник", 3)
        runner1.run()
        runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
