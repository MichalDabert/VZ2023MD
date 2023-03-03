""" This module initialises all tone data variables. Tonedata is a block of voice patch data (336 bytes) """


tone_internal = []
"""
functions
"""


def bits_to_hex(b1, b2, b3, b4, b5, b6, b7, b8):
    bits = [1 if b else 0 for b in [b1, b2, b3, b4, b5, b6, b7, b8]]  # list comprehension
    decimal = int(''.join(map(str, bits)), 2)
    return hex(decimal)


def hex_to_bits(hex_value, num_bits):
    # Convert hexidecimal value to binary string
    if isinstance(hex_value, int):
        hex_value = str(hex_value)
    binary_string = bin(int(hex_value, 16))[2:].zfill(num_bits)

    # Split binary string into variables, each representing a bit
    bits = tuple(map(int, binary_string))

    # Return the variables as a tuple
    return bits

midi_notes = {

    # Octave 0
    'C0': '0C',
    'C#0': '0D',
    'D0': '0E',
    'D#0': '0F',
    'E0': '10',
    'F0': '11',
    'F#0': '12',
    'G0': '13',
    'G#0': '14',
    'A0': '15',
    'A#0': '16',
    'B0': '17',

    # Octave 1
    'C1': '18',
    'C#1': '19',
    'D1': '1A',
    'D#1': '1B',
    'E1': '1C',
    'F1': '1D',
    'F#1': '1E',
    'G1': '1F',
    'G#1': '20',
    'A1': '21',
    'A#1': '22',
    'B1': '23',

    # Octave 2
    'C2': '24',
    'C#2': '25',
    'D2': '26',
    'D#2': '27',
    'E2': '28',
    'F2': '29',
    'F#2': '2A',
    'G2': '2B',
    'G#2': '2C',
    'A2': '2D',
    'A#2': '2E',
    'B2': '2F',

    # Octave 3
    'C3': '30',
    'C#3': '31',
    'D3': '32',
    'D#3': '33',
    'E3': '34',
    'F3': '35',
    'F#3': '36',
    'G3': '37',
    'G#3': '38',
    'A3': '39',
    'A#3': '3A',
    'B3': '3B',

    # Octave 4
    'C4': '3C',
    'C#4': '3D',
    'D4': '3E',
    'D#4': '3F',
    'E4': '40',
    'F4': '41',
    'F#4': '42',
    'G4': '43',
    'G#4': '44',
    'A4': '45',
    'A#4': '46',
    'B4': '47',

    # Octave 5
    'C5': '48',
    'C#5': '49',
    'D5': '4A',
    'D#5': '4B',
    'E5': '4C',
    'F5': '4D',
    'F#5': '4E',
    'G5': '4F',
    'G#5': '50',
    'A5': '51',
    'A#5': '52',
    'B5': '53',

    # Octave 6
    'C6': '54',
    'C#6': '55',
    'D6': '56',
    'D#6': '57',
    'E6': '58',
    'F6': '59',
    'F#6': '5A',
    'G6': '5B',
    'G#6': '5C',
    'A6': '5D',
    'A#6': '5E',
    'B6': '5F',

    # Octave 7
    "C7": "60",
    "C#7": "61",
    "D7": "62",
    "D#7": "63",
    "E7": "64",
    "F7": "65",
    "F#7": "66",
    "G7": "67",
    "G#7": "68",
    "A7": "69",
    "A#7": "6A",
    "B7": "6B",

    # Octave 8
    "C8": "6C",
    "C#8": "6D",
    "D8": "6E",
    "D#8": "6F",
    "E8": "70",
    "F8": "71",
    "F#8": "72",
    "G8": "73",
    "G#8": "74",
    "A8": "75",
    "A#8": "76",
    "B8": "77",

    # Octave 9
    "C9": "78",
}

"""
classes
"""


class ToneByte:
    def __init__(self, bit_1, bit_2, bit_3, bit_4, bit_5, bit_6, bit_7, bit_8):
        self.bit_1 = bit_1
        self.bit_2 = bit_2
        self.bit_3 = bit_3
        self.bit_4 = bit_4
        self.bit_5 = bit_5
        self.bit_6 = bit_6
        self.bit_7 = bit_7
        self.bit_8 = bit_8
        self.hex_value = bits_to_hex(bit_1, bit_2, bit_3, bit_4, bit_5, bit_6, bit_7, bit_8)
        tone_internal.append(self.hex_value)
        print(self.hex_value)
        # tone_internal.insert(byte_number, self.hex_value) # add byteno variable and pass as arg?


"""
this will include Module data and voice variables (pitch, total volume, name etc)
"""


class Voice:
    def __init__(self,
                 m4_ext_phase=False, m6_ext_phase=False, m8_ext_phase=False,
                 line_a="mix", line_b="mix", line_c="mix", line_d="mix",
                 pitch_vel_rate_1=False, pitch_rate_1=0, pitch_sus_1=False, pitch_level_1=0,
                 pitch_vel_rate_2=False, pitch_rate_2=0, pitch_sus_2=False, pitch_level_2=0,
                 pitch_vel_rate_3=False, pitch_rate_3=0, pitch_sus_3=False, pitch_level_3=0,
                 pitch_vel_rate_4=False, pitch_rate_4=0, pitch_sus_4=False, pitch_level_4=0,
                 pitch_vel_rate_5=False, pitch_rate_5=0, pitch_sus_5=False, pitch_level_5=0,
                 pitch_vel_rate_6=False, pitch_rate_6=0, pitch_sus_6=False, pitch_level_6=0,
                 pitch_vel_rate_7=False, pitch_rate_7=0, pitch_sus_7=False, pitch_level_7=0,
                 pitch_vel_rate_8=False, pitch_rate_8=0, pitch_sus_8=False, pitch_level_8=0,
                 pitch_env_end=0, total_level=0, pitch_range=False,  # False/0/ Narrow
                 pitch_env_depth=0,
                 kb_follow_pitch_key_1=midi_notes["C0"], kb_follow_pitch_level_1=0,
                 kb_follow_pitch_key_2=midi_notes["C1"], kb_follow_pitch_level_2=0,
                 kb_follow_pitch_key_3=midi_notes["C2"], kb_follow_pitch_level_3=0,
                 kb_follow_pitch_key_4=midi_notes["C3"], kb_follow_pitch_level_4=0,
                 kb_follow_pitch_key_5=midi_notes["C4"], kb_follow_pitch_level_5=0,
                 kb_follow_pitch_key_6=midi_notes["C5"], kb_follow_pitch_level_6=0,
                 rate_kb_follow_key_1=midi_notes["C1"], rate_kb_follow_rate_1=0,
                 rate_kb_follow_key_2=midi_notes["C2"], rate_kb_follow_rate_2=0,
                 rate_kb_follow_key_3=midi_notes["C3"], rate_kb_follow_rate_3=0,
                 rate_kb_follow_key_4=midi_notes["C4"], rate_kb_follow_rate_4=0,
                 rate_kb_follow_key_5=midi_notes["C5"], rate_kb_follow_rate_5=0,
                 rate_kb_follow_key_6=midi_notes["C6"], rate_kb_follow_rate_6=0,
                 octave_pol=False, octave_no=0,
                 vib_multi=False,vib_wave="triangle", vib_depth=0, vib_rate=0, vib_delay=0,
                 trm_multi=False,trm_wave="triangle", trm_depth=0, trm_rate=0, trm_delay=0,
                 voice_name="initVZ2023MD"):

        self.m4_ext_phase = m4_ext_phase
        self.m6_ext_phase = m6_ext_phase
        self.m8_ext_phase = m8_ext_phase


        # line, waveform ERROR IN MANUAL PAGE 9. WRONG MODULE WAVEFORM NUMBERING
        lines = {"mix": (0, 0), "phase": (0, 1), "ring": (1, 1)}

        self.line_a1, self.line_a2 = lines.get(line_a, (0, 0))  # default values 0
        self.line_b1, self.line_b2 = lines.get(line_b, (0, 0))
        self.line_c1, self.line_c2 = lines.get(line_c, (0, 0))
        self.line_d1, self.line_d2 = lines.get(line_d, (0, 0))

        self.pitch_vel_rate_1 = pitch_vel_rate_1
        self.pitch_rate_1 = pitch_rate_1
        self.pitch_sus_1 = pitch_sus_1
        self.pitch_level_1 = pitch_level_1

        self.pitch_vel_rate_2 = pitch_vel_rate_2
        self.pitch_rate_2 = pitch_rate_2
        self.pitch_sus_2 = pitch_sus_2
        self.pitch_level_2 = pitch_level_2

        self.pitch_vel_rate_3 = pitch_vel_rate_3
        self.pitch_rate_3 = pitch_rate_3
        self.pitch_sus_3 = pitch_sus_3
        self.pitch_level_3 = pitch_level_3

        self.pitch_vel_rate_4 = pitch_vel_rate_4
        self.pitch_rate_4 = pitch_rate_4
        self.pitch_sus_4 = pitch_sus_4
        self.pitch_level_4 = pitch_level_4

        self.pitch_vel_rate_5 = pitch_vel_rate_5
        self.pitch_rate_5 = pitch_rate_5
        self.pitch_sus_5 = pitch_sus_5
        self.pitch_level_5 = pitch_level_5

        self.pitch_vel_rate_6 = pitch_vel_rate_6
        self.pitch_rate_6 = pitch_rate_6
        self.pitch_sus_6 = pitch_sus_6
        self.pitch_level_6 = pitch_level_6

        self.pitch_vel_rate_7 = pitch_vel_rate_7
        self.pitch_rate_7 = pitch_rate_7
        self.pitch_sus_7 = pitch_sus_7
        self.pitch_level_7 = pitch_level_7

        self.pitch_vel_rate_8 = pitch_vel_rate_8
        self.pitch_rate_8 = pitch_rate_8
        self.pitch_sus_8 = pitch_sus_8
        self.pitch_level_8 = pitch_level_8

        self.pitch_env_end = pitch_env_end
        self.total_level = total_level
        self.pitch_range = pitch_range
        self.pitch_env_depth = pitch_env_depth

        self.kb_follow_pitch_key_1 = kb_follow_pitch_key_1
        self.kb_follow_pitch_level_1 = kb_follow_pitch_level_1

        self.kb_follow_pitch_key_2 = kb_follow_pitch_key_2
        self.kb_follow_pitch_level_2 = kb_follow_pitch_level_2

        self.kb_follow_pitch_key_3 = kb_follow_pitch_key_3
        self.kb_follow_pitch_level_3 = kb_follow_pitch_level_3

        self.kb_follow_pitch_key_4 = kb_follow_pitch_key_4
        self.kb_follow_pitch_level_4 = kb_follow_pitch_level_4

        self.kb_follow_pitch_key_5 = kb_follow_pitch_key_5
        self.kb_follow_pitch_level_5 = kb_follow_pitch_level_5

        self.kb_follow_pitch_key_6 = kb_follow_pitch_key_6
        self.kb_follow_pitch_level_6 = kb_follow_pitch_level_6

        self.rate_kb_follow_key_1 = rate_kb_follow_key_1
        self.rate_kb_follow_rate_1 = rate_kb_follow_rate_1

        self.rate_kb_follow_key_2 = rate_kb_follow_key_2
        self.rate_kb_follow_rate_2 = rate_kb_follow_rate_2

        self.rate_kb_follow_key_3 = rate_kb_follow_key_3
        self.rate_kb_follow_rate_3 = rate_kb_follow_rate_3

        self.rate_kb_follow_key_4 = rate_kb_follow_key_4
        self.rate_kb_follow_rate_4 = rate_kb_follow_rate_4

        self.rate_kb_follow_key_5 = rate_kb_follow_key_5
        self.rate_kb_follow_rate_5 = rate_kb_follow_rate_5

        self.rate_kb_follow_key_6 = rate_kb_follow_key_6
        self.rate_kb_follow_rate_6 = rate_kb_follow_rate_6

        self.octave_pol = octave_pol
        self.octave_no = octave_no

        self.vib_multi = vib_multi
        self.vib_wave = vib_wave
        self.vib_depth = vib_depth
        self.vib_rate = vib_rate
        self.vib_delay = vib_delay

        self.trm_multi = trm_multi
        self.trm_wave = trm_wave
        self.trm_depth = trm_depth
        self.trm_rate = trm_rate
        self.trm_delay = trm_delay

        self.voice_name = voice_name




"""
reusable Module for M1~M8
"""


class Module:
    def __init__(self, waveform="sine", detune_fine=0, pitch_fix=False, range_width=False, polarity=True, detune_notes=0,
                 vel_rate_1=False, rate_1=0, sus_1=False, level_1=0,
                 vel_rate_2=False, rate_2=0, sus_2=False, level_2=0,
                 vel_rate_3=False, rate_3=0, sus_3=False, level_3=0,
                 vel_rate_4=False, rate_4=0, sus_4=False, level_4=0,
                 vel_rate_5=False, rate_5=0, sus_5=False, level_5=0,
                 vel_rate_6=False, rate_6=0, sus_6=False, level_6=0,
                 vel_rate_7=False, rate_7=0, sus_7=False, level_7=0,
                 vel_rate_8=False, rate_8=0, sus_8=False, level_8=0,
                 amp_sens=0, env_end_step=0,
                 module_active=False,  # 0/False/ = module on
                 env_depth=0,
                 kb_follow_amp_key_1=0, kb_follow_amp_level_1=0,
                 kb_follow_amp_key_2=0, kb_follow_amp_level_2=0,
                 kb_follow_amp_key_3=0, kb_follow_amp_level_3=0,
                 kb_follow_amp_key_4=0, kb_follow_amp_level_4=0,
                 kb_follow_amp_key_5=0, kb_follow_amp_level_5=0,
                 kb_follow_amp_key_6=0, kb_follow_amp_level_6=0,
                 vel_curve=0, vel_sens=0):

        self.waveform = waveform
        self.detune_fine = detune_fine
        self.pitch_fix = pitch_fix
        self.range_width = range_width
        self.polarity = polarity
        self.detune_notes = detune_notes

        self.vel_rate_1 = vel_rate_1
        self.rate_1 = rate_1
        self.sus_1 = sus_1
        self.level_1 = level_1

        self.vel_rate_2 = vel_rate_2
        self.rate_2 = rate_2
        self.sus_2 = sus_2
        self.level_2 = level_2

        self.vel_rate_3 = vel_rate_3
        self.rate_3 = rate_3
        self.sus_3 = sus_3
        self.level_3 = level_3

        self.vel_rate_4 = vel_rate_4
        self.rate_4 = rate_4
        self.sus_4 = sus_4
        self.level_4 = level_4

        self.vel_rate_5 = vel_rate_5
        self.rate_5 = rate_5
        self.sus_5 = sus_5
        self.level_5 = level_5

        self.vel_rate_6 = vel_rate_6
        self.rate_6 = rate_6
        self.sus_6 = sus_6
        self.level_6 = level_6

        self.vel_rate_7 = vel_rate_7
        self.rate_7 = rate_7
        self.sus_7 = sus_7
        self.level_7 = level_7

        self.vel_rate_8 = vel_rate_8
        self.rate_8 = rate_8
        self.sus_8 = sus_8
        self.level_8 = level_8

        self.amp_sens = amp_sens
        self.env_end_step = env_end_step

        self.module_active = module_active
        self.env_depth = env_depth

        self.kb_follow_amp_key_1 = kb_follow_amp_key_1
        self.kb_follow_amp_level_1 = kb_follow_amp_level_1

        self.kb_follow_amp_key_2 = kb_follow_amp_key_2
        self.kb_follow_amp_level_2 = kb_follow_amp_level_2

        self.kb_follow_amp_key_3 = kb_follow_amp_key_3
        self.kb_follow_amp_level_3 = kb_follow_amp_level_3

        self.kb_follow_amp_key_4 = kb_follow_amp_key_4
        self.kb_follow_amp_level_4 = kb_follow_amp_level_4

        self.kb_follow_amp_key_5 = kb_follow_amp_key_5
        self.kb_follow_amp_level_5 = kb_follow_amp_level_5

        self.kb_follow_amp_key_6 = kb_follow_amp_key_6
        self.kb_follow_amp_level_6 = kb_follow_amp_level_6

        self.vel_curve = vel_curve
        self.vel_sens = vel_sens

"""
initialized voice and 8 modules with default values
"""

voice = Voice()

m1 = Module()
m2 = Module()
m3 = Module()
m4 = Module()
m5 = Module()
m6 = Module()
m7 = Module()
m8 = Module()

"""
bytes of data formatted according to VZ-1/VZ-10m MIDI System Exclusive Format
"""

byte_0 = ToneByte(0, 0, 0, 0, 0, voice.m8_ext_phase, voice.m6_ext_phase, voice.m4_ext_phase)


waveforms = {"sine": (0, 0, 0),
             "saw_1": (0, 0, 1),
             "saw_2": (0, 1, 0),
             "saw_3": (0, 1, 1),
             "saw_4": (1, 0, 0),
             "saw_5": (1, 0, 1),
             "noise_1": (1, 1, 0),
             "noise_2": (1, 1, 1)}


wave_m1_1, wave_m1_2, wave_m1_3 = waveforms.get(m1.waveform)
wave_m2_1, wave_m2_2, wave_m2_3 = waveforms.get(m2.waveform)
wave_m3_1, wave_m3_2, wave_m3_3 = waveforms.get(m3.waveform)
wave_m4_1, wave_m4_2, wave_m4_3 = waveforms.get(m4.waveform)
wave_m5_1, wave_m5_2, wave_m5_3 = waveforms.get(m5.waveform)
wave_m6_1, wave_m6_2, wave_m6_3 = waveforms.get(m6.waveform)
wave_m7_1, wave_m7_2, wave_m7_3 = waveforms.get(m7.waveform)
wave_m8_1, wave_m8_2, wave_m8_3 = waveforms.get(m8.waveform)


byte_01 = ToneByte(voice.line_a1, voice.line_a2, wave_m2_1, wave_m2_2, wave_m2_3, wave_m1_1, wave_m1_2, wave_m1_3)

byte_02 = ToneByte(voice.line_b1, voice.line_b2, wave_m4_1, wave_m4_2, wave_m4_3, wave_m3_1, wave_m3_2, wave_m3_3)

byte_03 = ToneByte(voice.line_c1, voice.line_c2, wave_m6_1, wave_m6_2, wave_m6_3, wave_m5_1, wave_m5_2, wave_m5_3)

byte_04 = ToneByte(voice.line_d1, voice.line_d2, wave_m8_1, wave_m8_2, wave_m8_3, wave_m7_1, wave_m7_2, wave_m7_3)







# detuning, in pairs of bytes 5-20

# Module 1
fine_m1_1, fine_m1_2, fine_m1_3, fine_m1_4, fine_m1_5, fine_m1_6 = hex_to_bits(m1.detune_fine, 6)
byte_05 = ToneByte(fine_m1_1, fine_m1_2, fine_m1_3, fine_m1_4, fine_m1_5, fine_m1_6, m1.pitch_fix, m1.range_width)

octn_m1_1, octn_m1_2, octn_m1_3, octn_m1_4, octn_m1_5, octn_m1_6, octn_m1_7 = hex_to_bits(m1.detune_notes, 7)
byte_06 = ToneByte(m1.polarity, octn_m1_1, octn_m1_2, octn_m1_3, octn_m1_4, octn_m1_5, octn_m1_6, octn_m1_7)


# Module 2
fine_m2_1, fine_m2_2, fine_m2_3, fine_m2_4, fine_m2_5, fine_m2_6 = hex_to_bits(m2.detune_fine, 6)
byte_07 = ToneByte(fine_m2_1, fine_m2_2, fine_m2_3, fine_m2_4, fine_m2_5, fine_m2_6, m2.pitch_fix, m2.range_width)
octn_m2_1, octn_m2_2, octn_m2_3, octn_m2_4, octn_m2_5, octn_m2_6, octn_m2_7 = hex_to_bits(m2.detune_notes, 7)
byte_08 = ToneByte(m2.polarity, octn_m2_1, octn_m2_2, octn_m2_3, octn_m2_4, octn_m2_5, octn_m2_6, octn_m2_7)

# Module 3
fine_m3_1, fine_m3_2, fine_m3_3, fine_m3_4, fine_m3_5, fine_m3_6 = hex_to_bits(m3.detune_fine, 6)
byte_09 = ToneByte(fine_m3_1, fine_m3_2, fine_m3_3, fine_m3_4, fine_m3_5, fine_m3_6, m3.pitch_fix, m3.range_width)
octn_m3_1, octn_m3_2, octn_m3_3, octn_m3_4, octn_m3_5, octn_m3_6, octn_m3_7 = hex_to_bits(m3.detune_notes, 7)
byte_10 = ToneByte(m3.polarity, octn_m3_1, octn_m3_2, octn_m3_3, octn_m3_4, octn_m3_5, octn_m3_6, octn_m3_7)

# Module 4
fine_m4_1, fine_m4_2, fine_m4_3, fine_m4_4, fine_m4_5, fine_m4_6 = hex_to_bits(m4.detune_fine, 6)
byte_11 = ToneByte(fine_m4_1, fine_m4_2, fine_m4_3, fine_m4_4, fine_m4_5, fine_m4_6, m4.pitch_fix, m4.range_width)
octn_m4_1, octn_m4_2, octn_m4_3, octn_m4_4, octn_m4_5, octn_m4_6, octn_m4_7 = hex_to_bits(m4.detune_notes, 7)
byte_12 = ToneByte(m4.polarity, octn_m4_1, octn_m4_2, octn_m4_3, octn_m4_4, octn_m4_5, octn_m4_6, octn_m4_7)

# Module 5
fine_m5_1, fine_m5_2, fine_m5_3, fine_m5_4, fine_m5_5, fine_m5_6 = hex_to_bits(m5.detune_fine, 6)
byte_13 = ToneByte(fine_m5_1, fine_m5_2, fine_m5_3, fine_m5_4, fine_m5_5, fine_m5_6, m5.pitch_fix, m5.range_width)
octn_m5_1, octn_m5_2, octn_m5_3, octn_m5_4, octn_m5_5, octn_m5_6, octn_m5_7 = hex_to_bits(m5.detune_notes, 7)
byte_14 = ToneByte(m5.polarity, octn_m5_1, octn_m5_2, octn_m5_3, octn_m5_4, octn_m5_5, octn_m5_6, octn_m5_7)

# Module 6
fine_m6_1, fine_m6_2, fine_m6_3, fine_m6_4, fine_m6_5, fine_m6_6 = hex_to_bits(m6.detune_fine, 6)
byte_15 = ToneByte(fine_m6_1, fine_m6_2, fine_m6_3, fine_m6_4, fine_m6_5, fine_m6_6, m6.pitch_fix, m6.range_width)
octn_m6_1, octn_m6_2, octn_m6_3, octn_m6_4, octn_m6_5, octn_m6_6, octn_m6_7 = hex_to_bits(m6.detune_notes, 7)
byte_16 = ToneByte(m6.polarity, octn_m6_1, octn_m6_2, octn_m6_3, octn_m6_4, octn_m6_5, octn_m6_6, octn_m6_7)

# Module 7
fine_m7_1, fine_m7_2, fine_m7_3, fine_m7_4, fine_m7_5, fine_m7_6 = hex_to_bits(m7.detune_fine, 6)
byte_17 = ToneByte(fine_m7_1, fine_m7_2, fine_m7_3, fine_m7_4, fine_m7_5, fine_m7_6, m7.pitch_fix, m7.range_width)
octn_m7_1, octn_m7_2, octn_m7_3, octn_m7_4, octn_m7_5, octn_m7_6, octn_m7_7 = hex_to_bits(m7.detune_notes, 7)
byte_18 = ToneByte(m7.polarity, octn_m7_1, octn_m7_2, octn_m7_3, octn_m7_4, octn_m7_5, octn_m7_6, octn_m7_7)

# Module 8
fine_m8_1, fine_m8_2, fine_m8_3, fine_m8_4, fine_m8_5, fine_m8_6 = hex_to_bits(m8.detune_fine, 6)
byte_19 = ToneByte(fine_m8_1, fine_m8_2, fine_m8_3, fine_m8_4, fine_m8_5, fine_m8_6, m8.pitch_fix, m8.range_width)
octn_m8_1, octn_m8_2, octn_m8_3, octn_m8_4, octn_m8_5, octn_m8_6, octn_m8_7 = hex_to_bits(m8.detune_notes, 7)
byte_20 = ToneByte(m8.polarity, octn_m8_1, octn_m8_2, octn_m8_3, octn_m8_4, octn_m8_5, octn_m8_6, octn_m8_7)

