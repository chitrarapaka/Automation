#Given a String S, reverse the string without reversing its individual words. Words are separated by dots.
#String Reverse Program
#S = "i.like.this.program.very.much"
#T = S.split(".")
#T.reverse()
#res = "."
#res = res.join(T)
#######################################################################
#sorting elements / numbers in a list
def sort_li(L):
    L.sort()
    print(L)
    print("sorted list is" + " " + str(L)) # while printing,typecasted list to string and concatenated

#### Reversing a list function
def list_rev(l1):

    l2 = l1.reverse()
    l2 = l1

    print(l2)
#########################################



L = ['9','5','0']
#sort_li(L)

list_rev(['Om','namah','shivaya'])







