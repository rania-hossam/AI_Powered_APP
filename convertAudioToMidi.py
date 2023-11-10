import subprocess
import sys

def transcribe_audio_to_midi(input_audio_path, output_directory):
    try:
        # Use the basic-pitch command line tool to transcribe audio to MIDI
        subprocess.run(["basic-pitch", output_directory, input_audio_path], check=True)

        print("Audio transcription to MIDI completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python transcribe_audio_to_midi.py input_audio_path output_directory")
        sys.exit(1)

    input_audio_path = sys.argv[1]
    output_directory = sys.argv[2]

    transcribe_audio_to_midi(input_audio_path ,output_directory )

