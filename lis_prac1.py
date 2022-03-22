#def list_to_str(s):
 #   str1 = ""

  #  for ele in s:
    #    str1 = str1 + ele
   #     return str1

#s = ['Geeks', 'For', 'Geeks']
 #print(list_to_str(s))

#reversing a list
def list_rev(l1):

    l2 = l1.reverse()
    l2 = l1

    print(l2)


list_rev(['Om','namah','shivaya'])

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




