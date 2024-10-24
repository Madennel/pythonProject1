import unittest
from module_12_1 import RunnerTest
from tests_12_2 import TournamentTest

# Создание объекта TestSuite
test_suite = unittest.TestSuite()

# Добавление тестов в TestSuite
test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest))
test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest))

# Создание объекта TextTestRunner
if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
