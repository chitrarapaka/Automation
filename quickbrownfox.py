###### Count number of alphabets ,check if all the alphabets exist in given string


def count_of_alphabets(str):
    d = {}
    for i in range(0,len(str)):
        letter = str[i].lower()
        if letter in d:
            d[letter] = d[letter]+1

        else:
            d[letter]=1

    print(d.items())
    return


##str = "The quick brown fox jumps over the lazy dog"
#count_of_alphabets(str)
#############################################################
def alphacheck(str):
    l1 = []
    ### For loop below is to form a list with only alphabets
    for i in range(0,len(str)):

        if str[i].isalpha(): ### ignore anything other than alphabet-ex-123
            l1.append( str[i].lower()) ####

    l1 = list(set(l1)) #### Removes duplicates
    #l1.sort()
    if len(l1)== 26: # After removing duplicates,if len is 26,it will be a Panagram
        print("Yes,{} is a Panagram".format(str))
    else:
        return False


str = "The quick123, brown fox jumps over the lazy dog" ### This is a Panagram
##str = "aabcdd"
print(alphacheck(str))





