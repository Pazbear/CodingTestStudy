def solution(n, money):
    dp = [0 for _ in range(n+1)]
    dp[0]=1
    for m in money:
        for i in range(1,n+1):
            if i>=m:
                dp[i]=(dp[i]+dp[i-m])%1000000007
    return dp[n]