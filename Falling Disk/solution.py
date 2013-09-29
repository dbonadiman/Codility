def solution(A,B):
    M = len(B)
    N = len(A)
    for i in range(1,len(A)):
        A[i] = min(A[i-1],A[i])
    i = 0
    count = 0
    while i<M and N>0:
        if B[i] <= A[N-1]:
            count += 1
            i+=1
        N-=1
    return count

def main():
    print solution([5,6,4,3,6,2,3],[2,3,5,2,4])


if __name__=="__main__":
    main()


