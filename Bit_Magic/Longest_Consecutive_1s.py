"""

Question:

Given a number N, Your task is to find the  length of the longest consecutive 1's in its binary representation.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N.

Output:
For each test case in a new line print the length of the longest consecutive 1's in N's binary representation.

Constraints:
1<=T<100
1<=N<=1000

Example:
Input
2
14
222
Output
3 
4


"""

#code

def consec_set(n):
    max_length = 0
    temp = 0
    while n:
        if n & 1:
            temp += 1
            if temp > max_length:
                max_length = temp
        else:
            temp = 0
        n >>= 1
    return max_length
    
T = int(input())
for i in range(T):
    n = int(input())
    print(consec_set(n))
