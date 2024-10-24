import unittest
import logging
from tests_12_2 import Runner, Tournament

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def skip_if_frozen(func):
        def wrapper(*args, **kwargs):
            if args[0].is_frozen:
                logging.info("Тесты в этом кейсе заморожены")
                raise unittest.SkipTest("Тесты в этом кейсе заморожены")
            return func(*args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Тест", 10)
        runner.walk()
        self.assertEqual(runner.distance, 10)
        logging.info('"test_walk" выполнен успешно')

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Тест", 10)
        runner.run()
        self.assertEqual(runner.distance, 20)
        logging.info('"test_run" выполнен успешно')

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Усэйн", 10)
        runner2 = Runner("Ник", 3)
        runner1.run()
        runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
        logging.info('"test_challenge" выполнен успешно')


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def skip_if_frozen(func):
        def wrapper(*args, **kwargs):
            if args[0].is_frozen:
                logging.info("Тесты в этом кейсе заморожены")
                raise unittest.SkipTest("Тесты в этом кейсе заморожены")
            return func(*args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_first_tournament(self):
        runner1 = Runner("Усэйн", 10)
        runner2 = Runner("Ник", 3)
        tournament = Tournament(90, runner1, runner2)
        results = tournament.start()
        self.assertTrue(results[1] == runner1)
        logging.info('"test_first_tournament" выполнен успешно')

    @skip_if_frozen
    def test_second_tournament(self):
        runner1 = Runner("Андрей", 9)
        runner2 = Runner("Ник", 3)
        tournament = Tournament(90, runner1, runner2)
        results = tournament.start()
        self.assertTrue(results[1] == runner1)
        logging.info('"test_second_tournament" выполнен успешно')

    @skip_if_frozen
    def test_third_tournament(self):
        runner1 = Runner("Андрей", 9)
        runner2 = Runner("Усэйн", 10)
        runner3 = Runner("Ник", 3)
        tournament = Tournament(90, runner1, runner2, runner3)
        results = tournament.start()
        self.assertTrue(results[1] == runner1 or results[1] == runner2)
        logging.info('"test_third_tournament" выполнен успешно')


if __name__ == "__main__":
    unittest.main()
