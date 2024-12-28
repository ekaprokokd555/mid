from midiutil import MIDIFile
import random

def generate_music(file_name, genre="default", duration=30):
    # Set up MIDI file
    midi = MIDIFile(1)  # One track
    track = 0  # Track number
    time = 0  # Start at the beginning
    midi.addTrackName(track, time, "Generated Music")
    midi.addTempo(track, time, 120)  # Default tempo

    # Genre-based configuration
    scales = {
        "default": [60, 62, 64, 65, 67, 69, 71, 72],  # C major scale
        "jazz": [60, 63, 65, 66, 69, 72, 75, 78],     # Jazz scale
        "blues": [60, 63, 65, 66, 67, 70, 72],       # Blues scale
        "rock": [60, 62, 64, 67, 69, 71, 72],         # Rock scale
        "classical": [60, 62, 64, 65, 67, 69, 71, 72], # Classical scale
        "electronic": [60, 62, 63, 65, 68, 72, 75],  # Electronic feel
    }

    # Choose scale based on genre
    scale = scales.get(genre.lower(), scales["default"])

    # Generate random notes
    for i in range(duration * 4):  # 4 beats per second
        pitch = random.choice(scale)
        duration = random.choice([0.25, 0.5, 1, 2])  # Note duration in beats
        volume = random.randint(50, 100)  # Note volume

        midi.addNote(track, 0, pitch, time, duration, volume)
        time += duration

    # Write to file
    with open(file_name, "wb") as output_file:
        midi.writeFile(output_file)

    print(f"Music generated and saved to {file_name}")

# Example usage
generate_music("output_music.mid", genre="jazz", duration=60)
