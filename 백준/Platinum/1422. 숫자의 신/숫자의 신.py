K,N,*G=map(int,open(0).read().split())
print(*sorted(G+[max(G)]*(N-K),key=lambda O:str(O)*9)[::-1],sep='')
