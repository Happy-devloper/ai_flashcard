import json
import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()
topic = input("What topic do you want to study? ")
client = InferenceClient(token=os.getenv("HF_TOKEN"))
response =  client.chat.completions.create(
    model="Qwen/Qwen3-8B",
    messages=[{
        "role": "user",
        "content": f'Create 5 flashcards about {topic}. Return only a JSON list with "question" and "answer" fields.',
    }],
)
cards = json.loads(response.choices[0].message.content)

for card in cards:
    print(f"\nQuestion: {card['question']}")
    input("Your answer (press Enter to reveal): ")
    print(f"Answer: {card['answer']}")