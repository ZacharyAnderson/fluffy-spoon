"""
    a child is running up a staircase with n steps and can hope either 1 step,
    2 steps, or 3 steps at a time. Implement a method to count how many
    possible ways the child can run up the stairs.
"""


def triple_step_recursive(steps):
    if steps < 0:
        return 0
    elif steps == 0:
        return 1
    else:
        return triple_step_recursive(steps - 1) + triple_step_recursive(steps - 2)\
            + triple_step_recursive(steps - 3)


def triple_step(steps):
    memo = [-1] * (steps + 1)
    return triple_step_memo(steps, memo)


def triple_step_memo(steps, memo):
    if steps < 0:
        return 0
    elif steps == 0:
        return 1
    elif memo[steps] > -1:
        return memo[steps]
    else:
        memo[steps] = triple_step_memo(steps - 1, memo) + \
            triple_step_memo(steps - 2, memo) + \
            triple_step_memo(steps - 3, memo)
        return memo[steps]


if __name__ == "__main__":
    print(triple_step_recursive(4))
    print(triple_step(4))
