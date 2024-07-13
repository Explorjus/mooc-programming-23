# Write your solution here


word = input("Please type in a string:")
width = 20 - len(word)
star = "*" * width
print(f"{star}{word}")