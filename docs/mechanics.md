# Mechanics

## Pet body return via Wow Factor

**Classification:** COMMUNITY-VALIDATED

**Validity last reviewed:** 2026-09-16

### Scope

Version 0.1 models the normal pet-body return probability using the
community-derived Wow Factor model.

Special cases such as Exclusive, Retired, Unhatchable, or other bodies
with additional game rules are outside the scope of version 0.1.

### Model

For two pet bodies A and B with Wow Factors `w_A` and `w_B`:

P(A) = (11 - w_A) / [(11 - w_A) + (11 - w_B)]

P(B) = (11 - w_B) / [(11 - w_A) + (11 - w_B)]

Under this model, a higher Wow Factor corresponds to a lower probability
of that body being returned.

### Repeated hatches

When calculating probabilities over repeated hatches, version 0.1 assumes
that each hatch is independent and uses the same body-return probability.

**Classification:** SIMULATION ASSUMPTION