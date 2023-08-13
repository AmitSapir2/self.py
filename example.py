def check_valid_letter(low_case_letter, old_letters_guessed): 
    """
    this function checks the validity of the letter_guessed and previews guseed letters-old_letters_guessed
    :params letter_gussed:current input letter, old_letters_guessed:old inputs
    :type string, list
    :return validity of the input and if the the user guessed the letter already
    :rtype bool
    """
    if not low_case_letter.isalpha() or len(low_case_letter)>1 or low_case_letter in old_letters_guessed:
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    letter_for_check=letter_guessed.lower()
    if check_valid_letter(letter_for_check, old_letters_guessed):
        old_letters_guessed.append(letter_for_check)
        return True
    else:
        print("X")
        list_as_string=''.join(sorted(old_letters_guessed)) #converts list to strings
        lower_case_string=list_as_string.lower()            #converts string to all lower case
        sorted_string="->".join(sorted(lower_case_string))  #adds -> to the string
        print(sorted_string)
        return False

def main():
    letter=input ("write a letter: \n")
    print(try_update_letter_guessed(letter,old_letters))
    farwell=input("press any key to finish")

if __name__ == "__main__":
    main()