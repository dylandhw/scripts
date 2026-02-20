# quickly testing something

import random
from collections import Counter

import matplotlib.pyplot as plt

numbers = [random.randint(1, 100) for _ in range(1000)]

counts = Counter(numbers)

x = list(range(1, 101))
y = [counts.get(i, 0) for i in x]

plt.figure()
plt.bar(x, y)
plt.xlabel("number")
plt.ylabel("frequency")
plt.title("frequency of random numbers (1-100)")
plt.show()
