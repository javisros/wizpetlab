import random
from math import sqrt


def simulate_hatch(
    probability: float,
    rng: random.Random,
) -> bool:
    """Simulate one hatch.

    Returns True for success and False for failure.
    """

    if not 0 <= probability <= 1:
        raise ValueError("probability must be between 0 and 1")

    random_number = rng.random()

    return random_number < probability


def simulate_hatches(
    probability: float,
    n_hatches: int,
    seed: int | None = None,
) -> float:
    """Estimate success probability using repeated simulated hatches."""

    if not 0 <= probability <= 1:
        raise ValueError("probability must be between 0 and 1")

    if n_hatches < 1:
        raise ValueError("n_hatches must be at least 1")

    rng = random.Random(seed)

    successes = 0

    for _ in range(n_hatches):
        if simulate_hatch(probability, rng):
            successes += 1

    return successes / n_hatches


def monte_carlo_standard_error(
    probability: float,
    n_samples: int,
) -> float:
    """Return the theoretical standard error of a Bernoulli estimate."""

    if not 0 <= probability <= 1:
        raise ValueError("probability must be between 0 and 1")

    if n_samples < 1:
        raise ValueError("n_samples must be at least 1")

    return sqrt(
        probability * (1 - probability) / n_samples
    )


def simulate_until_success(
    probability: float,
    rng: random.Random,
) -> int:
    """Simulate hatches until the first success.

    Returns the number of attempts required.
    """

    if not 0 < probability <= 1:
        raise ValueError("probability must be greater than 0 and at most 1")

    attempts = 0

    while True:
        attempts += 1

        if simulate_hatch(probability, rng):
            return attempts


def simulate_players(
    probability: float,
    n_players: int,
    seed: int | None = None,
) -> list[int]:
    """Simulate many players hatching until their first success."""

    if not 0 < probability <= 1:
        raise ValueError("probability must be greater than 0 and at most 1")

    if n_players < 1:
        raise ValueError("n_players must be at least 1")

    rng = random.Random(seed)

    results = []

    for _ in range(n_players):
        attempts = simulate_until_success(probability, rng)
        results.append(attempts)

    return results