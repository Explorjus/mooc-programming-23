# Write your solution here
word1 = str(input("Please type in string 1:"))
word2 = str(input("Please type in string 2:"))

length1 = "-"*len(word1)
length2 = "-"*len(word2)

if length1 == length2:
    print("The strings are equally long")


if length1 > length2:
    print(word1 + " is longer" )

if length1 < length2:
    print(word2 + " is longer")
