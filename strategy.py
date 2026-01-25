
def select_strategy(intent, difficulty, user_profile):
    confidence = user_profile["confidence"]
    level = user_profile["level"]

    if intent == "debugging":
        if confidence < 0.4:
            return "diagnostic_slow"
        else: 
            return "diagnostic_fast"
        

    if intent == "comparison":
        return "side_by_side"
    
    
    if difficulty == "advanced" and level != "advanced":
        return "build_from_basics_slow"
    

    if confidence < 0.4:
        return "step_by_step"
    
    return "direct"
