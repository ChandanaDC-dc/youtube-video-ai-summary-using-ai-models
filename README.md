# 🎧 YouTube Audio to Text Converter (Offline Whisper + yt_dlp)

This project lets you **download audio from any YouTube video** and **convert it into text (transcription)** using OpenAI’s **Whisper** model — all **offline**, without any API key.

---

## 🧩 Features

✅ Download audio directly from a YouTube URL  
✅ Automatically converts it into `.wav` format  
✅ Transcribes the entire audio (not just a preview)  
✅ Saves full text into `transcript.txt`  
✅ 100% offline — no OpenAI API key required  

---

## 🧠 Requirements

Make sure you have **Python 3.8+** installed.

### Install the required libraries:
```bash
pip install yt_dlp openai-whisper ffmpeg-python






| File       | Description                                         |
| ---------- | --------------------------------------------------- |
| `audio.py` | Downloads YouTube audio and saves it as `audio.wav` |
| `text.py`  | Converts the saved audio into text using Whisper    |
|`summary.py`| Converts the saved raw text into the summarized theory|

for the summarization purpose using the LLM models to convert the raw transcript into summary format, so using their API key. 
