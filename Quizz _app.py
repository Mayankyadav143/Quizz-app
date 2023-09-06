class Question:
    def _init_(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.text)
        for i, choice in enumerate(question.choices, start=1):
            print(f"{i}. {choice}")
        
        user_answer = int(input("Enter the number of your answer: "))
        
        if question.check_answer(user_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, the correct answer was {question.choices[question.correct_answer - 1]}\n")
    
    print(f"You got {score}/{len(questions)} questions correct!")

if _name_ == "_main_":
    # Define your quiz questions here
    q1 = Question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], 3)
    q2 = Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], 2)
    q3 = Question("What is the largest mammal in the world?", ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"], 3)
    
    # Create a list of questions
    questions = [q1, q2, q3]
    
    #