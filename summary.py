import requests
import textwrap
import re

# 🔒 Replace with your Hugging Face API key
API_KEY = "your Hugging Face API key"

# ✅ Use a balanced and reliable model (less repetition)
MODEL = "facebook/bart-large-cnn"

def clean_summary(text):
    """Remove repeated phrases and extra spaces."""
    # Remove duplicated words/phrases like 'waving her wand again' repeated
    cleaned = re.sub(r'\b(\w+\s+){1,3}\1+', r'\1', text)
    cleaned = re.sub(r'(\b\w+\b)( \1\b)+', r'\1', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()

def summarize_long_text(text, chunk_size=1000):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    summaries = []

    chunks = textwrap.wrap(text, chunk_size, break_long_words=False, replace_whitespace=False)
    print(f"🧩 Text split into {len(chunks)} chunks...")

    for i, chunk in enumerate(chunks, 1):
        print(f"⏳ Summarizing chunk {i}/{len(chunks)}...")
        payload = {
            "inputs": chunk,
            "parameters": {
                "min_length": 100,
                "max_length": 300,
                "temperature": 0.7
            }
        }

        response = requests.post(
            f"https://router.huggingface.co/hf-inference/models/{MODEL}",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and "summary_text" in data[0]:
                summary = clean_summary(data[0]["summary_text"])
                summaries.append(summary)
            else:
                print("⚠️ Unexpected response format:", data)
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")

    full_summary = clean_summary(" ".join(summaries))
    print("\n✅ Clean Final Summary Generated Successfully:\n")
    print(full_summary)
    return full_summary


if __name__ == "__main__":
    with open("transcript.txt", "r", encoding="utf-8") as f:
        full_text = f.read()

    summarize_long_text(full_text)
