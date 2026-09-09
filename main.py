#CLI Mental Math Game (Main)

from CLI_mental_math import *

def main() -> None:
    
    print("Let's Practice your math skill\n"
              "How to play? just type the related answer to the question:)")

    is_playing: bool = True
    
    while is_playing:
        
        choosen_operation: str = determine_the_operation() 
        choosen_difficulty: str = determine_the_difficulty()
        choosen_amount_of_question: int = determine_how_many_question()
        timer()
        start_practicing(choosen_operation, choosen_amount_of_question, choosen_difficulty)
        
        while True:
            practice_again: str = input("Would you like to practice again? (Yes/No)\n>").title()
            
            if practice_again in ("Yes", "Y"):
                print("Let's go practicing again!")
                break
            
            elif practice_again in ("No", "N"):
                print("See you and have a nice day!")
                is_playing = False
                break
            
            else:
                print("Your choice of practicing again is not recognized. Please to try again!\n")

if __name__ == "__main__":
    main()
