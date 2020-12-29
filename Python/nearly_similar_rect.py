sides = [[4,8], [15,30], [25,50]]
n =3

total_sides = len(sides)
count = 0
for row in range (0, 2):
    first_div = sides[row][0] / sides[row+1][0]
    second_div = sides[row][1] / sides[row+1][1]
    third_div = sides[row][1] / sides[row+2][1]
    if first_div == second_div:
        count = count+1
            
        
print(count)