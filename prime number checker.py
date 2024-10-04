def sort_list(numbers):
    return sorted(numbers), sorted(numbers, reverse=True)

numbers = [23, 1, 45, 34, 7, 9]
asc, desc = sort_list(numbers)
print(f"Ascending: {asc}")
print(f"Descending: {desc}")
