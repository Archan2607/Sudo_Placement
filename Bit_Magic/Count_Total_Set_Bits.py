"""

Question:

Find the sum of all bits from numbers 1 to N.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N.

Output:

Print the sum of all bits.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 1000

Example:

Input:
2
4
17

Output:
5
35

Explanation:
An easy way to look at it is to consider the number, n = 4:
0 0 0 = 0
0 0 1 = 1
0 1 0 = 1
0 1 1 = 2
1 0 0 = 1
Therefore , the total number of bits is 5
"""

#code
t=int(input())
while t!=0:
    n = int(input())
    total = 0
    get_bin = lambda x, n: format(x, 'b').zfill(n)
    for index in range (0, n+1):
        binary = get_bin(index, 64)
        blist = list(binary)
        length = len (blist)
        count = 0
        i = 0
        while (i != length):
            if int(blist[i]) == 1:
                count=count+1
            i=i+1
        total=total+count
    print(total)
    t = t - 1
