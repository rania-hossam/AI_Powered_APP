import streamlit as st
from scripts.convertAudioToMidi import transcribe_audio_to_midi
from scripts.Notes_from_MIDI import extract_notes_from_single_midi
from scripts.musicalnotation import convert_midi_to_png
from scripts.manipulation import image_manipulation
from scripts.result import deploy_cluster
import subprocess
from audiocraft.models import MusicGen
import streamlit as st 
import torch 
import torchaudio
import numpy as np
import base64
import os
import sys
def feature_transcribe_audio(unique_key):
    st.header("SHOW INFORMATION ABOUT MUSIC NOTES")
    audio_file = st.file_uploader("Upload Audio", type=['wav', 'mp3', 'ogg'],key=unique_key)
    
    if audio_file is not None:
        temp_directory = "temp_audio"
        if not os.path.exists(temp_directory):
            os.makedirs(temp_directory)

        temp_file_path = os.path.join(temp_directory, audio_file.name)
        with open(temp_file_path, "wb") as f:
            f.write(audio_file.getbuffer())

        output_directory = "C:./ML_OPS/MIDIFILES"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Transcribe the audio to MIDI
        try:
            transcribe_audio_to_midi(output_directory, temp_file_path)
            st.success("Audio transcription to MIDI completed successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
            sys.exit(1)


def music_information():
    feature_transcribe_audio("audio_uploader_feature_2")
    output="./MIDIFILES/newly_generated_music_notes_basic_pitch.mid"
    note_info_list=extract_notes_from_single_midi(output)
    st.dataframe(note_info_list)

def music_sheet_generation():
    midi_file = r'C:\Users\rania\Downloads\ML_OPS\MIDIFILES\newly_generated_music_notes_basic_pitch.mid'
    output_png = r'C:\Users\rania\Downloads\ML_OPS\themes\kkkk.png'
    musescore_exe = r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe"

    # Button to trigger conversion
    if st.button('Generate Music Sheet'):
        convert_midi_to_png(midi_file, output_png, musescore_exe)

        if os.path.exists(output_png):
            st.image('./themes/image.png')
def show_cluster():
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

        # Get the path of the trained model (change this path accordingly)
        model_path = "path/to/your/kmeans_model.pkl"

        # Button to trigger the deployment
        if st.button("your Cluster"):
            # Call the deploy_cluster function
            predictions = deploy_cluster(model_path, uploaded_file)


def run_setup_script():
        subprocess.Popen(['python', './ML_OPS/server.py'])
@st.cache_resource
def load_model():
    model = MusicGen.get_pretrained('facebook/musicgen-small')
    return model

def generate_music_tensors(description, duration: int):
    print("Description: ", description)
    print("Duration: ", duration)
    model = load_model()

    model.set_generation_params(
        use_sampling=True,
        top_k=250,
        duration=duration
    )

    output = model.generate(
        descriptions=[description],
        progress=True,
        return_tokens=True
    )

    return output[0]


def save_audio(samples: torch.Tensor):
    """Renders an audio player for the given audio samples and saves them to a local directory.

    Args:
        samples (torch.Tensor): a Tensor of decoded audio samples
            with shapes [B, C, T] or [C, T]
        sample_rate (int): sample rate audio should be displayed with.
        save_path (str): path to the directory where audio should be saved.
    """

    print("Samples (inside function): ", samples)
    sample_rate = 32000
    save_path = "audio_output/"
    assert samples.dim() == 2 or samples.dim() == 3

    samples = samples.detach().cpu()
    if samples.dim() == 2:
        samples = samples[None, ...]

    for idx, audio in enumerate(samples):
        audio_path = os.path.join(save_path, f"audio_{idx}.wav")
        torchaudio.save(audio_path, audio, sample_rate)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

st.set_page_config(
    page_icon= "musical_note",
    page_title= "Music Gen"
)




# Set the page config to widen the app and set a title
st.set_page_config(page_title="Learn Music Easly for Dyslexia", layout="wide")

def main():
    # Inject custom CSS for image brightness, spacing, text color, and header color
    st.markdown("""
        <style>
            img { 
                filter: brightness(50%); /* Image brightness */
                display: block; /* Ensures the image is on its own line */
                margin-bottom: 20px; /* Space below the image */
                width: 200px; /* Set a fixed width for the image */
            }
            h1, h2, h3, h4, h5, h6, div, p, a { /* Targeting all text elements */
                color: #f07807; /* Custom text color */
            }
            .sidebar .sidebar-content {
                padding-top: 0px; /* Reduce padding at the top of the sidebar */
            }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar for navigation or additional information
    with st.sidebar:
        st.image("./themes/logo-modified.png")  # Image in the sidebar
        
        # Adding options/features to the sidebar
        feature_selected = st.selectbox(
            "Choose a feature",
            ["Home", "VISUALIZING MUSIC SHEETS IN COLORY WAY", "SHOW INFORMATION ABOUT MUSIC NOTES", "MUSIC GENERATION", "SHOW MUSIC SHEETS FROM YOUR AUDIO"]  # List your features here
        )

    # Main content area based on the selected feature
    if feature_selected == "Home":
        display_home_page()
    elif feature_selected == "VISUALIZING MUSIC SHEETS IN COLORY WAY":
        display_feature_1()
    elif feature_selected == "SHOW INFORMATION ABOUT MUSIC NOTES":
        display_feature_2()
    elif feature_selected == "MUSIC GENERATION":
        display_feature_3()
    elif feature_selected == "SHOW MUSIC SHEETS FROM YOUR AUDIO":
        display_feature_4()
        music_sheet_generation()

def display_home_page():
    # Home page content
    st.title("Learn Music Easly for Dyslexia")
    st.subheader("Welcome to Music Learning!🎷🎺🪗")
    st.write("This application is designed to help individuals with dyslexia learn music in a more accessible way.")



def display_feature_1():
    st.title("Visualizing Music Sheets in a Colorful Way")
    show_cluster()
    # Button to show the link
    if st.button("Show Music Sheet Visualization"):
        # Provide a clickable link to the local server hosting the file
        st.markdown("Click [here](http://localhost:8000/ml_color_music_score-master/CLUSTER_REPRESENTATION.html) to view the music sheet visualization.", unsafe_allow_html=True)

    



def display_feature_2():
    # Feature 2 content
    st.title("SHOW INFORMATION ABOUT MUSIC NOTES")
    feature_transcribe_audio("audio_uploader_feature_2")
def display_feature_3():
    # Feature 3 content
    st.title("MUSIC GENERATION ")
    st.title("Text to Music Generator🎵")

    with st.expander("See explanation"):
        st.write("Music Generator app built using Meta's Audiocraft library. We are using Music Gen Small model.")

    text_area = st.text_area("Enter your description.......")
    time_slider = st.slider("Select time duration (In Seconds)", 0, 20, 10)

    if text_area and time_slider:
        st.json({
            'Your Description': text_area,
            'Selected Time Duration (in Seconds)': time_slider
        })

        st.subheader("Generated Music")
        music_tensors = generate_music_tensors(text_area, time_slider)
        print("Musci Tensors: ", music_tensors)
        save_music_file = save_audio(music_tensors)
        audio_filepath = 'audio_output/audio_0.wav'
        audio_file = open(audio_filepath, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes)
        st.markdown(get_binary_file_downloader_html(audio_filepath, 'Audio'), unsafe_allow_html=True)

def display_feature_4():
    # Feature 3 content
    st.title("SHOW MUsic SHEETS FROM YOUR AUDIO ")

if __name__ == "__main__":
    main()
