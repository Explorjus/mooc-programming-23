# Write your solution here
while True:
    string = input("Please type in a string: ")
    print(string)
    width = "-"  * len(string)
    print(width)
    szerokosc = len(string)
    
    if szerokosc == 0:
        break
