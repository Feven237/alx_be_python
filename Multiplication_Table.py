number = int(input("Enter a number to see its multiplication table: "))
multipliers = [1,2,3,4,5,6,7,8,9,10]
for i in multipliers :
    result = number * i
    print(f"{number} * {i} = {result}")