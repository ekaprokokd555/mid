from midiutil import MIDIFile
import random

# Fungsi untuk membuat melodi breakbeat

def add_breakbeat_melody(track, midi, channel=0):
    # Breakbeat menggunakan pola cepat dengan variasi nada
    breakbeat_scale = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale

    start_time = 0
    duration = 0.25  # Durasi setiap not (seperempat ketukan untuk pola cepat)

    for _ in range(32):  # Membuat 32 not untuk pola intens
        note = random.choice(breakbeat_scale)  # Pilih not acak dari skala
        velocity = random.randint(90, 120)  # Dinamika kuat untuk energi
        midi.addNote(track, channel, note, start_time, duration, velocity)
        start_time += duration

# Membuat file MIDI baru
midi = MIDIFile(1)  # 1 track untuk melodi

# Menambahkan track
midi.addTrackName(0, 0, "Breakbeat Melody")
midi.addTempo(0, 0, 140)  # Tempo khas breakbeat (140 BPM)

# Tambahkan melodi breakbeat
add_breakbeat_melody(0, midi)

# Simpan ke file MIDI
with open("breakbeat_melody.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("File MIDI 'breakbeat_melody.mid' berhasil dibuat!")
