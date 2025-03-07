from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load knowledge data
with open("knowledge_base.json", "r") as file:
    knowledge_data = json.load(file)

@app.route('/external_knowledge', methods=['GET'])
def external_knowledge():
    """
    Handles Dify's External Knowledge API requests
    """
    query = request.args.get('query', '').lower()  # Get user's input query
    print("Received query:", query)  # Debugging print

    # Determine the best journaling approach based on user query
    if "trauma" in query or "grief" in query or "stress" in query:
        approach = "Expressive_Writing_Therapy"
    elif "gratitude" in query or "happiness" in query:
        approach = "Positive_Psychology_Gratitude_Journaling"
    elif "self-identity" in query or "reframe" in query:
        approach = "Narrative_Therapy"
    elif "negative thoughts" in query or "anxiety" in query:
        approach = "Cognitive_Behavioral_Therapy"
    else:
        return jsonify({"data": []})  # Return empty response if no approach is found

    # Prepare the response in Dify's required format
    response = {
        "data": [
            {
                "id": approach,
                "content": f"The recommended journaling approach for you is **{approach}**.",
                "metadata": {
                    "structure": knowledge_data[approach]["structure"],
                    "criteria": knowledge_data[approach]["criteria"],
                    "summarization": knowledge_data[approach]["summarization"]
                }
            }
        ]
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=52000, debug=True)

