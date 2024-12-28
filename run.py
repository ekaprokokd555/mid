from midiutil import MIDIFile
import random

# Fungsi untuk membuat melodi bebas genre

def add_random_melody(track, midi, channel=0, num_notes=16, scale=None):
    if scale is None:
        scale = [60, 62, 64, 65, 67, 69, 71, 72]  # Default: C major scale

    start_time = 0
    duration = 1  # Durasi setiap not

    for _ in range(num_notes):
        note = random.choice(scale)  # Pilih not acak dari skala
        velocity = random.randint(70, 110)  # Dinamika acak
        midi.addNote(track, channel, note, start_time, duration, velocity)
        start_time += duration

# Membuat file MIDI baru
midi = MIDIFile(1)  # 1 track untuk melodi

# Menambahkan track
midi.addTrackName(0, 0, "Random Melody")
midi.addTempo(0, 0, 120)  # Tempo 120 BPM

# Tambahkan melodi acak
add_random_melody(0, midi)

# Simpan ke file MIDI
with open("random_melody.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("File MIDI 'random_melody.mid' berhasil dibuat!")
