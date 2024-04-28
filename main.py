import sys
import random
import utils as dict
from colorama import init,Fore

#init colorama
init()

def guess (dictionary):
    while dictionary :
        word, definition = dict.get_word(dictionary)
        print("Que significa:", word,"?")
        answer = input()
        
        while answer != definition:
            if answer == "-q":
                print("\n")
                quit()
            else:
                print(Fore.RED + "Respuesta incorrecta. vuelve a intentarlo")
                print(Fore.RESET)
                print("\n")
                print("Que significa:", word,"?")            
                answer = input()
        print(Fore.GREEN + "Correcto.")
        print(Fore.RESET)
        del dictionary[word]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <input file>")
    else:
        file_name = sys.argv[1]
        dictionary = dict.read_file(file_name)
        print(Fore.MAGENTA)
        dict.print_home()
        print(Fore.RESET)
        guess(dictionary)
        print(Fore.GREEN)
        dict.print_success()
        
