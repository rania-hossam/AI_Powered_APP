from music21 import converter, lily

# Load MIDI file
midi = converter.parse('C:\\Users\\rania\\Downloads\\ML_OPS\\MIDIFILES\\newly_generated_music_notes_basic_pitch.mid')

# Convert to LilyPond format
lily_content = lily.translate.LilypondConverter().parse(midi)
