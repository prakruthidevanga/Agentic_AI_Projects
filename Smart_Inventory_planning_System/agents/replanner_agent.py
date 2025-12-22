def replanner_agent(feedback):
    if "increase" in feedback.lower():
        return "Replanning triggered due to demand change"
    return "No replanning required"