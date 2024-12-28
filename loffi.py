from midiutil import MIDIFile
import random

# Fungsi untuk membuat melodi lo-fi

def add_lofi_melody(track, midi, channel=0):
    # Lo-fi sering menggunakan skala minor dan pola yang santai
    lofi_scale = [60, 62, 63, 65, 67, 68, 70, 72]  # C natural minor scale

    start_time = 0
    duration = random.choice([0.5, 1, 1.5])  # Durasi variatif untuk vibe santai

    for _ in range(12):  # Membuat 12 not untuk melodi sederhana
        note = random.choice(lofi_scale)  # Pilih not acak dari skala
        velocity = random.randint(60, 80)  # Dinamika lembut untuk lo-fi
        midi.addNote(track, channel, note, start_time, duration, velocity)
        start_time += duration

# Membuat file MIDI baru
midi = MIDIFile(1)  # 1 track untuk melodi

# Menambahkan track
midi.addTrackName(0, 0, "Lo-Fi Melody")
midi.addTempo(0, 0, 70)  # Tempo khas lo-fi (70 BPM)

# Tambahkan melodi lo-fi
add_lofi_melody(0, midi)

# Simpan ke file MIDI
with open("lofi_melody.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("File MIDI 'lofi_melody.mid' berhasil dibuat!")
