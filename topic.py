def extract_topic(question: str):
    question = question.lower()

    topics = [
        "gradient descent",
        "backprop",
        "sgd",
        "adam",
        "neural network",
        "cnn",
        "loss function",
        "decorator",
        "polymorphism",
        "duck typing",
        "inheritance"
    ]

    for t in topics:
        if t in question:
            return t

    return None
