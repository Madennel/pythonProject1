import unittest
from module_12_1 import Runner

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[len(finishers) + 1] = participant
                    self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def skip_if_frozen(func):
        def wrapper(*args, **kwargs):
            if args[0].is_frozen:
                print("Тесты в этом кейсе заморожены.")
                return unittest.skip("Тесты в этом кейсе заморожены.")(func)(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_first_tournament(self):
        runner1 = Runner("Усэйн", 10)
        runner2 = Runner("Ник", 3)
        tournament = Tournament(90, runner1, runner2)
        results = tournament.start()
        self.assertTrue(results[1] == runner1)

    @skip_if_frozen
    def test_second_tournament(self):
        runner1 = Runner("Андрей", 9)
        runner2 = Runner("Ник", 3)
        tournament = Tournament(90, runner1, runner2)
        results = tournament.start()
        self.assertTrue(results[1] == runner1)

    @skip_if_frozen
    def test_third_tournament(self):
        runner1 = Runner("Усэйн", 10)
        runner2 = Runner("Андрей", 9)
        runner3 = Runner("Ник", 3)
        tournament = Tournament(90, runner1, runner2, runner3)
        results = tournament.start()
        self.assertTrue(results[1] == runner1)
