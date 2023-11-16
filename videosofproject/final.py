import streamlit as st
from scripts.convertAudioToMidi import transcribe_audio_to_midi
from scripts.Notes_from_MIDI import extract_notes_from_single_midi
import os
import sys

def feature_transcribe_audio():
    st.header("SHOW INFORMATION ABOUT MUSIC NOTES")
    audio_file = st.file_uploader("Upload Audio", type=['wav', 'mp3', 'ogg'])
    
    if audio_file is not None:
        temp_directory = "temp_audio"
        if not os.path.exists(temp_directory):
            os.makedirs(temp_directory)

        temp_file_path = os.path.join(temp_directory, audio_file.name)
        with open(temp_file_path, "wb") as f:
            f.write(audio_file.getbuffer())

        output_directory = "C:\\Users\\rania\\Downloads\\ML_OPS\\MIDIFILES"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Transcribe the audio to MIDI
        try:
            transcribe_audio_to_midi(output_directory, temp_file_path)
            st.success("Audio transcription to MIDI completed successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
            sys.exit(1)
    output="C:\\Users\\rania\\Downloads\\ML_OPS\\MIDIFILES\\newly_generated_music_notes_basic_pitch.mid"
    note_info_list=extract_notes_from_single_midi(output)
    st.dataframe(note_info_list)


if __name__ == "__main__":
    feature_transcribe_audio()

