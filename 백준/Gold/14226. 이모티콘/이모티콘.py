import sys
from collections import deque

if __name__ == '__main__':
    S = int(input())

    # dp[i][j] = x : 화면에 있는 이모티콘의 갯수 i개, 클립보드에 있는 이모티콘의 갯수 j개 일때 걸린 시간 x초
    dp = [[-1] * 1001 for _ in range(1001)]
    dp[1][0] = 0
    q = deque([(1, 0)])
    # 각 연산은 1초가 소요
    while q:
        i, j = q.popleft()
        # 화면에 있는 i개의 이모티콘을 클립보드에 붙이는 경우
        if i <= 1000:
            if dp[i][i] == -1:
                dp[i][i] = dp[i][j] + 1
                q.append((i, i))
        # 클립보드에 있는 j개의 이모티콘을 화면에 붙이는 경우
        if i + j <= 1000:
            if dp[i + j][j] == -1:
                dp[i + j][j] = dp[i][j] + 1
                q.append((i + j, j))
        # 화면에서 이모티콘을 1개 삭제하는 경우
        if i - 1 >= 0:
            if dp[i - 1][j] == -1:
                dp[i - 1][j] = dp[i][j] + 1
                q.append((i - 1, j))
        if i == S: break
    ans = sys.maxsize
    for y in dp[S]:
        if y != -1: ans = min(ans, y)
    print(ans)