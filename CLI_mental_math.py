#File name: mental_math_game
import random
import time

class MentalMathGame:
    
    def __init__(self) -> None:
        self.game_mode: str = ""
        self.operation: str = ""
        self.difficulty: str = ""
        self.question_amount: int = 0
        self.correct_answer_count: int = 0
        
    
    def timer(self) -> None:
        for i in range(3, 0, -1):
            print(i, end="...")
            time.sleep(1)
        print("Go!", end="\n\n")

    
    def count_score(self) -> None:  
        score: float = 100 * (self.correct_answer_count / self.question_amount) #This function used to count how many correct answer that
        print(F"Game Summary\n"                                                 #you had guess and give you the total score with it
              F"Total of Question Answered: {self.question_amount}\n"
              F"Correct Answer Count: {self.correct_answer_count} \n"
              F"Incorrect Answer Count: {self.question_amount - self.correct_answer_count}\n"
              F"Your Score: {round(score, 2)}")
        
    def determine_game_mode(self) -> None:
        game_mode_options: tuple[*str] = ("Type The Answer Mode", "Abcd Mode", "Incorrect Limit Mode")
        
        while True:
            the_game_mode_i_chose: str = input("What is the game mode?\n"
                                                "1. Type The Answer Mode\n"
                                                "2. Abcd Mode\n"
                                                "3. Incorrect Limit Mode\n"
                                                "Select by typing it or the number!\n>").title()
                                            
            if the_game_mode_i_chose in ("1", "Type The Answer Mode", "Type The Answer"):
                self.game_mode = game_mode_options[0]
                return
            
            elif the_game_mode_i_chose in ("2", "Abcd Mode", "Abcd"):
                self.game_mode = game_mode_options[1]
                return
            
            elif the_game_mode_i_chose in ("3", "Incorrect Limit Mode", "Incorrect Limit"):
                self.game_mode = game_mode_options[2]
                return
        
            else:
                print("Your choice of game mode is not recognized. Please to try again!\n")

    
    
    def determine_the_operation(self) -> None:
        operator_options: tuple[*str] = ("+", "-", "*", "/")
        
        while True:
            the_operation_i_chose: str = input("What is the operation?\n"
                                                "1. Addition\n"
                                                "2. Subtraction\n"
                                                "3. Multiplication\n"
                                                "4. Division\n"
                                                "Select by typing it or the number!\n>").title()
                                                
            if the_operation_i_chose in ("1", "Addition"):
                self.operation = operator_options[0]
                return
            
            elif the_operation_i_chose in ("2", "Subtraction"):
                self.operation = operator_options[1]
                return
            
            elif the_operation_i_chose in ("3", "Multiplication"):
                self.operation = operator_options[2]
                return
            
            elif the_operation_i_chose in ("4", "Division"):
                self.operation = operator_options[3]
                return
            
            else:
                print("Your choice of operations is not recognized. Please to try again!\n")
    
    
    def determine_the_difficulty(self) -> str:
        difficulty_options: tuple[*str] = ("Easy", "Medium", "Hard", "Challenging")

        while True:
            the_difficulty_i_chose: str = input("What is the difficulty?\n"
                                                "1. Easy\n"
                                                "2. Medium\n"
                                                "3. Hard\n"
                                                "4. Challenging\n"
                                                "Select by typing it or the number!\n>").title()
                                                
            if the_difficulty_i_chose in ("1", "Easy"):
                self.difficulty = difficulty_options[0]
                return
            
            elif the_difficulty_i_chose in ("2", "Medium"):
                self.difficulty = difficulty_options[1]
                return
            
            elif the_difficulty_i_chose in ("3", "Hard"):
                self.difficulty = difficulty_options[2]
                return
            
            elif the_difficulty_i_chose in ("4", "Challenging"):
                self.difficulty = difficulty_options[3]
                return
            
            else:
                print("Your choice of difficulty is not recognized. Please to try again!\n")
     

    def determine_how_many_question(self) -> None:

        while True:
            try:
                the_question_amount_i_chose: int = int(input("How many question that you like? (Maxs 1000 questions)\n>"))
                
                if 1 <= the_question_amount_i_chose <= 1000:
                    self.question_amount = the_question_amount_i_chose
                    return
                
                elif the_question_amount_i_chose < 1:
                    print("The question amount shouldn't less than 1")
                    
                elif the_question_amount_i_chose > 1000:
                    print("The question amount shouldn't more than 1000")
            
            except ValueError:
                print(F"Your choice of question amount is not recognized. Please to try again!\n")


    def generate_question_if_addition(self) -> None:
        
        positive_number_range: int = 0
        negative_number_range: int = 0
        
        match self.difficulty:
            case "Easy":
                positive_number_range = 10
                negative_number_range = -10
                
            case "Medium":
                positive_number_range = 50
                negative_number_range = -50
                
            case "Hard":
                positive_number_range = 500
                negative_number_range = -500
                
            case "Challenging":
                positive_number_range = 1000
                negative_number_range = -1000
            
        for i in range(1, self.question_amount + 1):
            
            number1: int = random.randint(negative_number_range, positive_number_range)    
            number2: int = random.randint(negative_number_range, positive_number_range)
            
            while True:
                try:
                    your_answer: int = int(input(F"{i}. {number1} + {number2} = ?\n>"))
                    real_answer: int = number1 + number2
                    
                    if your_answer == real_answer:
                        print(F"Correct!. The answer is {real_answer}")
                        self.correct_answer_count += 1
                        break
                    
                    elif your_answer != real_answer:
                        print(F"Incorrect!. The answer is {real_answer}")
                        break
                
                except ValueError:
                    print("Your answer is a none number type. Please insert number only and try again!\n")


    def generate_question_if_subtraction(self) -> None:
        
        positive_number_range: int = 0
        negative_number_range: int = 0
        
        match self.difficulty:
            case "Easy":
                positive_number_range = 10
                negative_number_range = -10
                
            case "Medium":
                positive_number_range = 50
                negative_number_range = -50
                
            case "Hard":
                positive_number_range = 250
                negative_number_range = -250
                
            case "Challenging":
                positive_number_range = 500
                negative_number_range = -500
            
        for i in range(1, self.question_amount + 1):
            
            number1: int = random.randint(negative_number_range, positive_number_range)    
            number2: int = random.randint(negative_number_range, positive_number_range)
            
            while True:
                try:
                    your_answer: int = int(input(F"{i}. {number1} - {number2} = ?\n>"))
                    real_answer: int = number1 - number2
                    
                    if your_answer == real_answer:
                        print(F"Correct!. The answer is {real_answer}")
                        self.correct_answer_count += 1 
                        break
                    
                    elif your_answer != real_answer:
                        print(F"Incorrect!. The answer is {real_answer}")
                        break
                
                except ValueError:
                    print("Your answer is a none number type. Please insert number only and try again!\n")


    def generate_question_if_multiplication(self) -> None:
        
        positive_number_range: int = 0
        negative_number_range: int = 0
        
        match self.difficulty:
            case "Easy":
                positive_number_range = 5
                negative_number_range = -5
                
            case "Medium":
                positive_number_range = 10
                negative_number_range = -10
                
            case "Hard":
                positive_number_range = 50
                negative_number_range = -50
                
            case "Challenging":
                positive_number_range = 100
                negative_number_range = -100
            
        for i in range(1, self.question_amount + 1):
            
            number1: int = random.randint(negative_number_range, positive_number_range)    
            number2: int = random.randint(negative_number_range, positive_number_range)
            
            while True:
                try:
                    your_answer: int = int(input(F"{i}. {number1} X {number2} = ?\n>"))
                    real_answer: int = number1 * number2
                    
                    if your_answer == real_answer:
                        print(F"Correct!. The answer is {real_answer}")
                        self.correct_answer_count += 1
                        break
                    
                    elif your_answer != real_answer:
                        print(F"Incorrect!. The answer is {real_answer}")
                        break
                
                except ValueError:
                    print("Your answer is a none number type. Please insert number only and try again!\n")
        
        
    def generate_question_if_division(self) -> None:
        
        positive_number_range: int = 0
        negative_number_range: int = 0
        
        match self.difficulty:
            case "Easy":
                positive_number_range = 10
                negative_number_range = -10
                
            case "Medium":
                positive_number_range = 50
                negative_number_range = -50
                
            case "Hard":
                positive_number_range = 500
                negative_number_range = -500
                
            case "Challenging":
                positive_number_range = 1000
                negative_number_range = -1000
            
        for i in range(1, self.question_amount + 1):
            
            number1: int = random.randint(negative_number_range, positive_number_range) + 1 #For both num1 & num2, adding "+ 1" is to prevent the program to pick "0"
            number2: int = random.randint(negative_number_range, positive_number_range) + 1
            num1_and_num2_remainder: int = number1 % number2  
            number1 -= num1_and_num2_remainder
            
            while True:
                try:
                    your_answer: int = int(input(F"{i}. {number1} / {number2} = ?\n>"))
                    real_answer: int = number1 // number2
                    
                    if your_answer == real_answer:
                        print(F"Correct!. The answer is {real_answer}")
                        self.correct_answer_count += 1
                        break
                    
                    elif your_answer != real_answer:
                        print(F"Incorrect!. The answer is {real_answer}")
                        break
                
                except ValueError:
                    print("Your answer is a none number type. Please insert number only and try again!\n")
    
    
    def start_practicing(self) -> None:
        match self.operation:
            case "+":
                self.generate_question_if_addition()
            
            case "-":
                self.generate_question_if_subtraction()
            
            case "*":
                self.generate_question_if_multiplication()
            
            case "/":
                self.generate_question_if_division()
