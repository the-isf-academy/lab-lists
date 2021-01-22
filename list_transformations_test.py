from list_transformations import reverse_list, square_list, capitalize_list, sort_list

numbers = [25,10,20,15,5]
lowercase_words = ["hello","banana","office","pie"]

def main():
    print("--Number List Transformations---")
    print("Initial Number List:",numbers)
    print("Numbers revered:", reverse_list(numbers))
    print("Numbers sorted:", sort_list(numbers))
    print("Numbers squared:", square_list(numbers),"\n")
 
    print("--Word List Transformations---")
    print("Inital Word list:",lowercase_words)
    print("Words reversed:", reverse_list(lowercase_words))
    print("Words sorted:", sort_list(lowercase_words))
    print("Words capitalized:", capitalize_list(lowercase_words))


if __name__ == "__main__":
    main()
