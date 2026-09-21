#CLI Mental Math Game (Main)

from mental_math_game import MentalMathGame

def main() -> None:
    
    print("Let's Practice your math skill\n"
          "How to play? just type the related answer to the question:)")

    is_playing: bool = True
    
    while is_playing:
        
        game: MentalMathGame = MentalMathGame()
        game.determine_the_operation() 
        game.determine_the_difficulty()
        game.determine_how_many_question()
        game.timer()
        game.start_practicing()
        game.count_score()
        
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
