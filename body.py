def body_probability(wow_a: int, wow_b: int) -> float:
    """Return the modeled probability of obtaining pet body A."""

    if not 0 <= wow_a <= 10:
        raise ValueError("wow_a must be between 0 and 10")

    if not 0 <= wow_b <= 10:
        raise ValueError("wow_b must be between 0 and 10")

    weight_a = 11 - wow_a
    weight_b = 11 - wow_b

    total_weight = weight_a + weight_b

    probability_a = weight_a / total_weight

    return probability_a


def cumulative_probability(probability: float, n_hatches: int) -> float:
    """Return the probability of at least one success after n hatches."""

    if not 0 <= probability <= 1:
        raise ValueError("probability must be between 0 and 1")

    if n_hatches < 1:
        raise ValueError("n_hatches must be at least 1")

    return 1 - (1 - probability) ** n_hatches