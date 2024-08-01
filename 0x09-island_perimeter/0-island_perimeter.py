#!/usr/bin/python3
"""Island perimeter - Dfs approach"""


def island_perimeter(grid: [[int]]) -> int:
    """

    :param grid: 2-D array grid for Dfs 1s land 0 water
    :return: perimter of 1s (the island)
    """
    if not grid or not grid[0]:
        return 0

    visited = set()

    def dfs(i, j):
        if i >= len(grid) or j >= len(grid[0]) or i < 0 \
                or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0
        visited.add((i, j))
        perim = dfs(i, j + 1)
        perim += dfs(i, j - 1)
        perim += dfs(i + 1, j)
        perim += dfs(i - 1, j)
        return perim
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
    return 0 # in case of all water