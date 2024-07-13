# Write your solution here
width = int(input("Width:"))
rows = int(input("Height:"))

final_width = "#" * width

while rows > 0:
    rows -= 1
    
    print(final_width)