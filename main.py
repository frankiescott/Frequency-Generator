import math
import struct
import wave

def make_soundfile(freq=440, data_size=10000, file_name="test.wav"):
    frate = 44100.0
    amp = 8000.0

    sine_list = []
    for x in range(data_size):
        sine_list.append(math.sin(2 * math.pi * freq * (x / frate)))

    wav_file = wave.open(file_name, "w")
    comptype = "NONE"
    compname = "not compressed"

    wav_file.setparams((1, 2, frate, data_size, "NONE", "not compressed"))
    for s in sine_list:
        wav_file.writeframes(struct.pack('h', int(s * amp / 2)))
    wav_file.close()

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
hz = 440
set = []
for i in range(0, 9):
    for j in range(0, 12):
        set.append([notes[j] + str(i)])

set[57].append(hz)
for i in range(58, len(set)):
    set[i].append(hz * pow(1.059463, i - 57))

for i in range(0, 57):
    set[i].append(hz * pow(1.059463, -(57 - i)))

for i in range(0, len(set)):
    make_soundfile(int(set[i][1]), 40000, set[i][0] + ".wav")
