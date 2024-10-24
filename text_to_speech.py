from gtts import gTTS
import os

# Load vocabulary from a text file
with open('vocabulary.txt', 'r') as file:
    lines = file.readlines()

# Iterate through each line and convert text to speech
for i, line in enumerate(lines):
    # Clean up the line
    text = line.strip()
    if text:
        # Create TTS object
        tts = gTTS(text=text, lang='en')
        # Save the audio file
        tts.save(f"output_{i}.mp3")
        print(f"Generated audio for: {text}")

print("All audio files generated successfully.")
