""" This module initialises all tone data variables. Tonedata is a block of voice patch data (336 bytes) """


tone_internal = []
#print_to_console = False
def bits_to_hex(b1, b2, b3, b4, b5, b6, b7, b8):
    bits = [1 if b else 0 for b in [b1, b2, b3, b4, b5, b6, b7, b8]]  # list comprehension
    decimal = int(''.join(map(str, bits)), 2)
    return hex(decimal)


def hex_to_bits(hex_value, num_bits):
    # Convert hexidecimal value to binary string
    binary_string = bin(int(hex_value, 16))[2:].zfill(num_bits)

    # Split binary string into variables, each representing a bit
    bits = tuple(map(int, binary_string))

    # Return the variables as a tuple
    return bits


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
        # tone_internal.insert(byte_number, self.hex_value) # add byteno variable and pass as arg?




# external module phase

m4_ext_phase = True
m6_ext_phase = False
m8_ext_phase = False

byte_0 = ToneByte(0, 0, 0, 0, 0, m8_ext_phase, m6_ext_phase, m4_ext_phase)


# line, waveform ERROR IN MANUAL PAGE 9. WRONG MODULE WAVEFORM NUMBERING
lines = {"mix": (0, 0), "phase": (0, 1), "ring": (1, 1)}

line_A = "ring"
line_B = "mix"
line_C = "phase"
line_D = "ring"

line_A1, line_A2 = lines.get(line_A, (0, 0))  # default values 0
line_B1, line_B2 = lines.get(line_B, (0, 0))
line_C1, line_C2 = lines.get(line_C, (0, 0))
line_D1, line_D2 = lines.get(line_D, (0, 0))

waveforms = {"sine": (0, 0, 0),
             "saw_1": (0, 0, 1),
             "saw_2": (0, 1, 0),
             "saw_3": (0, 1, 1),
             "saw_4": (1, 0, 0),
             "saw_5": (1, 0, 1),
             "noise_1": (1, 1, 0),
             "noise_2": (1, 1, 1)}

wave_m1 = "sine"
wave_m2 = "saw_3"
wave_m3 = "noise_1"
wave_m4 = "sine"
wave_m5 = "saw_2"
wave_m6 = "saw_3"
wave_m7 = "noise_1"
wave_m8 = "saw_5"

wave_m1_1, wave_m1_2, wave_m1_3 = waveforms.get(wave_m1, (0, 0, 0))
wave_m2_1, wave_m2_2, wave_m2_3 = waveforms.get(wave_m2, (0, 0, 0))
wave_m3_1, wave_m3_2, wave_m3_3 = waveforms.get(wave_m3, (0, 0, 0))
wave_m4_1, wave_m4_2, wave_m4_3 = waveforms.get(wave_m4, (0, 0, 0))
wave_m5_1, wave_m5_2, wave_m5_3 = waveforms.get(wave_m5, (0, 0, 0))
wave_m6_1, wave_m6_2, wave_m6_3 = waveforms.get(wave_m6, (0, 0, 0))
wave_m7_1, wave_m7_2, wave_m7_3 = waveforms.get(wave_m7, (0, 0, 0))
wave_m8_1, wave_m8_2, wave_m8_3 = waveforms.get(wave_m8, (0, 0, 0))


byte_01 = ToneByte(line_A1, line_A2, wave_m2_1, wave_m2_2, wave_m2_3, wave_m1_1, wave_m1_2, wave_m1_3)
byte_02 = ToneByte(line_B1, line_B2, wave_m4_1, wave_m4_2, wave_m3_3, wave_m3_1, wave_m3_2, wave_m3_3)
byte_03 = ToneByte(line_C1, line_C2, wave_m6_1, wave_m6_2, wave_m6_3, wave_m5_1, wave_m5_2, wave_m5_3)
byte_04 = ToneByte(line_D1, line_D2, wave_m8_1, wave_m8_2, wave_m8_3, wave_m7_1, wave_m7_2, wave_m7_3)






# detuning, in pairs of bytes 5-20

m1_detune_fine = "2F"
m1_pitch_fix = True
m1_range_width = False
m1_polarity = True

fine_m1_1, fine_m1_2, fine_m1_3, fine_m1_4, fine_m1_5, fine_m1_6 = hex_to_bits(m1_detune_fine, 6)
byte_05 = ToneByte(fine_m1_1, fine_m1_2, fine_m1_3, fine_m1_4, fine_m1_5, fine_m1_6, m1_pitch_fix, m1_range_width)

m1_detune_notes = "1A"
oct_note_m1_1, oct_note_m1_2, oct_note_m1_3, oct_note_m1_4, oct_note_m1_5, oct_note_m1_6, oct_note_m1_7 = hex_to_bits(m1_detune_notes, 7)
byte_06 = ToneByte(m1_polarity, oct_note_m1_1, oct_note_m1_2, oct_note_m1_3, oct_note_m1_4, oct_note_m1_5, oct_note_m1_6, oct_note_m1_7)
byte_07 = ToneByte
byte_08 = ToneByte
byte_09 = ToneByte
byte_10 = ToneByte
byte_11 = ToneByte
byte_12 = ToneByte
byte_13 = ToneByte
byte_14 = ToneByte
byte_15 = ToneByte
byte_16 = ToneByte
byte_17 = ToneByte
byte_18 = ToneByte
byte_19 = ToneByte
byte_20 = ToneByte



ENVELOPE (PITCH, AMP) 21-164
AMP ENV END STEP, AMP SENS 165-172
PITCH END STEP 173
TOTAL LEVEL 174
A NEW(sic) ENV DEPTH, MODULE ON/OFF 175-182
PITCH ENV DEPTH, RANGE 183
LEVEL KEYBOARD FOLLOW (AMP) 184-279
LEVEL KEYBOARD FOLLOW (PITCH) 280-291
RATE KEYBOARD FOLLOW 292-303
VELOCITY SENS 304-313
VIBRATO (WAVE, MULTI), OCTAVE 314
VIBRATO DEPTH 315
VIBRATO RATE 316
VIBRATO DELAY 317
TREMOLO (WAVE, MULTI) 318
TREMOLO DEPTH 319
TREMOLO RATE 320
TREMOLO DELAY 321
VOICE NAME 322-335
CHECKSUM 336