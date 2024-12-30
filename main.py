from midiutil import MIDIFile

# Helper function to generate chords
def generate_chord(root, chord_type):
    chords = {
        "major": [0, 4, 7],
        "minor": [0, 3, 7],
        "diminished": [0, 3, 6],
        "augmented": [0, 4, 8],
        "sus2": [0, 2, 7],
        "sus4": [0, 5, 7],
        "maj7": [0, 4, 7, 11],
        "m7": [0, 3, 7, 10],
        "7": [0, 4, 7, 10],
        "dim7": [0, 3, 6, 9],
        "m7b5": [0, 3, 6, 10],
        "9": [0, 4, 7, 10, 14],
        "maj9": [0, 4, 7, 11, 14],
        "m9": [0, 3, 7, 10, 14],
        "11": [0, 4, 7, 10, 14, 17],
        "maj11": [0, 4, 7, 11, 14, 17],
        "m11": [0, 3, 7, 10, 14, 17],
        "13": [0, 4, 7, 10, 14, 17, 21],
        "maj13": [0, 4, 7, 11, 14, 17, 21],
        "m13": [0, 3, 7, 10, 14, 17, 21],
        "7#5": [0, 4, 8, 10],
        "maj7b5": [0, 4, 6, 11],
        "mMaj7": [0, 3, 7, 11],
        "7#9": [0, 4, 7, 10, 15],
        "7b9": [0, 4, 7, 10, 13],
        "7#11": [0, 4, 7, 10, 18],
        "7b13": [0, 4, 7, 10, 20],
        "add2": [0, 2, 4, 7],
        "add9": [0, 4, 7, 14],
        "add4": [0, 4, 5, 7],
        "power": [0, 7],
        "6": [0, 4, 7, 9],
        "m6": [0, 3, 7, 9],
        "6_9": [0, 4, 7, 9, 14],
        "b5": [0, 4, 6],
        "#5": [0, 4, 8],
        "quartal": [0, 5, 10],
        "quintal": [0, 7, 14]
    }
    return [root + interval for interval in chords[chord_type]]

# All 12 keys
keys = [
    60,  # C
    61,  # C#
    62,  # D
    63,  # D#
    64,  # E
    65,  # F
    66,  # F#
    67,  # G
    68,  # G#
    69,  # A
    70,  # A#
    71   # B
]

# Chord types
chord_types = [
    "major",
    "minor",
    "diminished",
    "augmented",
    "sus2",
    "sus4",
    "maj7",
    "m7",
    "7",
    "dim7",
    "m7b5",
    "9",
    "maj9",
    "m9",
    "11",
    "maj11",
    "m11",
    "13",
    "maj13",
    "m13",
    "7#5",
    "maj7b5",
    "mMaj7",
    "7#9",
    "7b9",
    "7#11",
    "7b13",
    "add2",
    "add9",
    "add4",
    "power",
    "6",
    "m6",
    "6_9",
    "b5",
    "#5",
    "quartal",
    "quintal"
]

# Generate MIDI files for each chord in all keys
for chord_type in chord_types:
    for root in keys:
        # Create a new MIDI file
        midi = MIDIFile(1)
        track = 0
        channel = 0
        volume = 100
        duration = 4

        # Add track name and tempo
        midi.addTrackName(track, 0, f"{chord_type} chord")
        midi.addTempo(track, 0, 120)

        # Generate the chord
        chord = generate_chord(root, chord_type)

        # Add the chord notes to the MIDI file
        time = 0
        for note in chord:
            midi.addNote(track, channel, note, time, duration, volume)

        # Determine file name based on root and chord type
        note_name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        file_name = f"{note_name[root % 12]}_{chord_type}.mid"

        # Save the MIDI file
        with open(file_name, "wb") as midi_file:
            midi.writeFile(midi_file)

print("MIDI files for all chords in all 12 keys have been created successfully!")
