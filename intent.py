def detect_intent(question):
    question = question.lower()
    
    for i in ["bug", "error", "issue", "problem"]:
        if i in question:
            return "debugging"


    for i in ["vs", "differenc", "compare"]:
        if i in question:
            return "comparison"
        
    for i in ["explain", "why"]:
        if i in question:
            return "explanation"
        
    for i in ["how", "way to", "steps", "method"]:
        if i in question:
            return "procedure"
    
    for i in ["what is", "define", "meaning"]:
        if i in question:
            return "definition"
    return "general"