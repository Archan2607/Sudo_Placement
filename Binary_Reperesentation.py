"""

Reference Question Link : - https://practice.geeksforgeeks.org/problems/binary-representation/0

"""


t=int(input())

for _ in range(t):
    print('{0:014b}'.format(int(input())),end='\n')
