'''Question statement: There are n intermediate stations between two places A and B. Find the number of ways in which a train can be made to stop at m of these intermediate stations so that no two stopping stations are consecutive?'''
'''Solved considering this as a combination problem'''
n = int(input())
m = int(input())
result1 = 1 
result2 = 1 
result3 = 1 
for i in range(1,(n-m+2)):
    result1 *= i 
result1 
for j in range(1,m+1):
    result2 *= j 
result2
for k in range(1,(n-(2*m)+2)):
    result3 *= k 
result3
print(result1//(result2*result3))
