# Write your solution here
limit = int(input("Limit:")) - 1
loops = 0
sum = 0

while sum <= limit:
    
    loops += 1
    sum += loops 
    
print(sum)