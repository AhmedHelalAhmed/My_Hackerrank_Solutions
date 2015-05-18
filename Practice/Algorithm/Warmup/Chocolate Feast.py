T = int(input())

for i in range(T):

    N,C,M = map(int,input().split())
    answer = 0
    answer += N//C
    wrap = answer
    while wrap>=M:
        n=wrap//M
        e=wrap%M
        answer+=n
        wrap=n+e
    print(answer)

