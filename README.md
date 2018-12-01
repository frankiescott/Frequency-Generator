# Frequency Generator

Generates a wav file for each musical note frequency.


p1.py
p2.py
p5.py
p6.py
p7.py
p8.py
main.py
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
1
2
3
4
5
6
25
26
27
28
29
30
31
32
33
34
35
36
37
    amp = 8000.0
 
    sine_list = []
    for x in range(data_size):
        sine_list.append(math.sin(2 * math.pi * freq * (x / frate)))
 
    wav_file = wave.open(file_name, "w")
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
import math
import struct
import wave
 
def make_soundfile(freq, data_size, file_name):
    frate = 44100.0
 
set[57].append(hz)
for i in range(58, len(set)):
    set[i].append(hz * pow(1.059463, i - 57))
 
for i in range(0, 57):
    set[i].append(hz * pow(1.059463, -(57 - i)))
 
for i in range(0, len(set)):
    print("`" + set[i][0] + "\t" + str("%.2f" % set[i][1]) + "hz`")
#for i in range(0, len(set)):
    #make_soundfile(int(set[i][1]), 40000, set[i][0] + ".wav")
 

                                                                                                                                                           
Python - main.py:34
`C0	16.35hz`
`C#0	17.32hz`
`D0	18.35hz`
`D#0	19.45hz`
`E0	20.60hz`
`F0	21.83hz`
`F#0	23.12hz`
`G0	24.50hz`
`G#0	25.96hz`
`A0	27.50hz`
`A#0	29.14hz`
`B0	30.87hz`
`C1	32.70hz`
`C#1	34.65hz`
`D1	36.71hz`
`D#1	38.89hz`
`E1	41.20hz`
`F1	43.65hz`
`F#1	46.25hz`
`G1	49.00hz`
`G#1	51.91hz`
`A1	55.00hz`
`A#1	58.27hz`
`B1	61.74hz`
`C2	65.41hz`
`C#2	69.30hz`
`D2	73.42hz`
`D#2	77.78hz`
`E2	82.41hz`
`F2	87.31hz`
`F#2	92.50hz`
`G2	98.00hz`
`G#2	103.83hz`
`A2	110.00hz`
`A#2	116.54hz`
`B2	123.47hz`
`C3	130.81hz`
`C#3	138.59hz`
`D3	146.83hz`
`D#3	155.56hz`
`E3	164.81hz`
`F3	174.61hz`
`F#3	185.00hz`
`G3	196.00hz`
`G#3	207.65hz`
`A3	220.00hz`
`A#3	233.08hz`
`B3	246.94hz`
`C4	261.63hz`
`C#4	277.18hz`
`D4	293.66hz`
`D#4	311.13hz`
`E4	329.63hz`
`F4	349.23hz`
`F#4	369.99hz`
`G4	392.00hz`
`G#4	415.30hz`
`A4	440.00hz`
`A#4	466.16hz`
`B4	493.88hz`
`C5	523.25hz`
`C#5	554.37hz`
`D5	587.33hz`
`D#5	622.25hz`
`E5	659.25hz`
`F5	698.46hz`
`F#5	739.99hz`
`G5	783.99hz`
`G#5	830.61hz`
`A5	880.00hz`
`A#5	932.33hz`
`B5	987.77hz`
`C6	1046.50hz`
`C#6	1108.73hz`
`D6	1174.66hz`
`D#6	1244.51hz`
`E6	1318.51hz`
`F6	1396.91hz`
`F#6	1479.97hz`
`G6	1567.98hz`
`G#6	1661.22hz`
`A6	1760.00hz`
`A#6	1864.65hz`
`B6	1975.53hz`
`C7	2093.00hz`
`C#7	2217.46hz`
`D7	2349.31hz`
`D#7	2489.01hz`
`E7	2637.01hz`
`F7	2793.82hz`
`F#7	2959.95hz`
`G7	3135.95hz`
`G#7	3322.43hz`
`A7	3519.99hz`
`A#7	3729.30hz`
`B7	3951.05hz`
`C8	4185.99hz`
`C#8	4434.91hz`
`D8	4698.62hz`
`D#8	4978.01hz`
`E8	5274.02hz`
`F8	5587.63hz`
`F#8	5919.89hz`
`G8	6271.90hz`
`G#8	6644.85hz`
`A8	7039.97hz`
`A#8	7458.59hz`
`B8	7902.10hz`
