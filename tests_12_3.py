import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    # return self.distance

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')


    def test_walk(self):
        runner_1 = Runner('Walya')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = Runner('Rustam')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = Runner('Wikram')
        runner_4 = Runner('Zoya')
        for i in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


runner_test = RunnerTest()
print(runner_test)


import unittest
from unittest import TestCase

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

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


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        return cls.all_results

    is_frozen = True
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)



    def test_1(self):
        self.all_results = Tournament(90, self.runner_1, self.runner_3).start()
        for key, value in self.all_results.items():
            self.all_results[key] = value.name
        key_last = max(self.all_results, key = int)
        self.assertTrue(self.all_results[key_last], 'Ник')

    def test_2(self):
        self.all_results = Tournament(90, self.runner_2, self.runner_3).start()
        for key, value in self.all_results.items():
            self.all_results[key] = value.name
        key_last = max(self.all_results, key = int)
        self.assertTrue(self.all_results[key_last], 'Ник')


    def test_3(self):
        self.all_results = Tournament(90, self.runner_1,self.runner_2, self.runner_3).start()
        for key, value in self.all_results.items():
            self.all_results[key] = value.name
        key_last = max(self.all_results, key = int)
        self.assertTrue(self.all_results[key_last], 'Ник')

    # @classmethod
    def tearDown(self):
        print(self.all_results)
