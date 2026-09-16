import random
import unittest

from monte_carlo import (
    monte_carlo_standard_error,
    simulate_hatch,
    simulate_hatches,
    simulate_players,
    simulate_until_success,
)


class TestMonteCarlo(unittest.TestCase):

    def test_zero_probability_always_fails(self):
        rng = random.Random(42)

        self.assertFalse(
            simulate_hatch(0.0, rng)
        )

    def test_probability_one_always_succeeds(self):
        rng = random.Random(42)

        self.assertTrue(
            simulate_hatch(1.0, rng)
        )

    def test_same_seed_gives_same_result(self):
        estimate_1 = simulate_hatches(
            0.2,
            1_000,
            seed=42,
        )

        estimate_2 = simulate_hatches(
            0.2,
            1_000,
            seed=42,
        )

        self.assertEqual(
            estimate_1,
            estimate_2,
        )

    def test_probability_one_estimate_is_one(self):
        estimate = simulate_hatches(
            1.0,
            100,
            seed=42,
        )

        self.assertEqual(
            estimate,
            1.0,
        )

    def test_standard_error_decreases_with_sample_size(self):
        small_sample_error = monte_carlo_standard_error(
            0.2,
            100,
        )

        large_sample_error = monte_carlo_standard_error(
            0.2,
            10_000,
        )

        self.assertLess(
            large_sample_error,
            small_sample_error,
        )

    def test_hundred_times_more_samples_reduce_se_by_factor_ten(self):
        error_100 = monte_carlo_standard_error(
            0.2,
            100,
        )

        error_10000 = monte_carlo_standard_error(
            0.2,
            10_000,
        )

        self.assertAlmostEqual(
            error_100 / error_10000,
            10.0,
        )

    def test_certain_success_takes_one_attempt(self):
        rng = random.Random(42)

        attempts = simulate_until_success(
            1.0,
            rng,
        )

        self.assertEqual(
            attempts,
            1,
        )

    def test_simulate_players_returns_requested_number(self):
        results = simulate_players(
            0.2,
            100,
            seed=42,
        )

        self.assertEqual(
            len(results),
            100,
        )

    def test_player_attempt_counts_are_positive(self):
        results = simulate_players(
            0.2,
            100,
            seed=42,
        )

        self.assertTrue(
            all(attempt >= 1 for attempt in results)
        )


if __name__ == "__main__":
    unittest.main()