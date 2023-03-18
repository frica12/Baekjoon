# 1495 - 기타리스트 (DP)

import sys

N, S, M = map(int, sys.stdin.readline().split())

V = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(M+1)]

dp[S] = 1