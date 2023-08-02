def get_user_choice():
    while True:
        user_choice = input("Enter your choice (A/B/C/D): ").upper()
        if user_choice in ('A', 'B', 'C', 'D'):
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def run_quiz(questions):
    score = 0

    for question in questions:
        print("\n" + question)
        options = questions[question]
        for option in options:
            print(option)

        user_answer = get_user_choice()

        if user_answer == questions[question][-1]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    return score

def main():
    print("Welcome to the Quiz Application!")

    quiz_questions = {
        "What is the capital of France?": ['A. London', 'B. Paris', 'C. Berlin', 'D. Rome', 'B'],
        "Which planet is known as the 'Red Planet'?": ['A. Venus', 'B. Mars', 'C. Jupiter', 'D. Saturn', 'B'],
        "What is the chemical symbol for water?": ['A. WO', 'B. WA', 'C. HO', 'D. H2O', 'D']
    }

    score = run_quiz(quiz_questions)
    total_questions = len(quiz_questions)

    print("\nQuiz completed!")
    print(f"Your score: {score}/{total_questions}")

if __name__ == "__main__":
    main()
