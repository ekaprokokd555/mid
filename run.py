from midiutil import MIDIFile

# Fungsi untuk menambahkan melodi

def add_melody(track, midi, channel=0):
    melody_notes = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale
    start_time = 0
    duration = 1  # Durasi setiap not
    for note in melody_notes:
        midi.addNote(track, channel, note, start_time, duration, 100)
        start_time += duration

# Membuat file MIDI baru
midi = MIDIFile(1)  # 1 track untuk melodi

# Menambahkan track
midi.addTrackName(0, 0, "Melody")
midi.addTempo(0, 0, 120)  # Tempo 120 BPM

# Tambahkan melodi
add_melody(0, midi)

# Simpan ke file MIDI
with open("melody_music.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("File MIDI 'melody_music.mid' berhasil dibuat!")
