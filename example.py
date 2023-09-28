def opening_print():
    print("Welcome to the game Hangman ")
    print("""\
     _    _
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |
                        |___/ """)

def user_input():
    file_directory=input ("Please specify a directory for a txt file with words: \n")
    word_index=input ("What is the index of the word from your file?: \n")
    return file_directory, word_index


def choose_word(file_path, index):
    """
    this function checks if the user won
    :params file_path, index: the file path for the txt with optional secret word, the index of the chosen word in the file
    :type string, int
    :return number of different words in the file, thw word corresponding to the index 
    :rtype int, string
    """
    with open(file_path, 'r') as file:
        words = file.read()
    list_of_words = words.split()
    secret_word=list_of_words[(index-1)%len(list_of_words)]
    counter=len(set(list_of_words))
    guess_work=(counter,secret_word)
    return guess_work


def make_underscores(input_word):
    print(len(input_word)*"_ ")

def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {
        0: """
        x-------x
         """,
        1: """
        x-------x
        |
        |
        |
        |
        |""",
        2: """
        x-------x
        |       |
        |       0
        |
        |
        |""",
        3: """
        x-------x
        |       |
        |       0
        |       |
        |
        |""",
        4: """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |""",
        5: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |""",
        6: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |"""
    }
    print(HANGMAN_PHOTOS[num_of_tries])


def make_underscores(input_word):
    print(len(input_word)*"_ ")



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
        print("\n")
        list_as_string=''.join(sorted(old_letters_guessed)) #converts list to strings
        lower_case_string=list_as_string.lower()            #converts string to all lower case
        sorted_string="->".join(sorted(lower_case_string))  #adds -> to the string
        print(sorted_string)
        print("\n")
        return False

def show_hidden_word(secret_word, old_letters_guessed):
    """
    this function checks if the guessed letters by the user match the secret word
    :params secret_word: the word user has to guess, old_letters_guessed: letterg gueested in the past
    :type string, string
    :return string of _ and letters in the correct position 
    :rtype string
    """
    altered_word=["_"] * len(secret_word)
    for i in range(len(secret_word)):
            for j in range(len(old_letters_guessed)):
                if  secret_word[i] == old_letters_guessed[j]:
                    altered_word[i]=old_letters_guessed[j]
    return " ".join(altered_word)



def main():
    win_flag=0
    num_of_tries=0
    MAX_TRIES=6
    old_letters_guessed=[]
    letter_guessed=[]
    file_directory, word_index=user_input()
    secret_word=choose_word(file_directory, word_index)
    print_hangman(0)
    make_underscores(secret_word[1])
    while(win_flag==0 and MAX_TRIES>num_of_tries):
        letter_guessed=input ("Type a letter: \n")
        if try_update_letter_guessed(letter_guessed,old_letters_guessed):
            old_letters_guessed.append(letter_guessed.lower())
            unveiled_secret_word=show_hidden_word(secret_word, letter_guessed)
            print(unveiled_secret_word)
            if unveiled_secret_word==secret_word:
                print("WIN")
                win_flag=1
        else:
            print("your input was incorrect ")
            num_of_tries+=1
            print_hangman(num_of_tries)
            if num_of_tries==6:
                print("LOSE")


if __name__ == "__main__":
    main()