# Q WAP to delete all the occurrences of a character in a given string.

s="All the occurances  of a spsecified  character in a given string"
char=input("Enter the character you want to delete in string above")
result=""
for each in s:
    if each.upper() == char.upper() :
        continue
    result += each


print(result)
