Adaptive LLM Answering Engine (ALAE)

1.  Overview

    This is an adaptive tutoring system for AI/ML and programming concepts that adjusts explanation strategy based on user competence, memory, difficulty, and feedback to customize and tailor your experience according to your skill level, strengths and weaknesses, and confidence level.

2.  Core Idea

    This adaptive engine stores user skill level, confidence, topic familiarity, and feedback to customize future explanations.

    All decisions about pacing, structure, and appropriateness are made by ALAE itself. The LLM does not decide how to teach; it is prompted explicitly based on system-selected strategy and user memory.

3.  High-Level Pipeline

    How a single question flows through the system

                    User Question
                          ↓
         Topic / Intent / Difficulty Detection
                          ↓
         Strategy Selection (uses user memory)
                          ↓
                 Prompt Construction
                          ↓
                LLM Answer Generation
                          ↓
                 User Feedback (y/n)
                          ↓
                    Memory Update

    What's going on here?
    The program asks you for your question. After you enter it, the ALAE figures out the topic, the intent behind your query (ex. comparison, debugging, etc.), and it estimates the difficulty level based on keywords in your prompt. It then selects a strategy to respond (ex. slow_step_by_step or clear_and_concise) based on the information it gets from the prompt, the user confidence level, and expertise. Then it constructs a prompt by changing parts of a pre-programmed script to match the strategy. After this it sends the prompt to llama 3.1 instant through Groq API and receives the answer. After you're done reading the answer, you give feedback on the answer. It adjusts the confidence level, known topics, and confusion topics, and updates the user profile accordingly. This is a memory update. Then you ask your next question and this continues until you exit.

4.  User Memory Model

    This system remembers some information while interacting with the user. It stores "level" which is your expertise level, your confidence (between 0 and 1), the size and style of answers you prefer (currently under development), the topics you know well, the topics you were confused about, and the per-topic confidence level (again between 0 and 1). It updates these from the feedback you give after each prompt-answer.

        Global confidence
            Tracks overall understanding level.

        Topic confidence
            Tracks mastery per concept (e.g., CNN, SGD).

        Known topics
            Topics the user has shown understanding of.

        Confusion topics
            Topics the user has struggled with.

    Memory is updated only through explicit user feedback.

5.  Strategy System

    The system selects an answering strategy based on the interpreted prompt and user memory. It looks for keywords in the question, like 'how' and 'what is' and 'vs' etc to find out the intent, like 'procedure', 'definition', and 'comparison'.
    After this it looks for keywords for topic and difficulty estimation, like 'CNN' or 'adam' in your question. After that's done, it figures out the topic and the difficulty. It looks at your global confidence and your per-topic confidence, the topics you are good at, the topics you struggle with, and your preference (not yet implemented), like what style you prefer or how lengthy you wish your answers to be.

        Confused topics force slower, foundational explanations

        Advanced topics may be simplified depending on user level

        High topic confidence allows concise responses

        Strategy controls structure and pacing, not content

    Examples of strategy names: 'diagnostic_fast', 'side_by_side', etc.

6.  Prompt Control Philosophy

    If there is one thing you have to understand about this project, it is the policy used for deciding what the LLM does.
    The LLM is treated only as a language renderer. Prompts explicitly constrain behavior. The model cannot change strategy. Adaptation happens outside the LLM. So the LLM has minimal control over the length, style, etc. It does not decide what or how to teach; it only generates language within explicit constraints.

    So the LLM generates text. It does not take any decisions.
    This is the core philosophy behind this project.

7.  File Structure

    The functions and responsibilities of each step been distributed among the different files in the project.

        main.py — system pipeline coordinator

        user_model.py — user memory & learning

        topic.py — topic extraction

        intent.py — intent classification

        difficulty.py — difficulty estimation

        strategy.py — strategy selection logic

        prompt.py — prompt construction

        llm.py — LLM API wrapper

    Extra care has been taken to ensure that each file only has one responsibility. This modular approach improves readability and comprehension. This separation ensures that decision-making, memory, and language generation remain independent.

8.  Design Principles

    I have prioritized simplicity and explainability over extra features and cleverness. The goal was to make an AI/ML tutoring ALAE that would help you with your learning while at the same time allowing you to understand the logic behind what's going on in the application. This project itself serves as a lesson in AI/ML.
    For this I have selected a simple rule-based approach, although I do plan to upgrade it to a more flexible system later. This rule-based approach increases explainability and makes it easier to track what is going on. This is especially important in the development phase where understanding your code and its logic is more important than filling the project with gimmicks and fancy GUI elements.

9.  What This Project Is Not

    Now there is another thing you must understand about this project. This project is not intended to replace a human teacher or a production-grade tutoring platform. This project is still under development. But I will upgrade it and make it better with each feature and change in the logic.
    Right now it only uses a simple rule-based approach for choosing the strategy and finding out confidence levels. I plan to upgrade it to a more flexible and robust system later. Also, this project does not have a GUI. It is a simple command line application.
    Besides, I'm using a free Groq API which is capped at a limited number of requests for every few minutes. It cannot handle multiple users using it at the same time. So I suggest you to use your own API key if you want to test it out since I haven't included mine here. You can check the code for the API key at the file llm.py, client variable.

10. Current Status

    This project is still in its early stages of development. Many features are yet to be implemented and the logic can be improved further. But the core idea is here and working. v1.0 is stable and can be used for basic testing and understanding of the concept. This AI/ML adaptive tutoring engine can be further improved with more advanced techniques and better logic.

11. How to Run

    Make sure you have Python installed. Then install the required packages using pip. After this you can run the main.py file to start the application.

        pip install -r requirements.txt
        python main.py

    This project uses Python 3.10 or higher.

    Make sure to set your Groq API key in llm.py before running.

12. Why This Exists

    I created this project to explore and understand ALAE systems better. I wanted to learn how to build an adaptive tutoring system that would help users learn AI/ML and programming better and more efficiently. However, this project is still far from perfect and there is much to be done to improve it. But I believe this is a good starting point for anyone interested in building adaptive tutoring systems using LLMs.
