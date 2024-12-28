from midiutil import MIDIFile
import random

# Fungsi untuk membuat melodi House

def add_house_melody(track, midi, channel=0):
    # House menggunakan nada sederhana dengan pola berulang
    house_scale = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale

    start_time = 0
    duration = 0.5  # Setengah ketukan untuk pola groove

    for _ in range(16):  # Membuat 16 not berulang
        note = random.choice(house_scale)  # Pilih not acak dari skala
        velocity = random.randint(90, 110)  # Dinamika konsisten untuk groove
        midi.addNote(track, channel, note, start_time, duration, velocity)
        start_time += duration

# Membuat file MIDI baru
midi = MIDIFile(1)  # 1 track untuk melodi

# Menambahkan track
midi.addTrackName(0, 0, "House Melody")
midi.addTempo(0, 0, 125)  # Tempo khas House (125 BPM)

# Tambahkan melodi House
add_house_melody(0, midi)

# Simpan ke file MIDI
with open("house_melody.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("File MIDI 'house_melody.mid' berhasil dibuat!")
