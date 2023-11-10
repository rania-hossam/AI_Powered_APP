import os
import pretty_midi

def extract_notes_from_midi(midi_directory):
    note_info_list = []

    for filename in os.listdir(midi_directory):
        if filename.endswith('.mid'):
            midi_path = os.path.join(midi_directory, filename)
            midi_data = pretty_midi.PrettyMIDI(midi_path)

            for instrument in midi_data.instruments:
                for i, note in enumerate(instrument.notes):
                    note_name = pretty_midi.note_number_to_name(note.pitch)
                    duration = note.end - note.start

                    note_info = {
                        "file": filename,
                        "instrument": instrument.name,
                        "pitch": note.pitch,
                        "note_name": note_name,
                        "duration": duration,
                    }
                    note_info_list.append(note_info)

    return note_info_list

if __name__ == "__main__":
    midi_directory = 'C:\\Users\\rania\Downloads\\ML_OPS\\MIDIFILES'

    extracted_notes = extract_notes_from_midi(midi_directory)

    for note_info in extracted_notes:
        print(f'File: {note_info["file"]}, '
              f'Instrument: {note_info["instrument"]}, '
              f'Pitch={note_info["pitch"]}, '
              f'Note Name={note_info["note_name"]}, '
              f'Duration={note_info["duration"]:.4f} seconds')
    
