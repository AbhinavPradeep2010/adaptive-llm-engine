def estimate_difficulty(question: str) -> str:
    question = question.lower()
    advanced_keywords = [
        "gradient",
        "backprop",
        "sgd",
        "adam",
        "neural network",
        "cnn",
        "loss function",
        "mean squared error",
        "decorator",
        "polymorphism",
        "duck typing",
        "inheritance",
    ]

    for i in advanced_keywords:
        if i in question:
            return "advanced"
        
    return "basic"
