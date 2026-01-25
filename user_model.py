def create_user_profile():
    return {
        "level": "unknown",
        "confidence": 0.5,
        "prefers":{
            "detail": "medium",
            "style": "explanatory"
        },
        "known_topics": set(),
        "confusion_topics": set()
    }

def update_confidence(user_profile, signal):
    if signal == "confused":
        user_profile["confidence"] = max(0.0, user_profile["confidence"] - 0.1)
    elif signal == "understood":
        user_profile["confidence"] = min(1.0, user_profile["confidence"] + 0.1)

    user_profile["confidence"] = round(user_profile["confidence"], 2)