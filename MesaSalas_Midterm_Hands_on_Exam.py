import random

def generate_question():
    operand1, operand2 = random.randint(1, 99), random.randint(1, 99)
    operation = random.choice(['+', '-', '*', '/'])
    question = f"What is {operand1} {operation} {operand2}?"
    return operand1, operand2, operation, question

def student_answer(operand1, operand2, operation, student_answer):
    result = eval(f"{operand1} {operation} {operand2}")
    return int(result) == student_answer

def main():
    for _ in range(4):
        operand1, operand2, operation, question = generate_question()
        print(question, end=' ')
        user_answer = int(input("Your answer: "))
        correct = student_answer(operand1, operand2, operation, user_answer)
        print(f"{operand1} {operation} {operand2} = {user_answer}")
        print(f"Your answer is {'correct' if correct else 'incorrect'}\n")

if __name__ == "__main__":
    main()


