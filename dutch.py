from midiutil import MIDIFile
import random

# Fungsi untuk membuat melodi Dutch

def add_dutch_melody(track, midi, channel=0):
    # Dutch house menggunakan nada tinggi dan pola ritmis
    dutch_scale = [60, 62, 64, 67, 69, 72, 74, 76]  # C major scale dengan aksen tinggi

    start_time = 0
    duration = 0.5  # Setengah ketukan untuk groove house

    for _ in range(16):  # Membuat 16 not untuk pola melodi house
        note = random.choice(dutch_scale)  # Pilih not acak dari skala
        velocity = random.randint(100, 127)  # Dinamika kuat untuk energi tinggi
        midi.addNote(track, channel, note, start_time, duration, velocity)
        start_time += duration

# Membuat file MIDI baru
midi = MIDIFile(1)  # 1 track untuk melodi

# Menambahkan track
midi.addTrackName(0, 0, "Dutch Melody")
midi.addTempo(0, 0, 128)  # Tempo khas Dutch house (128 BPM)

# Tambahkan melodi Dutch
add_dutch_melody(0, midi)

# Simpan ke file MIDI
with open("dutch_melody.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("File MIDI 'dutch_melody.mid' berhasil dibuat!")
