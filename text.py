import whisper
import os

def transcribe_audio(audio_file="audio.wav"):
    """Transcribe full audio into text using Whisper"""
    if not os.path.exists(audio_file):
        print(f"❌ Audio file '{audio_file}' not found. Please run audio_download.py first.")
        return ""

    print("🧠 Loading Whisper model (small)…")
    model = whisper.load_model("small")  # Options: tiny, base, small, medium, large

    print("🎙️ Transcribing full audio… please wait…")
    result = model.transcribe(audio_file)

    full_text = result["text"]

    # ✅ Save full transcript
    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write(full_text)

    print("\n✅ Full transcription complete!")
    print("📝 Saved as: transcript.txt")

    # ✅ Print the entire text (no truncation)
    print("\n--- FULL TRANSCRIPT ---\n")
    print(full_text)

    return full_text


# ✅ Example usage
if __name__ == "__main__":
    transcribe_audio("audio.wav")
