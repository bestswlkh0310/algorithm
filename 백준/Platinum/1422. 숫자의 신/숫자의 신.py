from functools import cmp_to_key as C
T,S,I,D=int,str,input,sorted
K,N=map(T,I().split())
G=[*D([T(I()) for _ in' '*K],key=lambda x:(len(S(x)),x))]
print(''.join([*map(S,D(G+[G[-1]]*(N-K),key=C(lambda O,P:T(S(P)+S(O))-T(S(O)+S(P)))))]))
