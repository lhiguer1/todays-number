import re
from pathlib import Path
import speech_recognition as sr

def get_number_from_transcript(transcript):
    """Return number extracted from transcript. Return None if number is not found."""
    if not transcript:
        return None

    numbers = {
        '10': 10, 'ten': 10,
        '9': 9,   'nine': 9,
        '8': 8,   'eight': 8,
        '7': 7,   'seven': 7,
        '6': 6,   'six': 6,
        '5': 5,   'five': 5,
        '4': 4,   'four': 4,
        '3': 3,   'three': 3,
        '2': 2,   'two': 2,
        '1': 1,   'one': 1,
    }
    num_pattern = '|'.join(i for i in numbers)
    pattern = f'today\'?s number is.*(?P<todays_number>{num_pattern})'
    m = re.search(pattern, transcript)
    if m:
        return numbers[m.group('todays_number')]

def get_transcript(file:Path):
    try:
        r = sr.Recognizer()
        with sr.AudioFile(file.as_posix()) as source:
            audio = r.record(source)
            transcript = r.recognize_google(audio)
            return transcript
    except sr.UnknownValueError:
        pass
        # raise sr.UnknownValueError(f"Google Speech Recognition could not understand audio for {file}")
    except sr.RequestError as e:
        pass
        # raise sr.UnknownValueError(f"Could not request results from Google Speech Recognition service for {file}: {e}")