"""

Question:

In a party everyone is in couple except one. People who are in couple have same numbers. Find out the person who is not in couple.

Input:
The first line contains an integer 'T' denoting the total number of test cases. In each test cases, the first line contains an integer 'N' denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array. (N is always odd)


Output:
In each seperate line print number of the person not in couple.


Constraints:
1<=T<=30
1<=N<=500
1<=A[i]<=500
N%2==1


Example:
Input:
1
5
1 2 3 2 1

Output:
3


"""

t= int(input())
for a in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    s = set()
    for i in range(n):
        if(arr[i] in s):
            s.remove(arr[i])
        else:
            s.add(arr[i])
    temp = s.pop()
    print(temp)


