def build_prompt(strategy, question, confidence):
    
    if confidence < 0.3:
        pacing = "very slow, step-by-step, extra explanation"
    elif confidence < 0.6:
        pacing = "moderate pace, clear explanations"
    else:
        pacing = "concise, efficient, minimal repetition"

    strategy_instructions = {
        "diagnostic_slow": (
            "Ask clarifying debugging questions one step at a time. "
            "Do NOT explain the solution yet."
        ),
        "diagnostic_fast": (
            "Ask concise diagnostic questions. Assume the user is competent."
        ),
        "side_by_side": (
            "Provide a structured comparison with clear sections, pros/cons, "
            "and when to use each option."
        ),
        "build_from_basics_slow": (
            "Start from first principles and build up gradually with examples."
            "Do NOT explain the abbreviations."
        ),
        "step_by_step": (
            "Explain sequentially without skipping reasoning."
        ),
        "direct": (
            "Give a direct, clear explanation."
        ),
    }

    return f"""
        You are a computer science and machine learning tutor.
        Assume the question is about programming, algorithms, or ML unless stated otherwise.
        Your behavior is FIXED by the rules below.

        Strategy (DO NOT CHANGE):
        {strategy_instructions[strategy]}

        Delivery style:
        Speak at a {pacing} pace.

        Rules:
        - Do NOT change the strategy.
        - Do NOT decide how to teach.
        - ONLY decide wording and examples.
        - Follow the structure implied by the strategy.

        Question:
        {question}
    """


