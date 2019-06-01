def trap(height) -> int:
    total_water = 0
    if (height is None or len(height) == 0):
        return total_water

    left_highest = list()
    left_highest.append(0)

    for i in range(len(height)):
        left_highest.append(max(left_highest[i], height[i]))

    right_highest = 0
    for i in range(len(height)-1, 0, -1):
        right_highest = max(height[i], right_highest)
        if min(left_highest[i], right_highest) > height[i]:
            total_water += min(left_highest[i], right_highest) - height[i]

    return total_water


if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
