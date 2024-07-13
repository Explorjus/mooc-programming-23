# Write your solution here
limit = int(input("Limit:")) - 1
loops = 0
sum = 0
word = ""

while sum <= limit:
    
    loops += 1
    sum += loops 

    if sum <= limit:

        word += str(f"{loops} + ")

    else:
        word += str(f"{loops}")
    
    
    
    
print(f"The consecutive sum: {word} = {sum}")    