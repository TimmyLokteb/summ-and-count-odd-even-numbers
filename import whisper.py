import whisper

def generate_subtitles_simple(audio_path, output_path="subtitles.srt"):
    """
    audio to subtitles.srt
    :param audio_path: 
    :param output_path: 
    """

    model = whisper.load_model("base")
    result = model.transcribe(audio_path, language="ru")

    with open(output_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result["segments"], start=1):
            start = format_time(segment["start"])
            end = format_time(segment["end"])
            text = segment["text"]

            # write ,srt
            f.write(f"{i}\n")
            f.write(f"{start} --> {end}\n") 
            f.write(f"{text}\n\n")

    print(f"subtitles saved {output_path}")

def format_time(seconds):
    """HH:MM:SS,ms"""
    millis = int((seconds % 1) * 1000)
    seconds = int(seconds)
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02},{millis:03}"

if __name__ == "__main__":
    file = "C:/Users/User/Desktop/4.mp4" #file path
    generate_subtitles_simple(file, "C:/Users/User/Desktop/4_subtitles.srt") #file output
