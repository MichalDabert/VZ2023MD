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
    binary_string = bin(int(hex_value, 16))[2:].zfill(num_bits)

    # Split binary string into variables, each representing a bit
    bits = tuple(map(int, binary_string))

    # Return the variables as a tuple
    return bits

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
        # tone_internal.insert(byte_number, self.hex_value) # add byteno variable and pass as arg?


"""
this will include Module data and voice variables (pitch, total volume, name etc)
"""


class Voice:
    def __init__(self,
                 m4_ext_phase, m6_ext_phase, m8_ext_phase,
                 line_a, line_b, line_c, line_d,
                 pitch_vel_rate_1, pitch_rate_1, pitch_sus_1, pitch_level_1,
                 pitch_vel_rate_2, pitch_rate_2, pitch_sus_2, pitch_level_2,
                 pitch_vel_rate_3, pitch_rate_3, pitch_sus_3, pitch_level_3,
                 pitch_vel_rate_4, pitch_rate_4, pitch_sus_4, pitch_level_4,
                 pitch_vel_rate_5, pitch_rate_5, pitch_sus_5, pitch_level_5,
                 pitch_vel_rate_6, pitch_rate_6, pitch_sus_6, pitch_level_6,
                 pitch_vel_rate_7, pitch_rate_7, pitch_sus_7, pitch_level_7,
                 pitch_vel_rate_8, pitch_rate_8, pitch_sus_8, pitch_level_8,
                 pitch_env_end, total_level, pitch_range, pitch_env_depth,
                 kb_follow_pitch_key_1, kb_follow_pitch_level_1,
                 kb_follow_pitch_key_2, kb_follow_pitch_level_2,
                 kb_follow_pitch_key_3, kb_follow_pitch_level_3,
                 kb_follow_pitch_key_4, kb_follow_pitch_level_4,
                 kb_follow_pitch_key_5, kb_follow_pitch_level_5,
                 kb_follow_pitch_key_6, kb_follow_pitch_level_6,
                 rate_kb_follow_key_1, rate_kb_follow_rate_1,
                 rate_kb_follow_key_2, rate_kb_follow_rate_2,
                 rate_kb_follow_key_3, rate_kb_follow_rate_3,
                 rate_kb_follow_key_4, rate_kb_follow_rate_4,
                 rate_kb_follow_key_5, rate_kb_follow_rate_5,
                 rate_kb_follow_key_6, rate_kb_follow_rate_6,
                 octave_pol, octave_no,
                 vib_multi,vib_wave, vib_depth, vib_rate, vib_delay,
                 trm_multi,trm_wave, trm_depth, trm_rate, trm_delay,
                 voice_name):

        self.m4_ext_phase = m4_ext_phase
        self.m6_ext_phase = m6_ext_phase
        self.m8_ext_phase = m8_ext_phase


        # line, waveform ERROR IN MANUAL PAGE 9. WRONG MODULE WAVEFORM NUMBERING
        lines = {"mix": (0, 0), "phase": (0, 1), "ring": (1, 1)}

        line_a1, line_a2 = lines.get(line_a, (0, 0))  # default values 0
        line_b1, line_b2 = lines.get(line_b, (0, 0))
        line_c1, line_c2 = lines.get(line_c, (0, 0))
        line_d1, line_d2 = lines.get(line_d, (0, 0))

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
    def __init__(self, waveform, detune_fine, pitch_fix, range_width, polarity, detune_notes,
                 vel_rate_1, rate_1, sus_1, level_1, vel_rate_2, rate_2, sus_2, level_2,
                 vel_rate_3, rate_3, sus_3, level_3, vel_rate_4, rate_4, sus_4, level_4,
                 vel_rate_5, rate_5, sus_5, level_5, vel_rate_6, rate_6, sus_6, level_6,
                 vel_rate_7, rate_7, sus_7, level_7, vel_rate_8, rate_8, sus_8, level_8,
                 amp_sens, env_end_step, module_active, env_depth,
                 kb_follow_amp_key_1, kb_follow_amp_level_1,
                 kb_follow_amp_key_2, kb_follow_amp_level_2,
                 kb_follow_amp_key_3, kb_follow_amp_level_3,
                 kb_follow_amp_key_4, kb_follow_amp_level_4,
                 kb_follow_amp_key_5, kb_follow_amp_level_5,
                 kb_follow_amp_key_6, kb_follow_amp_level_6,
                 vel_curve, vel_sens):

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


byte_0 = ToneByte(0, 0, 0, 0, 0, m8_ext_phase, m6_ext_phase, m4_ext_phase)




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


byte_01 = ToneByte(line_a1, line_a2, wave_m2_1, wave_m2_2, wave_m2_3, wave_m1_1, wave_m1_2, wave_m1_3)
byte_02 = ToneByte(line_b1, line_b2, wave_m4_1, wave_m4_2, wave_m3_3, wave_m3_1, wave_m3_2, wave_m3_3)
byte_03 = ToneByte(line_c1, line_c2, wave_m6_1, wave_m6_2, wave_m6_3, wave_m5_1, wave_m5_2, wave_m5_3)
byte_04 = ToneByte(line_d1, line_d2, wave_m8_1, wave_m8_2, wave_m8_3, wave_m7_1, wave_m7_2, wave_m7_3)






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
