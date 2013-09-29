def solution(H):
    B = []
    tot = 0
    for h in H:
        if B:
            if h<B[-1]:
                while h < B[-1]:
                    B.pop()
                    tot += 1
                    if not B:
                        break
        if not B:
            B.append(h)
        else:
            if h > B[-1]:
                B.append(h)
    return tot+len(B)


if __name__=="__main__":
    print solution([8,8,5,7,9,8,7,4,8])
