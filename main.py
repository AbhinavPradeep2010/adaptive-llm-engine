from user_model import create_user_profile, update_confidence
from intent import detect_intent
from difficulty import estimate_difficulty
from strategy import select_strategy

user = create_user_profile()

while True:
    question = input("\nAsk a question (or type 'exit' to quit): ")

    if question.lower().strip() == 'exit':
        break

    intent = detect_intent(question)

    difficulty = estimate_difficulty(question)

    strategy = select_strategy(intent, difficulty, user)



    print("\n--- ALAE Decision ---")
    print("Intent:", intent)
    print("Difficulty:", difficulty)
    print("Strategy:", strategy)
    print("User confidence:", user["confidence"])


    feedback = input("\nDid you find the answer helpful? (y/n): ").strip().lower()

    if feedback == "y":
        update_confidence(user, "understood")

    elif feedback == "n":
        update_confidence(user, "confused")
