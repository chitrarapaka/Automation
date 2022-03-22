"""Q.Write
a
program
that
prompts
the
user
for a string s and a character c, and outputs the string produced from s by capitalizing each occurrence of the character c in s and making all other characters lowercase.
For
example,
if the user inputs "Mississippi" and "s", the program outputs "miSSiSSippi"."""

#########

s = input("Enter the word :- ")
c = input("Enter the character :- ")
str = ""
for i in range(len(s)):
    if s[i] == c:
        str += s[i].upper()
    else:
        str += s[i]
print(str)