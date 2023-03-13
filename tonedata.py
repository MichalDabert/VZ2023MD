""" This module includes functions for handling Voice and Module variables and combines them into a tone_internal list
    of 333 bytes of voice patch data, 2 bytes of data equal to 0x20, and a checksum """


tone_internal = []
for i in range(337):
    """
    initializes a list of bytes.
    """
    byte_num = str(i).zfill(2)
    byte_x = "byte_" + byte_num
    tone_internal.append(byte_x)
print(tone_internal)

"""
functions
"""


def ascii_to_hex(s):
    """
        Takes a string of up to 12 characters and returns their ascii values in hexadecimal format.
        Pads the remaining character slots with zeroes.

        Args:
            s (string): a string of up to 12 characters

        Returns:
            list: a list of ascii values in hexadecimal format
        """
    hex_values = []
    for char in range(12):
        if char < len(s):
            hex_values.append(hex(ord(s[char])))
        else:
            hex_values.append(hex(0))
    return hex_values



def calculate_checksum(sysex_data):
    """
    Calculates 7 bit checksum.

    Args:
        sysex_data (list): a list of hexadecimal values

    Returns:
        hex: hexadecimal checksum
    """
    new_checksum = 0
    for i in range(0, len(sysex_data), 2):
        new_checksum += int(sysex_data[i], 16) * 16 + int(sysex_data[i + 1], 16)
    return (128 - new_checksum % 128) % 128



def bits_to_hex(b1, b2, b3, b4, b5, b6, b7, b8):
    """
    Calculates the hex value of 8 bits of data.

    Args:
        b1 (int): The first bit.
        ~
        b8 (int): The las number bit.

    Returns:
        hex: The hex value of arguments as bits
    """
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
A dictionary that contains hex values of of notes.

Keys:
    -  (str): The name of the note

Values:
    -  (str): The hexadecimal value of the note.

"""

"""
classes
"""


class ToneByte:
    """A class that creates a byte of VZ1 MIDI System Exclusive tone data."""
    def __init__(self, bit_1, bit_2, bit_3, bit_4, bit_5, bit_6, bit_7, bit_8, index):
        """
        Initializes a new instance of the ToneByte class.

        Args:
            bit_1 to bit_8: internal structure of tone data.
            index: byte's position in the syx_messages["tone_data"].
        """
        self.bit_1 = bit_1
        self.bit_2 = bit_2
        self.bit_3 = bit_3
        self.bit_4 = bit_4
        self.bit_5 = bit_5
        self.bit_6 = bit_6
        self.bit_7 = bit_7
        self.bit_8 = bit_8
        self.hex_value = bits_to_hex(bit_1, bit_2, bit_3, bit_4, bit_5, bit_6, bit_7, bit_8)

        tone_internal[index] = self.hex_value
        # print(self.hex_value)
        # tone_internal.insert(byte_number, self.hex_value) # add byteno variable and pass as arg?


class KbFollow:
    """A class that represents 6 keyboard follow points."""
    def __init__(self,
                 p1_key=midi_notes["C0"], p1_level=0,
                 p2_key=midi_notes["C1"], p2_level=0,
                 p3_key=midi_notes["C2"], p3_level=0,
                 p4_key=midi_notes["C3"], p4_level=0,
                 p5_key=midi_notes["C4"], p5_level=0,
                 p6_key=midi_notes["C5"], p6_level=0):
        self.p1_key = p1_key
        self.p1_level = p1_level
        self.p2_key = p2_key
        self.p2_level = p2_level
        self.p3_key = p3_key
        self.p3_level = p3_level
        self.p4_key = p4_key
        self.p4_level = p4_level
        self.p5_key = p5_key
        self.p5_level = p5_level
        self.p6_key = p6_key
        self.p6_level = p6_level


class Voice:
    """A class that represents tone parameters not governed by Modules."""
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
                 pitch_env_end=0, total_level=0, pitch_curve=0, pitch_vel_sens=0,
                 rate_vel_curve=0, rate_vel_sens=0, pitch_range=False,  # False/0/ Narrow
                 pitch_env_depth=0,
                 octave_pol=False, octave_no=0,
                 vib_multi=False, vib_wave="triangle", vib_depth=0, vib_rate=0, vib_delay=0,
                 trm_multi=False, trm_wave="triangle", trm_depth=0, trm_rate=0, trm_delay=0,
                 voice_name="initVZ2023MD"):
        """
        Initializes a new instance of init tone of 8 sine waves, output mixed, max level, no release.

        Args:
            line_a etc.: Modules are grouped into 4 lines a~d.
            m4_ext_phase etc.: Modules m4, m6, and m8 may have their phase distorted by the line above.
        """

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

        self.pitch_curve = pitch_curve
        self.pitch_vel_sens = pitch_vel_sens

        self.rate_vel_curve = rate_vel_curve
        self.rate_vel_sens = rate_vel_sens
        self.pitch_range = pitch_range
        self.pitch_env_depth = pitch_env_depth

        self.kb_follow_pitch = KbFollow()
        self.kb_follow_mod_rate = KbFollow()

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


class Module:
    def __init__(self, waveform="sine",
                 detune_fine=0,
                 pitch_fix=False, range_width=False, polarity=True,
                 detune_notes=0,
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
                 vel_curve=0, vel_sens=0,):

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

        self.level_kb_follow = KbFollow()


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


level_kbfollow_amp = KbFollow()
level_kbfollow_pitch = KbFollow()
rate_kbfollow = KbFollow()

"""
bytes of data formatted according to VZ-1/VZ-10m MIDI System Exclusive Format
"""

byte_0 = ToneByte(0, 0, 0, 0, 0, voice.m8_ext_phase, voice.m6_ext_phase, voice.m4_ext_phase, 0)


waveforms = {"sine": (0, 0, 0),
             "saw_1": (0, 0, 1),
             "saw_2": (0, 1, 0),
             "saw_3": (0, 1, 1),
             "saw_4": (1, 0, 0),
             "saw_5": (1, 0, 1),
             "noise_1": (1, 1, 0),
             "noise_2": (1, 1, 1),
             "triangle": (0, 0),
             "saw_up": (0, 1),
             "saw_down": (1, 0),
             "square": (1, 1), }


wave_m1_1, wave_m1_2, wave_m1_3 = waveforms.get(m1.waveform)
wave_m2_1, wave_m2_2, wave_m2_3 = waveforms.get(m2.waveform)
wave_m3_1, wave_m3_2, wave_m3_3 = waveforms.get(m3.waveform)
wave_m4_1, wave_m4_2, wave_m4_3 = waveforms.get(m4.waveform)
wave_m5_1, wave_m5_2, wave_m5_3 = waveforms.get(m5.waveform)
wave_m6_1, wave_m6_2, wave_m6_3 = waveforms.get(m6.waveform)
wave_m7_1, wave_m7_2, wave_m7_3 = waveforms.get(m7.waveform)
wave_m8_1, wave_m8_2, wave_m8_3 = waveforms.get(m8.waveform)


byte_01 = ToneByte(voice.line_a1, voice.line_a2, wave_m2_1, wave_m2_2, wave_m2_3, wave_m1_1, wave_m1_2, wave_m1_3, 1)

byte_02 = ToneByte(voice.line_b1, voice.line_b2, wave_m4_1, wave_m4_2, wave_m4_3, wave_m3_1, wave_m3_2, wave_m3_3, 2)

byte_03 = ToneByte(voice.line_c1, voice.line_c2, wave_m6_1, wave_m6_2, wave_m6_3, wave_m5_1, wave_m5_2, wave_m5_3, 3)

byte_04 = ToneByte(voice.line_d1, voice.line_d2, wave_m8_1, wave_m8_2, wave_m8_3, wave_m7_1, wave_m7_2, wave_m7_3, 4)

# detune, in pairs of bytes 5-20

# Module 1
fine_m1_1, fine_m1_2, fine_m1_3, fine_m1_4, fine_m1_5, fine_m1_6 = hex_to_bits(m1.detune_fine, 6)
byte_05 = ToneByte(fine_m1_1, fine_m1_2, fine_m1_3, fine_m1_4, fine_m1_5, fine_m1_6, m1.pitch_fix, m1.range_width, 5)
octn_m1_1, octn_m1_2, octn_m1_3, octn_m1_4, octn_m1_5, octn_m1_6, octn_m1_7 = hex_to_bits(m1.detune_notes, 7)
byte_06 = ToneByte(m1.polarity, octn_m1_1, octn_m1_2, octn_m1_3, octn_m1_4, octn_m1_5, octn_m1_6, octn_m1_7, 6)


# Module 2
fine_m2_1, fine_m2_2, fine_m2_3, fine_m2_4, fine_m2_5, fine_m2_6 = hex_to_bits(m2.detune_fine, 6)
byte_07 = ToneByte(fine_m2_1, fine_m2_2, fine_m2_3, fine_m2_4, fine_m2_5, fine_m2_6, m2.pitch_fix, m2.range_width, 7)
octn_m2_1, octn_m2_2, octn_m2_3, octn_m2_4, octn_m2_5, octn_m2_6, octn_m2_7 = hex_to_bits(m2.detune_notes, 7)
byte_08 = ToneByte(m2.polarity, octn_m2_1, octn_m2_2, octn_m2_3, octn_m2_4, octn_m2_5, octn_m2_6, octn_m2_7, 8)

# Module 3
fine_m3_1, fine_m3_2, fine_m3_3, fine_m3_4, fine_m3_5, fine_m3_6 = hex_to_bits(m3.detune_fine, 6)
byte_09 = ToneByte(fine_m3_1, fine_m3_2, fine_m3_3, fine_m3_4, fine_m3_5, fine_m3_6, m3.pitch_fix, m3.range_width, 9)
octn_m3_1, octn_m3_2, octn_m3_3, octn_m3_4, octn_m3_5, octn_m3_6, octn_m3_7 = hex_to_bits(m3.detune_notes, 7)
byte_10 = ToneByte(m3.polarity, octn_m3_1, octn_m3_2, octn_m3_3, octn_m3_4, octn_m3_5, octn_m3_6, octn_m3_7, 10)

# Module 4
fine_m4_1, fine_m4_2, fine_m4_3, fine_m4_4, fine_m4_5, fine_m4_6 = hex_to_bits(m4.detune_fine, 6)
byte_11 = ToneByte(fine_m4_1, fine_m4_2, fine_m4_3, fine_m4_4, fine_m4_5, fine_m4_6, m4.pitch_fix, m4.range_width, 11)
octn_m4_1, octn_m4_2, octn_m4_3, octn_m4_4, octn_m4_5, octn_m4_6, octn_m4_7 = hex_to_bits(m4.detune_notes, 7)
byte_12 = ToneByte(m4.polarity, octn_m4_1, octn_m4_2, octn_m4_3, octn_m4_4, octn_m4_5, octn_m4_6, octn_m4_7, 12)

# Module 5
fine_m5_1, fine_m5_2, fine_m5_3, fine_m5_4, fine_m5_5, fine_m5_6 = hex_to_bits(m5.detune_fine, 6)
byte_13 = ToneByte(fine_m5_1, fine_m5_2, fine_m5_3, fine_m5_4, fine_m5_5, fine_m5_6, m5.pitch_fix, m5.range_width, 13)
octn_m5_1, octn_m5_2, octn_m5_3, octn_m5_4, octn_m5_5, octn_m5_6, octn_m5_7 = hex_to_bits(m5.detune_notes, 7)
byte_14 = ToneByte(m5.polarity, octn_m5_1, octn_m5_2, octn_m5_3, octn_m5_4, octn_m5_5, octn_m5_6, octn_m5_7, 14)

# Module 6
fine_m6_1, fine_m6_2, fine_m6_3, fine_m6_4, fine_m6_5, fine_m6_6 = hex_to_bits(m6.detune_fine, 6)
byte_15 = ToneByte(fine_m6_1, fine_m6_2, fine_m6_3, fine_m6_4, fine_m6_5, fine_m6_6, m6.pitch_fix, m6.range_width, 15)
octn_m6_1, octn_m6_2, octn_m6_3, octn_m6_4, octn_m6_5, octn_m6_6, octn_m6_7 = hex_to_bits(m6.detune_notes, 7)
byte_16 = ToneByte(m6.polarity, octn_m6_1, octn_m6_2, octn_m6_3, octn_m6_4, octn_m6_5, octn_m6_6, octn_m6_7, 16)

# Module 7
fine_m7_1, fine_m7_2, fine_m7_3, fine_m7_4, fine_m7_5, fine_m7_6 = hex_to_bits(m7.detune_fine, 6)
byte_17 = ToneByte(fine_m7_1, fine_m7_2, fine_m7_3, fine_m7_4, fine_m7_5, fine_m7_6, m7.pitch_fix, m7.range_width, 17)
octn_m7_1, octn_m7_2, octn_m7_3, octn_m7_4, octn_m7_5, octn_m7_6, octn_m7_7 = hex_to_bits(m7.detune_notes, 7)
byte_18 = ToneByte(m7.polarity, octn_m7_1, octn_m7_2, octn_m7_3, octn_m7_4, octn_m7_5, octn_m7_6, octn_m7_7, 18)

# Module 8
fine_m8_1, fine_m8_2, fine_m8_3, fine_m8_4, fine_m8_5, fine_m8_6 = hex_to_bits(m8.detune_fine, 6)
byte_19 = ToneByte(fine_m8_1, fine_m8_2, fine_m8_3, fine_m8_4, fine_m8_5, fine_m8_6, m8.pitch_fix, m8.range_width, 19)
octn_m8_1, octn_m8_2, octn_m8_3, octn_m8_4, octn_m8_5, octn_m8_6, octn_m8_7 = hex_to_bits(m8.detune_notes, 7)
byte_20 = ToneByte(m8.polarity, octn_m8_1, octn_m8_2, octn_m8_3, octn_m8_4, octn_m8_5, octn_m8_6, octn_m8_7, 20)


m1.rate_1 = "1A"
m2.rate_1 = "1B"
m3.rate_1 = "1C"
m4.rate_1 = "1D"
m5.rate_1 = "1E"
m6.rate_1 = "1F"
m6.rate_1 = "12"
m8.rate_1 = "13"


modules = [m1, m2, m3, m4, m5, m6, m7, m8]
# ar = amp rate bit
# pr = pitch rate bit
# al = amp level bit
# pl = pitch level bit

# bytes 21~28 amp rate 1
for i, module in enumerate(modules, start=21):
    ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7 = hex_to_bits(module.rate_1, 7)
    byte_x = ToneByte(module.vel_rate_1, ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7, i)

#  byte 29 pitch rate 1
pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7 = hex_to_bits(voice.pitch_rate_1, 7)
byte_29 = ToneByte(voice.pitch_vel_rate_1, pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7, 29)

# bytes 30~37 amp level 1
for i, module in enumerate(modules, start=30):
    al_1, al_2, al_3, al_4, al_5, al_6, al_7 = hex_to_bits(module.level_1, 7)
    byte_x = ToneByte(module.sus_1, al_1, al_2, al_3, al_4, al_5, al_6, al_7, i)

# byte 38 pitch level 1
pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7 = hex_to_bits(voice.pitch_level_1, 7)
byte_38 = ToneByte(voice.pitch_sus_1, pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7, 38)

# bytes 39~46 amp rate 2
for i, module in enumerate(modules, start=39):
    ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7 = hex_to_bits(module.rate_2, 7)
    byte_x = ToneByte(module.vel_rate_2, ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7, i)

# byte 47 pitch rate 2
pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7 = hex_to_bits(voice.pitch_rate_2, 7)
byte_47 = ToneByte(voice.pitch_vel_rate_2, pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7, 47)

# bytes 48~55  amp level 2
for i, module in enumerate(modules, start=48):
    al_1, al_2, al_3, al_4, al_5, al_6, al_7 = hex_to_bits(module.level_2, 7)
    byte_x = ToneByte(module.sus_2, al_1, al_2, al_3, al_4, al_5, al_6, al_7, i)

# byte 56 pitch level 2
pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7 = hex_to_bits(voice.pitch_level_2, 7)
byte_56 = ToneByte(voice.pitch_sus_2, pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7, 56)

# bytes 57~64 amp rate 3
for i, module in enumerate(modules, start=57):
    ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7 = hex_to_bits(module.rate_3, 7)
    byte_x = ToneByte(module.vel_rate_3, ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7, i)

#  byte 65 pitch rate 3
pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7 = hex_to_bits(voice.pitch_rate_3, 7)
byte_65 = ToneByte(voice.pitch_vel_rate_3, pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7, 65)

# bytes 66~73 amp level 3
for i, module in enumerate(modules, start=66):
    al_1, al_2, al_3, al_4, al_5, al_6, al_7 = hex_to_bits(module.level_3, 7)
    byte_x = ToneByte(module.sus_3, al_1, al_2, al_3, al_4, al_5, al_6, al_7, i)

# byte 74 pitch level 3
pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7 = hex_to_bits(voice.pitch_level_3, 7)
byte_74 = ToneByte(voice.pitch_sus_3, pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7, 74)


# bytes 75~82 amp rate 4
for i, module in enumerate(modules, start=75):
    ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7 = hex_to_bits(module.rate_4, 7)
    byte_x = ToneByte(module.vel_rate_4, ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7, i)

# byte 83 pitch rate 4
pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7 = hex_to_bits(voice.pitch_rate_4, 7)
byte_47 = ToneByte(voice.pitch_vel_rate_4, pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7, 83)

# bytes 84~91  amp level 4
for i, module in enumerate(modules, start=84):
    al_1, al_2, al_3, al_4, al_5, al_6, al_7 = hex_to_bits(module.level_4, 7)
    byte_x = ToneByte(module.sus_4, al_1, al_2, al_3, al_4, al_5, al_6, al_7, i)

# byte 92 pitch level 4
pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7 = hex_to_bits(voice.pitch_level_4, 7)
byte_92 = ToneByte(voice.pitch_sus_4, pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7, 92)

# bytes 93~100 amp rate 5
for i, module in enumerate(modules, start=93):
    ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7 = hex_to_bits(module.rate_5, 7)
    byte_x = ToneByte(module.vel_rate_5, ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7, i)

# byte 101 pitch rate 5
pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7 = hex_to_bits(voice.pitch_rate_5, 7)
byte_101 = ToneByte(voice.pitch_vel_rate_5, pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7, 101)

# bytes 102~109 amp level 5
for i, module in enumerate(modules, start=102):
    al_1, al_2, al_3, al_4, al_5, al_6, al_7 = hex_to_bits(module.level_5, 7)
    byte_x = ToneByte(module.sus_5, al_1, al_2, al_3, al_4, al_5, al_6, al_7, i)

# byte 110 pitch level 5
pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7 = hex_to_bits(voice.pitch_level_5, 7)
byte_110 = ToneByte(voice.pitch_sus_5, pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7, 110)

# bytes 111~118 amp rate 6
for i, module in enumerate(modules, start=111):
    ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7 = hex_to_bits(module.rate_6, 7)
    byte_x = ToneByte(module.vel_rate_6, ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7, i)

# byte 119 pitch rate 6
pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7 = hex_to_bits(voice.pitch_rate_6, 7)
byte_119 = ToneByte(voice.pitch_vel_rate_6, pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7, 119)

# bytes 120~127 amp level 6
for i, module in enumerate(modules, start=120):
    al_1, al_2, al_3, al_4, al_5, al_6, al_7 = hex_to_bits(module.level_6, 7)
    byte_x = ToneByte(module.sus_6, al_1, al_2, al_3, al_4, al_5, al_6, al_7, i)

# byte 128 pitch level 6
pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7 = hex_to_bits(voice.pitch_level_6, 7)
byte_128 = ToneByte(voice.pitch_sus_6, pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7, 128)

# bytes 129~136 amp rate 7
for i, module in enumerate(modules, start=129):
    ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7 = hex_to_bits(module.rate_7, 7)
    byte_x = ToneByte(module.vel_rate_7, ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7, i)

#  byte 137 pitch rate 7
pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7 = hex_to_bits(voice.pitch_rate_7, 7)
byte_137 = ToneByte(voice.pitch_vel_rate_7, pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7, 137)

# bytes 138~145 amp level 7
for i, module in enumerate(modules, start=138):
    al_1, al_2, al_3, al_4, al_5, al_6, al_7 = hex_to_bits(module.level_7, 7)
    byte_x = ToneByte(module.sus_7, al_1, al_2, al_3, al_4, al_5, al_6, al_7, i)

# byte 146 pitch level 7
pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7 = hex_to_bits(voice.pitch_level_7, 7)
byte_146 = ToneByte(voice.pitch_sus_7, pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7, 146)

# bytes 147~154 amp rate 8
for i, module in enumerate(modules, start=147):
    ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7 = hex_to_bits(module.rate_8, 7)
    byte_x = ToneByte(module.vel_rate_8, ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7, i)

#  byte 155 pitch rate 8
pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7 = hex_to_bits(voice.pitch_rate_8, 7)
byte_155 = ToneByte(voice.pitch_vel_rate_8, pr_1, pr_2, pr_3, pr_4, pr_5, pr_6, pr_7, 155)

# bytes 156~163 amp level 8
for i, module in enumerate(modules, start=156):
    al_1, al_2, al_3, al_4, al_5, al_6, al_7 = hex_to_bits(module.level_8, 7)
    byte_x = ToneByte(module.sus_8, al_1, al_2, al_3, al_4, al_5, al_6, al_7, i)

# byte 164 pitch level 8
pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7 = hex_to_bits(voice.pitch_level_8, 7)
byte_164 = ToneByte(voice.pitch_sus_8, pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7, 164)

# bytes 165~172 amp envelope end step, amp sens
for i, module in enumerate(modules, start=165):
    env_end_step_1, env_end_step_2, env_end_step_3 = hex_to_bits(module.env_end_step, 3)
    amp_sens_1, amp_sens_2, amp_sens_3 = hex_to_bits(module.amp_sens, 3)
    byte_x = ToneByte(0, env_end_step_1, env_end_step_2, env_end_step_3, 0, amp_sens_1, amp_sens_2, amp_sens_3, i)

# byte_173 pitch end step
pitch_env_end_1, pitch_env_end_2, pitch_env_end_3 = hex_to_bits(voice.pitch_env_end, 3)
byte_173 = ToneByte(0, pitch_env_end_1, pitch_env_end_2, pitch_env_end_3, 0, 0, 0, 0, 173)

# byte_174 total level
total_1, total_2, total_3, total_4, total_5, total_6,  total_7 = hex_to_bits(voice.total_level, 7)
byte_174 = ToneByte(0, total_1, total_2, total_3, total_4, total_5, total_6, total_7, 174)

# bytes 175~182 amp env depth, module on/off
for i, module in enumerate(modules, start=175):
    envd_1, envd_2, envd_3, envd_4, envd_5, envd_6, envd_7 = hex_to_bits(module.env_depth, 7)
    byte_x = ToneByte(module.module_active, envd_1, envd_2, envd_3, envd_4, envd_5, envd_6, envd_7, i)

# byte 183 pitch env depth and range
p_env_d_1, p_env_d_2, p_env_d_3, p_env_d_4, p_env_d_5, p_env_d_6 = hex_to_bits(voice.pitch_env_depth, 6)
byte_183 = ToneByte(voice.pitch_range, 0, p_env_d_1, p_env_d_2, p_env_d_3, p_env_d_4, p_env_d_5, p_env_d_6, 183)


 #bytes 184~279 keyboard follow - amp level

# Module 1
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m1.level_kb_follow.p1_key, 7)
byte_184 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 184)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m1.level_kb_follow.p1_level, 7)
byte_185 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 185)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m1.level_kb_follow.p2_key, 7)
byte_186 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 186)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m1.level_kb_follow.p2_level, 7)
byte_187 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 187)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m1.level_kb_follow.p3_key, 7)
byte_188 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 188)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m1.level_kb_follow.p3_level, 7)
byte_189 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 189)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m1.level_kb_follow.p4_key, 7)
byte_190 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 190)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m1.level_kb_follow.p4_level, 7)
byte_191 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 191)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m1.level_kb_follow.p5_key, 7)
byte_192 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 192)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m1.level_kb_follow.p5_level, 7)
byte_193 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 193)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m1.level_kb_follow.p6_key, 7)
byte_194 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 194)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m1.level_kb_follow.p6_level, 7)
byte_195 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 195)

# Module 2
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m2.level_kb_follow.p1_key, 7)
byte_196 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 196)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m2.level_kb_follow.p1_level, 7)
byte_197 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 197)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m2.level_kb_follow.p2_key, 7)
byte_198 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 198)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m2.level_kb_follow.p2_level, 7)
byte_199 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 199)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m2.level_kb_follow.p3_key, 7)
byte_200 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 200)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m2.level_kb_follow.p3_level, 7)
byte_201 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 201)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m2.level_kb_follow.p4_key, 7)
byte_202 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 202)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m2.level_kb_follow.p4_level, 7)
byte_203 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 203)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m2.level_kb_follow.p5_key, 7)
byte_204 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 204)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m2.level_kb_follow.p5_level, 7)
byte_205 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 205)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m2.level_kb_follow.p6_key, 7)
byte_206 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 206)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m2.level_kb_follow.p6_level, 7)
byte_207 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 207)

# Module 3
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m3.level_kb_follow.p1_key, 7)
byte_208 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 208)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m3.level_kb_follow.p1_level, 7)
byte_209 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 209)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m3.level_kb_follow.p2_key, 7)
byte_210 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 210)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m3.level_kb_follow.p2_level, 7)
byte_211 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 211)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m3.level_kb_follow.p3_key, 7)
byte_212 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 212)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m3.level_kb_follow.p3_level, 7)
byte_213 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 213)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m3.level_kb_follow.p4_key, 7)
byte_214 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 214)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m3.level_kb_follow.p4_level, 7)
byte_215 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 215)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m3.level_kb_follow.p5_key, 7)
byte_216 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 216)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m3.level_kb_follow.p5_level, 7)
byte_217 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 217)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m3.level_kb_follow.p6_key, 7)
byte_218 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 218)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m3.level_kb_follow.p6_level, 7)
byte_219 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 219)

# Module 4
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m4.level_kb_follow.p1_key, 7)
byte_220 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 220)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m4.level_kb_follow.p1_level, 7)
byte_221 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 221)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m4.level_kb_follow.p2_key, 7)
byte_222 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 222)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m4.level_kb_follow.p2_level, 7)
byte_223 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 223)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m4.level_kb_follow.p3_key, 7)
byte_224 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 224)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m4.level_kb_follow.p3_level, 7)
byte_225 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 225)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m4.level_kb_follow.p4_key, 7)
byte_226 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 226)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m4.level_kb_follow.p4_level, 7)
byte_227 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 227)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m4.level_kb_follow.p5_key, 7)
byte_228 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 228)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m4.level_kb_follow.p5_level, 7)
byte_229 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 229)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m4.level_kb_follow.p6_key, 7)
byte_230 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 230)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m4.level_kb_follow.p6_level, 7)
byte_231 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 231)

# Module 5
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m5.level_kb_follow.p1_key, 7)
byte_232 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 232)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m5.level_kb_follow.p1_level, 7)
byte_233 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 233)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m5.level_kb_follow.p2_key, 7)
byte_234 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 234)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m5.level_kb_follow.p2_level, 7)
byte_235 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 235)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m5.level_kb_follow.p3_key, 7)
byte_236 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 236)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m5.level_kb_follow.p3_level, 7)
byte_237 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 237)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m5.level_kb_follow.p4_key, 7)
byte_238 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 238)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m5.level_kb_follow.p4_level, 7)
byte_239 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 239)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m5.level_kb_follow.p5_key, 7)
byte_240 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 240)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m5.level_kb_follow.p5_level, 7)
byte_241 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 241)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m5.level_kb_follow.p6_key, 7)
byte_242 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 242)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m5.level_kb_follow.p6_level, 7)
byte_243 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 243)

# Module 6
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m6.level_kb_follow.p1_key, 7)
byte_244 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 244)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m6.level_kb_follow.p1_level, 7)
byte_245 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 245)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m6.level_kb_follow.p2_key, 7)
byte_246 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 246)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m6.level_kb_follow.p2_level, 7)
byte_247 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 247)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m6.level_kb_follow.p3_key, 7)
byte_248 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 248)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m6.level_kb_follow.p3_level, 7)
byte_249 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 249)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m6.level_kb_follow.p4_key, 7)
byte_250 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 250)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m6.level_kb_follow.p4_level, 7)
byte_251 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 251)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m6.level_kb_follow.p5_key, 7)
byte_252 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 252)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m6.level_kb_follow.p5_level, 7)
byte_253 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 253)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m6.level_kb_follow.p6_key, 7)
byte_254 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 254)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m6.level_kb_follow.p6_level, 7)
byte_255 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 255)

# Module 7
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m7.level_kb_follow.p1_key, 7)
byte_256 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 256)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m7.level_kb_follow.p1_level, 7)
byte_257 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 257)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m7.level_kb_follow.p2_key, 7)
byte_258 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 258)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m7.level_kb_follow.p2_level, 7)
byte_259 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 259)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m7.level_kb_follow.p3_key, 7)
byte_260 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 260)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m7.level_kb_follow.p3_level, 7)
byte_261 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 261)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m7.level_kb_follow.p4_key, 7)
byte_262 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 262)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m7.level_kb_follow.p4_level, 7)
byte_263 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 263)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m7.level_kb_follow.p5_key, 7)
byte_264 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 264)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m7.level_kb_follow.p5_level, 7)
byte_265 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 265)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m7.level_kb_follow.p6_key, 7)
byte_266 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 266)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m7.level_kb_follow.p6_level, 7)
byte_267 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 267)

# Module 8
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m8.level_kb_follow.p1_key, 7)
byte_268 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 268)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m8.level_kb_follow.p1_level, 7)
byte_269 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 269)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m8.level_kb_follow.p2_key, 7)
byte_270 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 270)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m8.level_kb_follow.p2_level, 7)
byte_271 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 271)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m8.level_kb_follow.p3_key, 7)
byte_272 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 272)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m8.level_kb_follow.p3_level, 7)
byte_273 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 273)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m8.level_kb_follow.p4_key, 7)
byte_274 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 274)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m8.level_kb_follow.p4_level, 7)
byte_275 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 275)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m8.level_kb_follow.p5_key, 7)
byte_276 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 276)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m8.level_kb_follow.p5_level, 7)
byte_277 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 277)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m8.level_kb_follow.p6_key, 7)
byte_278 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 278)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(m8.level_kb_follow.p6_level, 7)
byte_279 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 279)

#bytes 280~291 keyboard follow - pitch level
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_pitch.p1_key, 7)
byte_280 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 280)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_pitch.p1_level, 7)
byte_281 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 281)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_pitch.p2_key, 7)
byte_282 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 282)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_pitch.p2_level, 7)
byte_283 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 283)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_pitch.p3_key, 7)
byte_284 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 284)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_pitch.p3_level, 7)
byte_285 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 285)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_pitch.p4_key, 7)
byte_286 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 286)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_pitch.p4_level, 7)
byte_287 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 287)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_pitch.p5_key, 7)
byte_288 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 288)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_pitch.p5_level, 7)
byte_289 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 289)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_pitch.p6_key, 7)
byte_290 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 290)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_pitch.p6_level, 7)
byte_291 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 291)

#bytes 292~303 keyboard follow - rate
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_mod_rate.p1_key, 7)
byte_292 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 292)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_mod_rate.p1_level, 7)
byte_293 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 293)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_mod_rate.p2_key, 7)
byte_294 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 294)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_mod_rate.p2_level, 7)
byte_295 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 295)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_mod_rate.p3_key, 7)
byte_296 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 296)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_mod_rate.p3_level, 7)
byte_297 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 297)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_mod_rate.p4_key, 7)
byte_298 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 298)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_mod_rate.p4_level, 7)
byte_299 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 299)


b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_mod_rate.p5_key, 7)
byte_300 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 300)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_mod_rate.p5_level, 7)
byte_301 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 301)

b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_mod_rate.p6_key, 7)
byte_302 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 302)
b1, b2, b3, b4, b5, b6, b7 = hex_to_bits(voice.kb_follow_mod_rate.p6_level, 7)
byte_303 = ToneByte(0, b1, b2, b3, b4, b5, b6, b7, 303)


# bytes 304~311 velocity sensitivity
for i, module in enumerate(modules, start=304):
    curve_1, curve_2, curve_3 = hex_to_bits(module.vel_curve, 3)
    vel_sens_1, vel_sens_2, vel_sens_3, vel_sens_4, vel_sens_5 = hex_to_bits(module.vel_sens, 5)
    byte_x = ToneByte(curve_1, curve_2, curve_3, vel_sens_1, vel_sens_2, vel_sens_3, vel_sens_4, vel_sens_5, i)

# byte 312 pitch velocity curve, sense
curve_1, curve_2, curve_3 = hex_to_bits(voice.pitch_curve, 3)
vel_sens_1, vel_sens_2, vel_sens_3, vel_sens_4, vel_sens_5 = hex_to_bits(voice.pitch_vel_sens, 5)
byte_312 = ToneByte(curve_1, curve_2, curve_3, vel_sens_1, vel_sens_2, vel_sens_3, vel_sens_4, vel_sens_5, 312)

# byte 313 rate of pitch velocity curve, sense
curve_1, curve_2, curve_3 = hex_to_bits(voice.rate_vel_curve, 3)
vel_sens_1, vel_sens_2, vel_sens_3, vel_sens_4, vel_sens_5 = hex_to_bits(voice.rate_vel_sens, 5)
byte_313 = ToneByte(curve_1, curve_2, curve_3, vel_sens_1, vel_sens_2, vel_sens_3, vel_sens_4, vel_sens_5, 313)

# byte_314 vibrato, tone octave
octave_1, octave_2 = hex_to_bits(voice.octave_no, 2)
vib_wave_1, vib_wave_2 = waveforms.get(voice.vib_wave)
byte_314 = ToneByte(voice.octave_pol, octave_1, octave_2, 0, voice.vib_multi, 0, vib_wave_1, vib_wave_2, 314)

# byte_315 vibrato depth
vib_dpth_1, vib_dpth_2, vib_dpth_3, vib_dpth_4, vib_dpth_5, vib_dpth_6,  vib_dpth_7 = hex_to_bits(voice.vib_depth, 7)
byte_315 = ToneByte(0, vib_dpth_1, vib_dpth_2, vib_dpth_3, vib_dpth_4, vib_dpth_5, vib_dpth_6, vib_dpth_7, 315)

# byte_316 vibrato rate
vib_rte_1, vib_rte_2, vib_rte_3, vib_rte_4, vib_rte_5, vib_rte_6,  vib_rte_7 = hex_to_bits(voice.vib_rate, 7)
byte_316 = ToneByte(0, vib_rte_1, vib_rte_2, vib_rte_3, vib_rte_4, vib_rte_5, vib_rte_6, vib_rte_7, 316)

# byte_317 vibrato delay
vib_dly_1, vib_dly_2, vib_dly_3, vib_dly_4, vib_dly_5, vib_dly_6,  vib_dly_7 = hex_to_bits(voice.vib_delay, 7)
byte_317 = ToneByte(0, vib_dly_1, vib_dly_2, vib_dly_3, vib_dly_4, vib_dly_5, vib_dly_6, vib_dly_7, 317)

# byte_318 tremolo wave, multi
trm_wave_1, trm_wave_2,  = waveforms.get(voice.trm_wave)
byte_318 = ToneByte(0, 0, 0, 0, voice.trm_multi, 0,  trm_wave_1, trm_wave_2, 318)

# byte_319 tremolo depth
trm_dpth_1, trm_dpth_2, trm_dpth_3, trm_dpth_4, trm_dpth_5, trm_dpth_6,  trm_dpth_7 = hex_to_bits(voice.trm_depth, 7)
byte_319 = ToneByte(0, trm_dpth_1, trm_dpth_2, trm_dpth_3, trm_dpth_4, trm_dpth_5, trm_dpth_6, trm_dpth_7, 319)

# byte_320 tremolo rate
trm_rte_1, trm_rte_2, trm_rte_3, trm_rte_4, trm_rte_5, trm_rte_6,  trm_rte_7 = hex_to_bits(voice.trm_rate, 7)
byte_320 = ToneByte(0, trm_rte_1, trm_rte_2, trm_rte_3, trm_rte_4, trm_rte_5, trm_rte_6, trm_rte_7, 320)

# byte_321 tremolo delay
trm_dly_1, trm_dly_2, trm_dly_3, trm_dly_4, trm_dly_5, trm_dly_6,  trm_dly_7 = hex_to_bits(voice.trm_delay, 7)
byte_321 = ToneByte(0, trm_dly_1, trm_dly_2, trm_dly_3, trm_dly_4, trm_dly_5, trm_dly_6, trm_dly_7, 321)

# bytes 322~333 voice name
c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11, c_12, = ascii_to_hex(voice.voice_name)

for i, c in enumerate([c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11, c_12], start=322):
    l1, l2, l3, l4, l5, l6, l7, l8 = hex_to_bits(c, 8)
    byte = ToneByte(l1, l2, l3, l4, l5, l6, l7, l8, i)
    byte_name = f'byte_{i}'
    locals()[byte_name] = byte

# byte 334, 335: spacebars
byte_334 = ToneByte(0, 0, 1, 0, 0, 0, 0, 0, 334)
byte_335 = ToneByte(0, 0, 1, 0, 0, 0, 0, 0, 335)


# byte 336 checksum
tone_checksum = calculate_checksum(tone_internal[:-1])
chsm_1, chsm_2, chsm_3, chsm_4, chsm_5, chsm_6,  chsm_7, = hex_to_bits(tone_checksum, 7)
byte_336 = ToneByte(0, chsm_1, chsm_2, chsm_3, chsm_4, chsm_5, chsm_6,  chsm_7, 336)
print(tone_internal)
print("tone internal length:", len(tone_internal))
print("checksum:", tone_checksum)

for data in tone_internal:
    data = int(data, 16)
    #print(type(data))

