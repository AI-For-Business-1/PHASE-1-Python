
### 1. Count occurrences of letter `"a"` (lowercase only)
lst1 = ["apple", "banana", "Avocado", "grape", "mango"]  # example list

lst2 = list(map(lambda x: x.count("a"), lst1))
print(lst2)
# Output: [1, 3, 1, 1, 1]


### 2. Count occurrences of both `"A"` and `"a"` (case-insensitive)
lst1 = ["apple", "banana", "Avocado", "grape", "mango"]  # example list

lst2 = list(map(lambda x: x.lower().count("a"), lst1))
print(lst2)
# Output: [1, 3, 2, 1, 1]

### 3. Filter the list so that only negative numbers remain
lst1 = [10, -5, 3, -12, 0, 7, -1, 25]  # example list

lst2 = list(filter(lambda x: x < 0, lst1))
print(lst2)
# Output: [-5, -12, -1]

### 4. Add 2000 to the values that are below 8000
lst1 = [5000, 9000, 7500, 12000, 3000, 8500]  # example list

lst2 = list(map(lambda x: x + 2000, filter(lambda x: x < 8000, lst1)))
print(lst2)
# Output: [7000, 9500, 5000]


### 5. Read a sentence and return the length of each word as a list
sentence = 'I am learning Python programming with CSEstack'
words = sentence.split()
lengths = list(map(lambda word: len(word), words))
print(lengths)
# Output: [1, 2, 8, 6, 11, 4, 8]


# **Notes:**
# `map()` applies a function to every item.
# - `filter()` keeps only items that satisfy a condition.
# - `lambda` creates a small anonymous function.
# - Always convert the result of `map`/`filter` to a list with `list(...)` if you want to print or reuse it.