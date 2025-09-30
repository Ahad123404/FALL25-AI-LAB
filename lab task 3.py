movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

total_budget = 0
for movie, budget in movies:  
    total_budget += budget
average_budget = total_budget / len(movies) 


high_budget_movies = []
for movie, budget in movies:  
    if budget > average_budget:
        high_budget_movies.append(movie)

# Result
print("Average budget of movies:", average_budget)
print("High-budget movies (budget > average):")
for movie in high_budget_movies:
    print(movie)