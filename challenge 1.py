def lngst_com_subseq(first, last):
    m, n = len(first), len(last)
    dp = [["" for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if first[i-1] == last[j-1]:
                dp[i][j] = dp[i-1][j-1] + first[i-1]
            else:
                dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]

    return dp[m][n]

def spy_code_extraction(message):
    words = message.split()
    first_word = words[0]
    last_word = words[-1]

    # find Longest Com subseq
    lcs = lngst_com_subseq(first_word, last_word)
    
    # delete com from 1st word
    for char in lcs:
        first_word = first_word.replace(char, '', 1)

    return first_word

# Exemple
message = "free free palestine"
output = spy_code_extraction(message)
print("Output:", output)
