'''
Created on 31 May 2020

@author: czarn
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
for n in a:
    if n%2 == 0:
        b.append(n)
        
print(b)