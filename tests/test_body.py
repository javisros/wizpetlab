import unittest

from body import (
    attempts_for_probability,
    body_probability,
    cumulative_probability,
    expected_attempts,
    failure_probability,
    first_success_probability,
)


class TestBodyModel(unittest.TestCase):

    def test_equal_wow_factors_give_half_probability(self):
        self.assertAlmostEqual(
            body_probability(5, 5),
            0.5,
        )

    def test_complementary_body_probabilities_sum_to_one(self):
        probability_a = body_probability(3, 8)
        probability_b = body_probability(8, 3)

        self.assertAlmostEqual(
            probability_a + probability_b,
            1.0,
        )

    def test_cumulative_probability(self):
        self.assertAlmostEqual(
            cumulative_probability(0.5, 3),
            0.875,
        )

    def test_failure_probability(self):
        self.assertAlmostEqual(
            failure_probability(0.5, 3),
            0.125,
        )

    def test_success_and_failure_are_complements(self):
        success = cumulative_probability(0.2, 10)
        failure = failure_probability(0.2, 10)

        self.assertAlmostEqual(
            success + failure,
            1.0,
        )

    def test_expected_attempts(self):
        self.assertAlmostEqual(
            expected_attempts(0.25),
            4.0,
        )

    def test_attempts_for_target_probability(self):
        self.assertEqual(
            attempts_for_probability(0.5, 0.9),
            4,
        )

    def test_first_success_probability(self):
        self.assertAlmostEqual(
            first_success_probability(0.5, 3),
            0.125,
        )

    def test_invalid_wow_factor_raises_error(self):
        with self.assertRaises(ValueError):
            body_probability(-1, 5)

    def test_invalid_probability_raises_error(self):
        with self.assertRaises(ValueError):
            expected_attempts(0)


if __name__ == "__main__":
    unittest.main()