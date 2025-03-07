import json

# Load the knowledge base
with open("knowledge_base.json", "r") as file:
    knowledge_data = json.load(file)

# Example access
print(knowledge_data["Positive_Psychology_Gratitude_Journaling"]["structure"])
