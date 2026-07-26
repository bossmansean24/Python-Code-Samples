# Sean Bennett
# July 26, 2026
# This program greets only the student and instructor by name.

student_name = "Sean Bennett"
instructor_name = "Taghvaei Fatemeh"  

name = input("Enter your name: ").strip()

if name.casefold() == student_name.casefold():
    print(f"Hello, {student_name}!")
elif name.casefold() == instructor_name.casefold():
    print(f"Hello, {instructor_name}!")
else:
    print("Hello!")
