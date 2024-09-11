S = input()
i = len(S)
n = 0
for k in range(1, i+1):
    S1: str = S[:k - 1] + S[k:i]
    if S1[::-1] == S1:
        print(S1, " -палиндром")
        n += 1
    else:
        print(S1, " - не палиндром")
print(n)
