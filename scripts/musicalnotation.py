import subprocess

def convert_midi_to_png(midi_file_path, output_png_path, musescore_path):
    command = [musescore_path, midi_file_path, '-o', output_png_path]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Standard Output: {result.stdout.decode()}")
        print(f"Standard Error: {result.stderr.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Error running MuseScore: {e}")
    except OSError as e:
        if e.winerror == 740:
            print("Permission denied: MuseScore requires elevated privileges. Please run this script as an administrator.")
        else:
            print(f"OS error: {e}")

# Example usage
midi_file = './MIDIFILES/newly_generated_music_notes_basic_pitch.mid'
output_png = './themes/nn.png'
musescore_exe = "./MuseScore 4/bin/MuseScore4.exe"

convert_midi_to_png(midi_file, output_png, musescore_exe)
