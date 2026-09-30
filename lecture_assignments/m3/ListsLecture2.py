# CPSC223P Lecture
# September 8, 2026
# Topic: Looping through Lists

order_ops_list = ["paranTheses", "expoNents", "multiPlication", "diviSion", "addiTion", "subracTion"]

for word in order_ops_list:
    print(f"This word is: {word}")
    print(f"This word in upper is: {word.upper()}")
    print(f"This word in lower is: {word.lower()}")
    print(f"This word in title is: {word.title()}")
    print(f"The type of word is {type(word)}")
    print("----------------------------------------")


new_string = "This is an example of a title"
print(new_string.title())

primes = [2, 3, 5, 7, 11]
sum = 0
for n in primes:
    print(f"The number is {n}")
    sum += n
    print(f"The current sum is {sum}")

avg = sum/len(primes)
print(avg)

#Range() is its own object, similar but distinct from lists. You can cast it into a list

#Use range to generate numbers based on a pattern (simple range)
numbers = list(range(1, 100))
for n in numbers:
    print(n)

#Use range to generate numbers based on a pattern (just odd numbers)
numbers = range(1, 100, 2)
for n in numbers:
    print(n)
