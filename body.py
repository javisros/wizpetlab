from math import ceil, log


def body_probability(wow_a: int, wow_b: int) -> float:
    """Return the modeled probability of obtaining pet body A."""

    if not 0 <= wow_a <= 10:
        raise ValueError("wow_a must be between 0 and 10")

    if not 0 <= wow_b <= 10:
        raise ValueError("wow_b must be between 0 and 10")

    weight_a = 11 - wow_a
    weight_b = 11 - wow_b

    total_weight = weight_a + weight_b

    return weight_a / total_weight


def cumulative_probability(probability: float, n_hatches: int) -> float:
    """Return the probability of at least one success after n hatches."""

    if not 0 <= probability <= 1:
        raise ValueError("probability must be between 0 and 1")

    if n_hatches < 1:
        raise ValueError("n_hatches must be at least 1")

    return 1 - (1 - probability) ** n_hatches


def failure_probability(probability: float, n_hatches: int) -> float:
    """Return the probability of failing every one of n hatches."""

    if not 0 <= probability <= 1:
        raise ValueError("probability must be between 0 and 1")

    if n_hatches < 1:
        raise ValueError("n_hatches must be at least 1")

    return (1 - probability) ** n_hatches


def expected_attempts(probability: float) -> float:
    """Return the expected number of attempts until the first success."""

    if not 0 < probability <= 1:
        raise ValueError("probability must be greater than 0 and at most 1")

    return 1 / probability


def attempts_for_probability(
    probability: float,
    target_probability: float,
) -> int:
    """Return attempts needed to reach a target cumulative probability."""

    if not 0 < probability <= 1:
        raise ValueError("probability must be greater than 0 and at most 1")

    if not 0 < target_probability < 1:
        raise ValueError("target_probability must be between 0 and 1")

    if probability == 1:
        return 1

    attempts = log(1 - target_probability) / log(1 - probability)

    return ceil(attempts)


def first_success_probability(
    probability: float,
    attempt: int,
) -> float:
    """Return the probability that the first success occurs on a given attempt."""

    if not 0 < probability <= 1:
        raise ValueError("probability must be greater than 0 and at most 1")

    if attempt < 1:
        raise ValueError("attempt must be at least 1")

    return (1 - probability) ** (attempt - 1) * probability