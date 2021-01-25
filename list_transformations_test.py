# Testing file for lists lab
# By: Emma Brown

# =============================================================================
#  More-Than-You-Need-To-Know Lounge
# =============================================================================
# Welcome to the More-Than-You-Need-To-Know Lounge, a chill place for code that
# you don't need to understand.

# Thanks for stopping by, we hope you find something that catches your eye.
# But don't worry if this stuff doesn't make sense yet -- as long as we know
# how to use code, we don't have to understand everything about it.

# Of course, if you really like this place, stay a while. You can ask a
# teacher about it if you're interested.
#
# =============================================================================


from list_transformations import reverse_list, square_list, capitalize_list, sort_list
import sys

type_dict = {"1": [25,10,20,15,5], "2": [24.2,18.9,16.3,12.4,6.7], "3":["hello","banana","office","pie"],"4":"Exit"}

def choose_type():
    print("\nWould you like to test...")
    print("\t 1) Integers")
    print("\t 2) Floats")
    print("\t 3) Strings")
    print("\t 4) Exit")  
    type_input = input("Choose a type: ") 

    while type_input not in type_dict.keys():
        type_input = input("Please select a correct option: ")

    return type_input

def choose_number_test():
    print("\nWhich test would you like to run?")
    print("\t 1) square()")
    print("\t 2) reverse()")
    print("\t 3) sort()")
    print("\t 4) All Tests")
    test_input = input("Choose a test: ")

    while test_input not in type_dict.keys():
        test_input = input("Select a correct options: ")

    return test_input


def choose_string_test():
    print("\nWhich test would you like to run?")
    print("\t 1) capitalize()")
    print("\t 2) reverse()")
    print("\t 3) sort()")
    print("\t 4) All Tests")

    test_input = input("Choose a test: ")

    while test_input not in type_dict.keys():
        test_input = input("Select a correct options: ")

    return test_input

def all_number_tests(a_list):
    print("List squared:", square_list(a_list))
    print("List revered:", reverse_list(a_list))
    print("List sorted:", sort_list(a_list),"\n")

def all_string_tests(a_list):
    print("List capitalized:", capitalize_list(a_list))
    print("List reversed:", reverse_list(a_list))
    print("List sorted:", sort_list(a_list),"\n")

def main():
    print("----List Transformation Test Script----")
    
    type_input = choose_type()


    while type_input != "4":
        type_list = type_dict[type_input]
        if type_input == "1" or type_input == "2": 
            test_input = choose_number_test()
            print("\nInitial List: ", type_list)

            if test_input == "1":
                print("List squared:", square_list(type_list), "\n")
            elif test_input == "2":
                print("List revered:", reverse_list(type_list), "\n")
            elif test_input == "3":
                print("List sorted:", sort_list(type_list), "\n")
            elif test_input == "4":
                all_number_tests(type_list)

            
        elif type_input == "3":
            test_input = choose_string_test()
            print("\nInitial List: ", type_list)

            if test_input == "1":
                print("List capitalized:", capitalize_list(type_list), "\n")
            elif test_input == "2":
                print("List revered:", reverse_list(type_list), "\n")
            elif test_input == "3":
                print("List sorted:", sort_list(type_list), "\n")
            elif test_input == "4":
                all_string_tests(type_list)
        
        print("----List Transformation Test Script----")

        type_input = choose_type()
        


if __name__ == "__main__":
    main()
