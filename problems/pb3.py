def youngest_student(students):

    # iterate thru dict
    age = 0
    print(age)
    name = ""
    for key, value in students.items():
        # print(key, value)
        # should compare each age, conditional statement
        if value < age:
            age = value
            name = key
    return name
    pass # TODO:


 students = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
 print(youngest_student(students))  # Expected output: "Alice"
