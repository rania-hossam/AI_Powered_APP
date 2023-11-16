import subprocess
import sys

def transcribe_audio_to_midi(output_directory,input_audio_path):
    try:
        # Use the basic-pitch command line tool to transcribe audio to MIDI
        subprocess.run(["basic-pitch", output_directory, input_audio_path], check=True)

        print("Audio transcription to MIDI completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)


