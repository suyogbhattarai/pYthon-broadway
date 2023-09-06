# Create a dictionary student with keys id, name, age, department. Take a input from
# the user, which info (id, name, age or department) he wants to access and print the result.
# Handle the possible exceptions.

try:
    student={"id":2,"name":"suyog","age":20,"department":"science"}
    key=input("which key you want to access?")
    a=student[key]

except (KeyError):
    print("Please enter the correct key")
else:
    print(f"The {key} of the student is {a} ")
