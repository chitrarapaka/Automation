###***** VERY IMPORTANT *******########
#####@@@@@@@@@@@@@@@@@@@@ COUNT THE OCCURRENCES OF WORDS IN STR1 and printing the occurrences in dictionary ##############@@@@@@@@@@@@@

str1 = "mango banana apple pear banana grapes strawberry apple pear mango banana kiwi apple mango strawberry"
S = str1.split(" ") # Remove the leading spaces and splitting into words
# Create an empty dictionary
d = dict()

    # Iterate over each word in line
for word in S:
    #print(d)
    #print(word)
    # Check if the word is already in dictionary
    if word in d:
        # Increment count of word by 1
        d[word] = d[word] + 1
        #print(d[word])

    else:
        # Add the word to dictionary with count 1
        d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])
for key in d.keys():
    print(key, ":", d[key])


###########@@@@@@@@@@@@

