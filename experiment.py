from math import ceil
from statistics import mean, median

from body import (
    attempts_for_probability,
    body_probability,
    expected_attempts,
)
from monte_carlo import (
    monte_carlo_standard_error,
    simulate_hatches,
    simulate_players,
)


WOW_A = 10
WOW_B = 0
SEED = 42


def empirical_percentile(values: list[int], probability: float) -> int:
    """Return a simple nearest-rank empirical percentile."""

    sorted_values = sorted(values)

    index = ceil(probability * len(sorted_values)) - 1

    return sorted_values[index]


def main() -> None:
    p_exact = body_probability(WOW_A, WOW_B)

    print("Wizard101 Pet Lab")
    print("==================")
    print()

    print("Analytical model")
    print("----------------")
    print(f"Wow Factor A: {WOW_A}")
    print(f"Wow Factor B: {WOW_B}")
    print(f"Exact probability: {p_exact:.6f}")
    print(f"Exact probability: {p_exact:.2%}")
    print()

    print("Probability targets")
    print("-------------------")

    for target in [0.50, 0.90, 0.95, 0.99]:
        attempts = attempts_for_probability(
            p_exact,
            target,
        )

        print(
            f"{target:.0%} cumulative probability: "
            f"{attempts} hatches"
        )

    print()
    print(f"Expected attempts: {expected_attempts(p_exact):.2f}")
    print()

    print("Monte Carlo convergence")
    print("-----------------------")

    for n_hatches in [100, 1_000, 10_000, 100_000]:
        estimate = simulate_hatches(
            p_exact,
            n_hatches,
            seed=SEED,
        )

        observed_error = abs(estimate - p_exact)

        standard_error = monte_carlo_standard_error(
            p_exact,
            n_hatches,
        )

        print(
            f"N={n_hatches:>6} | "
            f"estimate={estimate:.6f} | "
            f"error={observed_error:.6f} | "
            f"SE={standard_error:.6f}"
        )

    print()

    n_players = 100_000

    results = simulate_players(
        p_exact,
        n_players,
        seed=SEED,
    )

    print("Simulated players")
    print("-----------------")
    print(f"Players: {n_players}")
    print(f"Mean attempts: {mean(results):.3f}")
    print(f"Median attempts: {median(results):.1f}")
    print(f"Minimum attempts: {min(results)}")
    print(f"Maximum attempts: {max(results)}")
    print()

    print("Empirical percentiles")
    print("---------------------")

    for percentile in [0.50, 0.90, 0.95, 0.99]:
        value = empirical_percentile(
            results,
            percentile,
        )

        print(
            f"{percentile:.0%}: "
            f"{value} hatches"
        )


if __name__ == "__main__":
    main()