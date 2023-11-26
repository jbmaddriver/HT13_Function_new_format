def deepest_lake_depth(heights):
    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])
    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])
    lake_depths = [min(left_max[i], right_max[i]) - heights[i] for i in range(n)]
    max_lake_depth = max(lake_depths)
    return max_lake_depth


heights = [1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]
result = deepest_lake_depth(heights)
print("The deepest lake depth is:", result)
