def solution(n):
    answer = 0
    dp = [0 for _ in range(n)]
    """
    1=>1 2=>2 3=>3 4=>5 5=>8
    """
    dp[0]=1
    dp[1]=2
    for i in range(2, len(dp)):
        dp[i] =(dp[i-2]+dp[i-1])%1000000007
    return dp[n-1]