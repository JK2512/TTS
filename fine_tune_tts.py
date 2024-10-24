from gtts import gTTS
import os

# Define a dictionary for technical abbreviations and their phonetic pronunciation
technical_terms = {
    "API": "A P I",
    "CUDA": "C U D A",
    "TTS": "T T S",
    "OAuth": "O Auth",
    "REST": "R E S T",
}

# Function to handle technical abbreviations
def process_text(text):
    words = text.split()
    processed_text = []
    for word in words:
        # Check if the word is in the technical terms dictionary
        if word in technical_terms:
            # Replace the word with its phonetic form
            processed_text.append(technical_terms[word])
        else:
            processed_text.append(word)
    # Join the processed words back into a string
    return " ".join(processed_text)

# Function to convert text to speech with error handling
def text_to_speech(text, filename):
    try:
        # Create TTS object with the processed text
        tts = gTTS(text=text, lang='en')
        # Save the audio file
        tts.save(filename)
        print(f"Generated audio for: {text}")
    except Exception as e:
        print(f"Error generating audio for '{text}': {e}")

# Load vocabulary from a text file
with open('vocabulary.txt', 'r') as file:
    lines = file.readlines()

# Iterate through each line and convert text to speech
for i, line in enumerate(lines):
    # Clean up the line and process technical abbreviations
    text = line.strip()
    if text:
        processed_text = process_text(text)
        print(f"Processing: {processed_text}")
        filename = f"output_{i}.mp3"
        # Convert to speech and save the file
        text_to_speech(processed_text, filename)
    else:
        print(f"Skipped empty line at line {i+1}")

print("All audio files generated successfully.")


