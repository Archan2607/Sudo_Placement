"""

Question Links : - https://practice.geeksforgeeks.org/problems/find-first-set-bit/0


"""

T = int(input())
while(T>0):
    N = int(input())
    b = bin(N)[2:][::-1]
    flag=0
    for e in range(0,len(b)):
        if(b[e]=='1'):
            flag=1
            print(e+1)
            break
    if(flag==0):
        print("0")
    T -= 1
