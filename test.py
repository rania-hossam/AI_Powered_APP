from convertAudioToMidi import transcribe_audio_to_midi
if __name__ == "__main__":
    input_audio_path = "C:\\Users\\rania\\Downloads\\ML_OPS\\newly_generated_music_notes.mp3"
    output_directory = "C:\\Users\\rania\\Downloads\\ML_OPS\\MIDIFILES"

    transcribe_audio_to_midi(input_audio_path, output_directory)
