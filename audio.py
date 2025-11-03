# audio_download.py

# ✅ Install dependencies (run only once)
# !pip install -q yt_dlp ffmpeg-python

import yt_dlp
import os

def download_audio(video_url, filename="audio.wav"):
    """Download audio from YouTube as a .wav file"""
    # Clean the URL (remove ?si= etc.)
    video_url = video_url.split("?")[0]

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'audio',  # Base name only (no extension)
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
            'quiet': False,
            'noplaylist': True,
            'nocheckcertificate': True,
        }

        print("🎧 Downloading audio from:", video_url)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        # Handle yt_dlp double-extension bug
        if os.path.exists("audio.wav"):
            final_name = "audio.wav"
        elif os.path.exists("audio.wav.wav"):
            os.rename("audio.wav.wav", "audio.wav")
            final_name = "audio.wav"
        else:
            print("❌ Audio file not found after download.")
            return None

        print(f"✅ Audio downloaded successfully: {final_name}")
        return final_name

    except Exception as e:
        print("❌ Error downloading audio:", e)
        return None


# ✅ Example usage
if __name__ == "__main__":
    video_url = "https://youtu.be/hD2l1TFWIUc"  # Replace with your YouTube link
    download_audio(video_url)
