# find out if string is a palindrome

def find_pal (S):
    S.upper()
    #print(S)
    j = len(S)
    for i in range(0, int(j/2)):
        print('i value is',i)
        print('j value is', j)
        if S[i]!=S[j-i-1]:
            return False

    return True


S = 'amma'
print(find_pal(S))
