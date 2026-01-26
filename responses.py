def generate_response(strategy, question):
    if strategy == "diagnostic_slow":
        return (
            "Let's debug this step by step.\n"
            "First, what exactly is the error message?\n"
            "Then, which line of code triggers it?"
        )

    if strategy == "diagnostic_fast":
        return (
            "What error are you getting and on which line?\n"
            "Paste the relevant code."
        )

    if strategy == "side_by_side":
        return (
            "Let's compare the two options side by side:\n"
            "- Key differences\n"
            "- Pros and cons\n"
            "- When to use each"
        )

    if strategy == "build_from_basics_slow":
        return (
            "This is an advanced topic, so let's start from the basics.\n"
            "We'll build the idea step by step before going deeper."
        )

    if strategy == "step_by_step":
        return (
            "Let's take this one step at a time.\n"
            "I'll explain each part clearly before moving on."
        )

    return "Here's a direct explanation of your question."
