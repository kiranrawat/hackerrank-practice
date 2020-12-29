# Enter your code here. Read input from STDIN. Print output to STDOUT
Score1 = [15,12,8,8,7,7,7,6,5,3] 
Score2 = [10,25,17,11,13,17,20,13,9,15]

m1 = (sum(Score1)/len(Score1))
m2 = (sum(Score2)/len(Score1))

Score_1 = [x-m1 for x in Score1]
Score_2 = [x-m2 for x in Score2]

n1 = sum([x*y for x,y in zip(Score_1,Score_2)])

Score1 = sum([(x-m1)**2 for x in Score1])
Score2 = sum([(x-m2)**2 for x in Score2])

n2 = (Score1**(1/2))*(Score2**(1/2))

r = n1/n2

print (round(r,3))