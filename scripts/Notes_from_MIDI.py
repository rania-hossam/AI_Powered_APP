import pretty_midi

def extract_notes_from_single_midi(midi_path):
    note_info_list = []
    midi_data = pretty_midi.PrettyMIDI(midi_path)

    for instrument in midi_data.instruments:
        for note in instrument.notes:
            note_name = pretty_midi.note_number_to_name(note.pitch)
            duration = note.end - note.start

            note_info = {
                "instrument": instrument.name,
                "pitch": note.pitch,
                "note_name": note_name,
                "duration": duration,
            }
            note_info_list.append(note_info)

    return note_info_list

extract_notes_from_single_midi("C:\\Users\\rania\\Downloads\\ML_OPS\\MIDIFILES\\newly_generated_music_notes_basic_pitch.mid")