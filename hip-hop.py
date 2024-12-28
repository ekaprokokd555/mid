from midiutil import MIDIFile
import random

# Fungsi untuk membuat melodi hip-hop

def add_hiphop_melody(track, midi, channel=0):
    # Hip-hop menggunakan pentatonik minor atau not bernada rendah
    hiphop_scale = [60, 63, 65, 67, 70, 72, 75]  # C minor pentatonic scale

    start_time = 0
    duration = 0.5  # Durasi setiap not (setengah ketukan untuk groove)

    for _ in range(16):  # Membuat 16 not
        note = random.choice(hiphop_scale)  # Pilih not acak dari skala
        velocity = random.randint(80, 100)  # Dinamika khas hip-hop
        midi.addNote(track, channel, note, start_time, duration, velocity)
        start_time += duration

# Membuat file MIDI baru
midi = MIDIFile(1)  # 1 track untuk melodi

# Menambahkan track
midi.addTrackName(0, 0, "Hip-Hop Melody")
midi.addTempo(0, 0, 90)  # Tempo khas hip-hop (90 BPM)

# Tambahkan melodi hip-hop
add_hiphop_melody(0, midi)

# Simpan ke file MIDI
with open("hiphop_melody.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("File MIDI 'hiphop_melody.mid' berhasil dibuat!")
