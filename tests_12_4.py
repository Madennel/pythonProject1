import unittest
import logging
from rt_with_exceptions import Runner, Tournament

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Тест", -1)  # Передаем отрицательное значение
        except ValueError:
            logging.warning("Неверная скорость для Runner")
        else:
            runner.walk()
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(12345)  # Передаем некорректный тип
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
        else:
            runner.run()
            logging.info('"test_run" выполнен успешно')

    def test_distance_after_run(self):
        runner = Runner("Тест", 10)
        runner.run()
        self.assertEqual(runner.distance, 20)
        logging.info('"test_distance_after_run" выполнен успешно')

    def test_distance_after_walk(self):
        runner = Runner("Тест", 10)
        runner.walk()
        self.assertEqual(runner.distance, 10)
        logging.info('"test_distance_after_walk" выполнен успешно')

class TournamentTest(unittest.TestCase):
    def test_tournament(self):
        runner1 = Runner("Усэйн", 10)
        runner2 = Runner("Ник", 3)
        tournament = Tournament(90, runner1, runner2)
        results = tournament.start()
        self.assertTrue(results[1] == runner1)
        logging.info('"test_tournament" выполнен успешно')

if __name__ == "__main__":
    unittest.main()
