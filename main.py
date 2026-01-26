from user_model import create_user_profile, update_confidence
from intent import detect_intent
from difficulty import estimate_difficulty
from strategy import select_strategy
from prompt import build_prompt
from llm import render_answer
from topic import extract_topic


user = create_user_profile()

while True:
    question = input("\nAsk a question (or type 'exit' to quit): ")

    if question.lower().strip() == 'exit':
        break

    topic = extract_topic(question)

    intent = detect_intent(question)

    difficulty = estimate_difficulty(question)

    strategy = select_strategy(intent, difficulty, user, topic)

    print("\n--- ALAE Decision ---")
    print("Intent:", intent)
    print("Difficulty:", difficulty)
    print("Strategy:", strategy)
    print("User confidence:", user["confidence"])
    print("User level:", user["level"])
    print("Confusion topics:", user["confusion_topics"])
    print("Known topics:", user["known_topics"])
    print("Topic confidence:", user["topic_confidence"])


    prompt = build_prompt(strategy, question, user["confidence"])
    answer = render_answer(prompt)

    print("\n--- Generated Prompt ---")
    print(prompt)

    print("\n--- ALAE Answer ---")
    print(answer)



    feedback = input("\nDid you find the answer helpful? (y/n): ").strip().lower()

    if feedback == "y":
        update_confidence(user, "understood")

        if topic:
            current = user["topic_confidence"].get(topic, 0.5)
            user["topic_confidence"][topic] = min(1.0, current + 0.1)
            user["topic_confidence"][topic] = round(user["topic_confidence"][topic], 2)

            user["known_topics"].add(topic)
            user["confusion_topics"].discard(topic)

    elif feedback == "n":
        update_confidence(user, "confused")

        if topic:
            current = user["topic_confidence"].get(topic, 0.5)
            user["topic_confidence"][topic] = max(0.0, current - 0.1)
            user["topic_confidence"][topic] = round(user["topic_confidence"][topic], 2)

            user["confusion_topics"].add(topic)
            user["known_topics"].discard(topic)

