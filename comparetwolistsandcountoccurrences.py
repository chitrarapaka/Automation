def list_to_str(s):
    str1 = ""
    for ele in s:
        str1 = str1 + ele
        return str1

s = ['Geeks', 'For', 'Chitra']
print(list_to_str(s))

##### Count occurrences of each word in a string or list
## Nested for loops

l1 = ["Sri","Vishnu", "Roopaya", "namah", "Shivaya"]
l2 = ['Om', 'namah', 'Shivaya']
for word in l2:
    counter = 0
    for ele in l1 :

          if word == ele :
            counter = counter + 1
    print("number of occurrences of " + word + " is " + str(counter))
    #####The pass Statement for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
### for x in fruits :
    #pass