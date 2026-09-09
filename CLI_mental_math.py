#CLI Mental Math Game (Function)

import random
import time

def timer() -> None:
    
    for i in range(3, 0, -1):
        print(i, end="...")
        time.sleep(1)
    print("Go!", end="\n\n")
    
    
def determine_the_difficulty() -> str:
    difficulty_options: tuple[*str] = ("Easy", "Medium", "Hard", "Challenging")
    
    while True:
        the_difficulty_i_chose: str = input("What is the difficulty?\n"
                                            "1. Easy\n"
                                            "2. Medium\n"
                                            "3. Hard\n"
                                            "4. Challenging\n"
                                            "Select by typing it or the number!\n>").title()
                                            
        if the_difficulty_i_chose in ("1", "Easy"):
            return difficulty_options[0]
        
        elif the_difficulty_i_chose in ("2", "Medium"):
            return difficulty_options[1]
        
        elif the_difficulty_i_chose in ("3", "Hard"):
            return difficulty_options[2]
        
        elif the_difficulty_i_chose in ("4", "Challenging"):
            return difficulty_options[3]
        
        else:
            print("Your choice of difficulty is not recognized. Please to try again!\n")
    

def determine_the_operation() -> str:
    operator_options: tuple[*str] = ("+", "-", "*", "/")
    
    while True:
        the_operation_i_chose: str = input("What is the operation?\n"
                                            "1. Addition\n"
                                            "2. Subtraction\n"
                                            "3. Multiplication\n"
                                            "4. Division\n"
                                            "Select by typing it or the number!\n>").title()
                                            
        if the_operation_i_chose in ("1", "Addition"):
            return operator_options[0]
        
        elif the_operation_i_chose in ("2", "Subtraction"):
            return operator_options[1]
        
        elif the_operation_i_chose in ("3", "Multiplication"):
            return operator_options[2]
        
        elif the_operation_i_chose in ("4", "Division"):
            return operator_options[3]
        
        else:
            print("Your choice of operations is not recognized. Please to try again!\n")
    

def determine_how_many_question() -> int:

    while True:
        try:
            the_question_amount_i_chose: int = int(input("How many question that you like? (Maxs 1000 questions)\n>"))
            
            if 1 <= the_question_amount_i_chose <= 1000:
                return the_question_amount_i_chose
            
            elif the_question_amount_i_chose < 1:
                print("The question amount shouldn't less than 1")
                
            elif the_question_amount_i_chose > 1000:
                print("The question amount shouldn't more than 1000")
        
        except ValueError:
            print(F"Your choice of question amount is not recognized. Please to try again!\n")


def count_score(question_amount: int, total_of_correct_answer: int) -> None:
    
    score: float = 100 * (total_of_correct_answer / question_amount)
    print(F"Game Summary\n"
          F"Total of Question Answered: {question_amount}\n"
          F"Correct Answer Count: {total_of_correct_answer} \n"
          F"Incorrect Answer Count: {question_amount - total_of_correct_answer} \n"
          F"Your Score: {round(score, 2)}")
          

def generate_question_if_addition(question_amount: int, difficulty: str) -> None:
    
    positive_number_range: int = 0
    negative_number_range: int = 0
    correct_answer_count: int = 0
    
    match difficulty:
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
        
    for i in range(1, question_amount + 1):
        
        number1: int = random.randint(negative_number_range, positive_number_range)    
        number2: int = random.randint(negative_number_range, positive_number_range)
        
        while True:
            try:
                your_answer: int = int(input(F"{i}. {number1} + {number2} = ?\n>"))
                real_answer: int = number1 + number2
                
                if your_answer == real_answer:
                    print(F"Correct!. The answer is {real_answer}")
                    correct_answer_count += 1
                    break
                
                elif your_answer != real_answer:
                    print(F"Incorrect!. The answer is {real_answer}")
                    break
            
            except ValueError:
                print("Your answer is a none number type. Please insert number only and try again!\n")
    
    count_score(question_amount, correct_answer_count)


def generate_question_if_subtraction(question_amount: int, difficulty: str) -> None:
    
    positive_number_range: int = 0
    negative_number_range: int = 0
    correct_answer_count: int = 0
    
    match difficulty:
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
        
    for i in range(1, question_amount + 1):
        
        number1: int = random.randint(negative_number_range, positive_number_range)    
        number2: int = random.randint(negative_number_range, positive_number_range)
        
        while True:
            try:
                your_answer: int = int(input(F"{i}. {number1} - {number2} = ?\n>"))
                real_answer: int = number1 - number2
                
                if your_answer == real_answer:
                    print(F"Correct!. The answer is {real_answer}")
                    correct_answer_count += 1
                    break
                
                elif your_answer != real_answer:
                    print(F"Incorrect!. The answer is {real_answer}")
                    break
            
            except ValueError:
                print("Your answer is a none number type. Please insert number only and try again!\n")
    
    count_score(question_amount, correct_answer_count)


def generate_question_if_multiplication(question_amount: int, difficulty: str) -> None:
    
    positive_number_range: int = 0
    negative_number_range: int = 0
    correct_answer_count: int = 0
    
    match difficulty:
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
        
    for i in range(1, question_amount + 1):
        
        number1: int = random.randint(negative_number_range, positive_number_range)    
        number2: int = random.randint(negative_number_range, positive_number_range)
        
        while True:
            try:
                your_answer: int = int(input(F"{i}. {number1} X {number2} = ?\n>"))
                real_answer: int = number1 * number2
                
                if your_answer == real_answer:
                    print(F"Correct!. The answer is {real_answer}")
                    correct_answer_count += 1
                    break
                
                elif your_answer != real_answer:
                    print(F"Incorrect!. The answer is {real_answer}")
                    break
            
            except ValueError:
                print("Your answer is a none number type. Please insert number only and try again!\n")
    
    count_score(question_amount, correct_answer_count)


def generate_question_if_division(question_amount: int, difficulty: str) -> None:
    
    positive_number_range: int = 0
    negative_number_range: int = 0
    correct_answer_count: int = 0
    
    
    match difficulty:
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
        
    for i in range(1, question_amount + 1):
        
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
                    correct_answer_count += 1
                    break
                
                elif your_answer != real_answer:
                    print(F"Incorrect!. The answer is {real_answer}")
                    break
            
            except ValueError:
                print("Your answer is a none number type. Please insert number only and try again!\n")
    
    count_score(question_amount, correct_answer_count)


def start_practicing( operation: str, question_amount: int, difficulty: str) -> None:
    match operation:
        case "+":
            generate_question_if_addition(question_amount, difficulty)
        
        case "-":
            generate_question_if_subtraction(question_amount, difficulty)
        
        case "*":
            generate_question_if_multiplication(question_amount, difficulty)
        
        case "/":
            generate_question_if_division(question_amount, difficulty)
