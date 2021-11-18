import os
import unittest

from Utils.Misc import hamming_distance, pattern_to_number, number_to_pattern, d_neighborhood, motif_enumeration, \
    profile_matrix, greedy_motif_search


class TestHammingDistance(unittest.TestCase):
    def test_hamming_distance(self):
        cases = [
            ("ACGT", "ACTT", 1)
        ]

        for i, case in zip(range(len(cases)), cases):
            with self.subTest(i=i):
                self.assertEqual(hamming_distance(case[0], case[1]), case[2])


class TestPatternToNumber(unittest.TestCase):
    def test_pattern_to_number(self):
        cases = [
            ("AA", 0),
            ("AC", 1),
            ("GGGG", 170)
        ]

        for i, case in zip(range(len(cases)), cases):
            with self.subTest(i=i):
                self.assertEqual(pattern_to_number(case[0]), case[1])


class TestNumberToPattern(unittest.TestCase):
    def test_number_to_pattern(self):
        cases = [
            (0, 1, "A"),
            (0, 5, "AAAAA"),
            (2, 3, "AAG")
        ]

        for i, case in zip(range(len(cases)), cases):
            with self.subTest(i=i):
                self.assertEqual(number_to_pattern(case[0], case[1]), case[2])


class TestDNeighborhood(unittest.TestCase):
    def test_d_neighborhood(self):
        cases = [
            ("A", 1, {"A", "C", "G", "T"}),
            ("AA", 2, {'AG', 'GT', 'TT', 'GG', 'AT', 'CT', 'AA', 'AC', 'CG', 'CC'}),
            ("ACT", 1, {'AAT', 'ACC', 'TCT', 'ATT', 'GCT', 'AGT', 'ACG', 'CCT', 'ACA', 'ACT'})
        ]

        for i, case in zip(range(len(cases)), cases):
            with self.subTest(i=i):
                self.assertEqual(d_neighborhood(case[0], case[1]), case[2])


class TestMotifEnumeration(unittest.TestCase):
    def test_motif_enumeration(self):
        cases = [
            (["A", "G", "T"], 1, 1, {'C', 'T', 'A', 'G'}),
            (["AG", "TC", "AT"], 2, 2, {'CG', 'AG', 'AT', 'AA', 'CT', 'TT', 'AC', 'GT', 'CC', 'GG'})
        ]

        for i, case in zip(range(len(cases)), cases):
            with self.subTest(i=i):
                self.assertEqual(motif_enumeration(case[0], case[1], case[2]), case[3])


class TestProfileMatrix(unittest.TestCase):
    def test_profile_matrix(self):
        cases = [
            (["A", "G", "T"], [[1 / 3], [0], [1 / 3], [1 / 3]]),
            (["AG", "TC", "AT"], [[2 / 3, 0], [0.0, 1 / 3], [0.0, 1 / 3], [1 / 3, 1 / 3]])
        ]

        for i, case in zip(range(len(cases)), cases):
            with self.subTest(i=i):
                print(profile_matrix(case[0]))
                self.assertEqual(profile_matrix(case[0]), case[1])


class TestGreedyMotifSearch(unittest.TestCase):
    def test_greedy_motif_search(self):
        for filename in os.listdir(r"GreedyMotifTests"):
            with open(f"GreedyMotifTests/{filename}") as file:
                lines = file.readlines()
                k, t = map(int, lines[0].split())
                dna = [line.strip() for line in lines[1:t+1]]
                result = [line.strip() for line in lines[t+1:]]

            self.assertEqual(result, greedy_motif_search(dna, k, t))
