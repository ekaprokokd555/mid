from midiutil import MIDIFile
import random

def generate_track(file_name, scale, instrument_type, duration=30, channel=0):
    # Set up a single-track MIDI file
    midi = MIDIFile(1)
    track = 0
    time = 0
    midi.addTrackName(track, time, instrument_type)
    midi.addTempo(track, time, 120)

    for i in range(duration * 4):  # 4 beats per second
        note = random.choice(scale)

        # Modify note based on instrument type
        if instrument_type == "bass":
            note -= 12  # Lower octave
        elif instrument_type == "chorus":
            note += 12  # Higher octave
        elif instrument_type == "beat":
            note = random.choice([35, 36, 38, 40])  # Drum kit MIDI notes

        duration = random.choice([0.25, 0.5, 1])
        volume = random.randint(50, 100) if instrument_type != "beat" else random.randint(70, 110)
        midi.addNote(track, channel, note, time, duration, volume)

        time += 0.25  # Increment time by quarter note

    # Write to file
    with open(file_name, "wb") as output_file:
        midi.writeFile(output_file)

    print(f"{instrument_type.capitalize()} track saved to {file_name}")

def generate_music_all_parts(base_name, genre="default", duration=30):
    # Define scales for different genres
    scales = {
        "default": [60, 62, 64, 65, 67, 69, 71, 72],  # C major scale
        "jazz": [60, 63, 65, 66, 69, 72, 75, 78],     # Jazz scale
        "blues": [60, 63, 65, 66, 67, 70, 72],       # Blues scale
        "rock": [60, 62, 64, 67, 69, 71, 72],         # Rock scale
        "classical": [60, 62, 64, 65, 67, 69, 71, 72], # Classical scale
        "electronic": [60, 62, 63, 65, 68, 72, 75],  # Electronic feel
    }

    # Get scale for the specified genre
    scale = scales.get(genre.lower(), scales["default"])

    # Generate individual tracks
    generate_track(f"{base_name}_bass.mid", scale, "bass", duration)
    generate_track(f"{base_name}_piano.mid", scale, "piano", duration)
    generate_track(f"{base_name}_chorus.mid", scale, "chorus", duration)
    generate_track(f"{base_name}_beat.mid", scale, "beat", duration, channel=9)  # Percussion channel

    print(f"All tracks for {genre} genre saved as separate files.")

# Example usage
generate_music_all_parts("output_music", genre="jazz", duration=60)
