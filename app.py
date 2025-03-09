from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Load knowledge data
with open("knowledge_base.json", "r") as file:
    knowledge_data = json.load(file)

@app.route('/external_knowledge', methods=['GET'])
def external_knowledge():
    query = request.args.get('query', '').lower()

    if not query:
        return jsonify({"data": [{"content": "External Knowledge API is working! Please provide a query parameter to receive journaling guidance."}]}), 200

    if "trauma" in query or "grief" in query or "stress" in query:
        approach = "Expressive_Writing_Therapy"
    elif "gratitude" in query or "happiness" in query:
        approach = "Positive_Psychology_Gratitude_Journaling"
    elif "self-identity" in query or "reframe" in query:
        approach = "Narrative_Therapy"
    elif "negative thoughts" in query or "anxiety" in query:
        approach = "Cognitive_Behavioral_Therapy"
    else:
        return jsonify({"data": []})  # Return empty response if no match is found

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
    port = int(os.environ.get("PORT", 52000))  # Use Render-assigned port
    app.run(host="0.0.0.0", port=port, debug=True)



