# Write a Python program that accepts an integer (n) and computes the value
#of n+nn+nnn + …

num=int(input("Enter the number")) #3
if num<10:

    new_num=0
    total=0


    for _ in range(num):
        new_num=new_num*10+num #0*10 + 3 = 3,#3*10+3=33,33*10 + 3=333
        total=(total+new_num )# 3+33+333

    print(total)

else:

     print("It is valid only for single digit number")


