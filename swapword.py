def swap(string):
    first_char=string[0]
    last_char=string[-1]
    modified_string=last_char+string[1:-1]+first_char
    return modified_string
word=input("enter the word:")
swapped_word=swap(word)
print("swapped word:",swapped_word)
