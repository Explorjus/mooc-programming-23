# Write your solution here
word = input("Please tyoe in a string:")


if word[1] == word[-2]:
    print(f"The second and the second to last characters are {word[1]}")

elif word[1] != word[-2]:
    print("The second and the second to last characters are different")