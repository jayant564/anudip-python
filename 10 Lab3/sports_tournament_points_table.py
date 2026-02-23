points = [25, -5, 40, 30, 10, -2]

# Replace negative with 0
points = [p if p >= 0 else 0 for p in points]

# Sort leaderboard
points.sort(reverse=True)

winner = points[0]
runner_up = points[1] if len(points) > 1 else None

print("Leaderboard:", points)
print("Winner points:", winner)
print("Runner-up points:", runner_up)