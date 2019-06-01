def robot_in_a_grid(obstacleGrid):
    if not len(obstacleGrid) or not len(obstacleGrid[0]):
        return 0

    columns = len(obstacleGrid[0]) - 1
    rows = len(obstacleGrid) - 1
    path = list()
    failed_points = set()

    if get_path(obstacleGrid, rows, columns, path, failed_points):
        return path
    return None


def get_path(obstacleGrid, row, column, path, failed_points):
    if column < 0 or row < 0 or obstacleGrid[row][column] == 1:
        return False

    if (row, column) in failed_points:
        return False

    is_at_origin = (row == 0) and (column == 0)
    if is_at_origin or get_path(obstacleGrid, row - 1, column,
                                path, failed_points)\
            or get_path(obstacleGrid, row, column - 1, path, failed_points):
        path.append((row, column))
        return True
    failed_points.add((row, column))
    return False


if __name__ == "__main__":
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(robot_in_a_grid(obstacleGrid))
