ratings = [5, 4, 6, 3, 2, 0, 5, 4, 1]

# Remove invalid (keep 1 to 5)
ratings = [r for r in ratings if 1 <= r <= 5]

avg_rating = sum(ratings) / len(ratings)
five_star_count = ratings.count(5)

ratings.sort()

print("Valid ratings:", ratings)
print("Average rating:", avg_rating)
print("5-star count:", five_star_count)
print("Sorted ratings:", ratings)