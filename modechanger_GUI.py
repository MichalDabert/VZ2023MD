import rtmidi
from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QComboBox

#from qt_material import apply_stylesheet


"""
establish MIDI connection
"""
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print(midiout.get_ports())

if available_ports:
    midiout.open_port(1)  # placeholder
else:
    midiout.open_virtual_port("My virtual output")

midi_channel = 0x70 # default MIDI channel 1

"""
GUI things
"""
app = QApplication()

main_window = QMainWindow()
main_window.setWindowTitle("CASIO VZ1 controller VZ2023MD")
main_window.setMinimumWidth(666)
icon = QtGui.QIcon("VZ2023MD.png")
main_window.setWindowIcon(icon)
#apply_stylesheet(app, theme='dark_red.xml')

voice_slots = {
    "normal": 40,  # Compare/Recall slot 0
    "Tone_1": 41,  # Compare/Recall slot 1
    "Tone_2": 42,  # Compare/Recall slot 2
    "Tone_3": 43,  # Compare/Recall slot 3
    "Tone_4": 44,  # Compare/Recall slot 4
}

syx_messages = {  # MIDI system exclusive
    #"tone_data"  : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x00, voice_slots["normal"], tone_data, tone_checksum, 0xF7], # default voice slot
    #"opme_data"  : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x01, voice_slots["normal"], opme_data, opme_checksum, 0xF7], # default voice slot 40 sound area ??
    #"mltch_data" : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x02, 0x00, mltch_data, mltch_checksum, 0xF7],

    "key_trnspse": {
             "G" : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x08, 0x05, 0xF7],
             "Ab": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x08, 0x03, 0xF7],
             "A" : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x08, 0x03, 0xF7],
             "Bb": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x08, 0x02, 0xF7],
             "B" : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x08, 0x01, 0xF7],
             "C" : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x00, 0x00, 0xF7],
             "C#": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x00, 0x01, 0xF7],
             "D" : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x00, 0x02, 0xF7],
             "Eb": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x00, 0x03, 0xF7],
             "E" : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x00, 0x04, 0xF7],
             "F" : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x00, 0x05, 0xF7],
             "F#": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x00, 0x06, 0xF7],
    },
    "normal_mode": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x50, 0x00, 0xF7],
    "combin_mode": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x50, 0x01, 0xF7],
    "opmemo_mode": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x50, 0x02, 0xF7],
    "multch_mode": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x50, 0x03, 0xF7],
    "multp0_mode": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x50, 0x04, 0xF7],
    "multp1_mode": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x50, 0x05, 0xF7],
    "card_bank_1": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x51, 0x00, 0xF7],
    "card_bank_2": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x51, 0x01, 0xF7],
    "card_bank_3": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x51, 0x02, 0xF7],
    "card_bank_4": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x51, 0x03, 0xF7],
    #"bend_range" : [0xF0, 0x44, 0x00, 0x00, midi_channel, 0x40, bend_range, 0xF7],
    "master_tune": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x00, 0x08, 0x05, 0xF7],  # set to standard A4=440Hz
    "open"       : {
    "int_tones"  : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x70, 0x00, 0xF7],
    "int_opmem"  : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x70, 0x01, 0xF7],
    "int_both"   : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x70, 0x00, 0xF7],
    },
    "ok"         : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x72, 0xF7],
    "error"      : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x73, 0xF7],
    }


"""
MIDI channel selector does not work yet
"""

#midi_channel_selector = QComboBox()
#midi_channel_selector.addItems([f"Channel: {i}" for i in range(1, 17)])
#midi_channel_selector.setCurrentIndex(0) # Set the default value to channel 1
#midi_channel_selector.currentIndexChanged.connect(lambda: set_midi_channel(midi_channel_selector.currentIndex()+1)) # Get user input when the value changes
# Function to set the value of the midi channel
#def set_midi_channel(channel):
#    midi_channel = hex(channel + 111) # not global!!
#    print(f"MIDI output channel:{(midi_channel)}")
#   print(syx_messages["normal_mode"])

"""
keyboard transposition selector
"""
transpose_selector = QComboBox()
transpose_selector.addItems(syx_messages["key_trnspse"])
transpose_selector.setCurrentIndex(5)  # C
key = transpose_selector.currentIndex()
transpose_selector.currentIndexChanged.connect(
    lambda index: midiout.send_message(syx_messages["key_trnspse"][transpose_selector.itemText(index)])
    # index as an arg
)


"""
Buttons
"""
master_button = QPushButton("Tune to A4=440Hz")
master_button.clicked.connect(lambda: midiout.send_message(syx_messages["master_tune"]))
normal_button = QPushButton("Normal Mode")
normal_button.clicked.connect(lambda: midiout.send_message(syx_messages["normal_mode"]))
combin_button = QPushButton("Combination Mode")
combin_button.clicked.connect(lambda: midiout.send_message(syx_messages["combin_mode"]))
opmemo_button = QPushButton("Operator Memory Mode")
opmemo_button.clicked.connect(lambda: midiout.send_message(syx_messages["opmemo_mode"]))
multch_button = QPushButton("Multi Channel Mode")
multch_button.clicked.connect(lambda: midiout.send_message(syx_messages["multch_mode"]))
multp0_button = QPushButton("Multi Channel Poly 0")
multp0_button.clicked.connect(lambda: midiout.send_message(syx_messages["multp0_mode"]))
multp1_button = QPushButton("Multi Channel Poly 1")
multp1_button.clicked.connect(lambda: midiout.send_message(syx_messages["multp1_mode"]))
card_b_1_button = QPushButton("Card Bank 1")
card_b_1_button.clicked.connect(lambda: midiout.send_message(syx_messages["card_bank_1"]))
card_b_2_button = QPushButton("Card Bank 2")
card_b_2_button.clicked.connect(lambda: midiout.send_message(syx_messages["card_bank_2"]))

"""
Voice selector
"""
bank_combo = QComboBox()
bank_combo.addItems(["Bank A", "Bank B", "Bank C", "Bank D", "Bank E", "Bank F", "Bank G", "Bank H"])
voice_combo = QComboBox()
voice_combo.addItems(["Voice 1", "Voice 2", "Voice 3", "Voice 4", "Voice 5", "Voice 6", "Voice 7", "Voice 8"])

bank_combo.currentIndexChanged.connect(lambda: send_program_change(bank_combo, voice_combo))
voice_combo.currentIndexChanged.connect(lambda: send_program_change(bank_combo, voice_combo))


def send_program_change(bank_combo, voice_combo):
    bank_index = bank_combo.currentIndex()  # Get the selected index for each combo box
    voice_index = voice_combo.currentIndex()
    value = (bank_index * 8) + voice_index # Combine the indices into a single value
    program_change = [0xC0, value]
    midiout.send_message(program_change)


"""
PySide layout
"""

main_layout = QVBoxLayout()
top_box = QVBoxLayout()
layout3 = QHBoxLayout()
layout4 = QHBoxLayout()
main_layout.addLayout(top_box)
main_layout.addLayout(layout3)
main_layout.addLayout(layout4)

#top_box.addWidget(midi_channel_selector)
top_box.addWidget(transpose_selector)
top_box.addWidget(master_button)
top_box.addWidget(normal_button)
top_box.addWidget(combin_button)
top_box.addWidget(opmemo_button)
layout3.addWidget(multch_button)
layout3.addWidget(multp0_button)
layout3.addWidget(multp1_button)
layout4.addWidget(card_b_1_button)
layout4.addWidget(card_b_2_button)
top_box.addWidget(bank_combo)
top_box.addWidget(voice_combo)
central_widget = QWidget()
central_widget.setLayout(main_layout)
main_window.setCentralWidget(central_widget)
main_window.show()
app.exec()
