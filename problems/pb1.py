def replace_spaces(sentence, "_" ):
    sentence = "Test  This is a test   Testing "
    # change the string to a list, so it can mutate
    new_list = list(sentence, "_")
    #  iterate thru the list
    for index in range(len(new_list)):
        print(index)
        # create a conditional statement, if the element at the index is a space then reassign it to a _
        if new_list[index] == " ":
            new_list[index] = "_"
            # i must join it back
    print("".join(new_list))

replace_spaces(sentence, "_")
        # make conditional statement


    
    
    
    
    
    
    
    
    
    
    #pass #TODO:



# sentence = "Test  This is a test   Testing "
# sentence2 = pb1.replace_spaces(sentence, "_")
# print(sentence2) # -> Test__This_is_a_test__Testing_