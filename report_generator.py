def generate_report(topic, research_data):
    prompt = f"""
    Generate a structured research report on: {topic}

    Include:
    1. Cover Page
    2. Title
    3. Introduction
    4. Key Findings
    5. Challenges
    6. Future Scope
    7. Conclusion

    Data:
    {research_data}
    """

    return prompt