import unittest

from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)  # Быстрый
        self.runner2 = Runner("Андрей", 9)  # Средний
        self.runner3 = Runner("Ник", 3)     # Медленный

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            finishers = cls.all_results[key]
            result = {place: str(runner) for place, runner in finishers.items()}
            print(result)

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[1] = results
        self.assertTrue(results[max(results.keys())] == self.runner3)

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[2] = results
        self.assertTrue(results[max(results.keys())] == self.runner3)

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[3] = results
        self.assertTrue(results[max(results.keys())] == self.runner3)

    def test_runner_speed_logic(self):
        tournament = Tournament(100, self.runner1, self.runner3)
        results = tournament.start()
        self.assertEqual(list(results.values())[0], self.runner1)
        self.assertEqual(list(results.values())[-1], self.runner3)

    def test_runner_speed_logic_andrey_nick(self):
        tournament = Tournament(100, self.runner2, self.runner3)
        results = tournament.start()
        self.assertEqual(list(results.values())[0], self.runner2)
        self.assertEqual(list(results.values())[-1], self.runner3)

if __name__ == "__main__":
    unittest.main()
