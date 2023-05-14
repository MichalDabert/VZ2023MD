import rtmidi
from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QComboBox, \
    QSlider, QLabel, QDialog, QCheckBox, QMenu
import tonedata



"""
Dialog to establish MIDI connection, select channel
"""


class MidiPortDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.midiout = rtmidi.MidiOut()
        self.setWindowTitle("Select MIDI Port")
        self.setFixedSize(300, 100)

        self.port_combo = QComboBox()
        self.update_ports()
        self.port_combo.currentIndexChanged.connect(self.port_selected)

        self.midi_channel_selector = QComboBox()
        self.midi_channel_selector.addItems([f"Channel: {i}" for i in range(1, 17)])
        self.midi_channel_selector.setCurrentIndex(0)  # Set the default value to channel 1
        self.midi_channel_selector.currentIndexChanged.connect(self.set_midi_channel)

        self.open_button = QPushButton("Open Port")
        self.open_button.clicked.connect(self.open_port)

        layout = QVBoxLayout()
        layout.addWidget(self.port_combo)
        layout.addWidget(self.midi_channel_selector)
        layout.addWidget(self.open_button)
        self.setLayout(layout)

    def update_ports(self):
        available_ports = self.midiout.get_ports()
        self.port_combo.clear()
        self.port_combo.addItems(available_ports)
        if "Microsoft GS Wavetable Synth 0" in available_ports:
            # Get the current index of the QComboBox
            current_index = self.port_combo.currentIndex()

            # next index if the current index is "Microsoft GS Wavetable Synth 0"
            if self.port_combo.currentText() == "Microsoft GS Wavetable Synth 0":
                self.port_combo.setCurrentIndex(current_index + 1)

    def port_selected(self, index):
        self.selected_port = self.port_combo.currentText()

    def set_midi_channel(self, index):
        self.selected_midich = self.midi_channel_selector.currentIndex() + 112
        print(f"MIDI output channel: {self.selected_midich}")

    def open_port(self):
        available_ports = self.midiout.get_ports()
        if available_ports:
            selected_index = self.port_combo.currentIndex()
            self.midiout.open_port(selected_index)
        else:
            self.midiout.open_virtual_port("My virtual output")

        self.accept()

    """
    MIDI channel selector
    """


"""
GUI things
"""

app = QApplication()
dialog = MidiPortDialog()
dialog.setWindowFlags(Qt.WindowStaysOnTopHint)
dialog.exec()
main_window = QMainWindow()

main_window.setWindowTitle("CASIO VZ1 controller VZ2023MD")
main_window.setMinimumWidth(666)
icon = QtGui.QIcon("VZ2023MD.png")
main_window.setWindowIcon(icon)

try:
    midi_channel = dialog.selected_midich
except AttributeError:
    midi_channel = 112

bend_range = 0x04  # default four semitones

voice_slots = {
    "normal": 0x40,  # Compare/Recall slot 0
    "Tone_1": 0x41,  # Compare/Recall slot 1
    "Tone_2": 0x42,  # Compare/Recall slot 2
    "Tone_3": 0x43,  # Compare/Recall slot 3
    "Tone_4": 0x44,  # Compare/Recall slot 4
}

syx_messages = {  # MIDI system exclusive
    "tone_data"  : [0xF0, 0x44, 0x03, 0x00, 0x70, 0x00, 0x40],
    #"opme_data"  : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x01, voice_slots["normal"], opme_data, opme_checksum, 0xF7], # default voice slot 40 sound area ??
    #"mltch_data" : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x02, 0x00, mltch_data, mltch_checksum, 0xF7],

    "key_trnspse": {
             "G" : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x08, 0x05, 0xF7],
             "Ab": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x01, 0x08, 0x04, 0xF7],
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
    "bend_range" : [0xF0, 0x44, 0x00, 0x00, midi_channel, 0x40, bend_range, 0xF7],
    "master_tune": [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x40, 0x00, 0x08, 0x05, 0xF7],  # set to standard A4=440Hz
    "open"       : {
    "int_tones"  : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x70, 0x00, 0xF7],
    "int_opmem"  : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x70, 0x01, 0xF7],
    "int_both"   : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x70, 0x00, 0xF7],
    },
    "ok"         : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x72, 0xF7],
    "error"      : [0xF0, 0x44, 0x03, 0x00, midi_channel, 0x73, 0xF7],
    }

def update_tone_data():
    syx_messages["tone_data"] = [0xF0, 0x44, 0x03, 0x00, 0x70, 0x00, 0x40]
    syx_messages["tone_data"].extend(tonedata.tone_internal)
    syx_messages["tone_data"].append(0xF7)
    print(f"tone_data updated. Checksum: {tonedata.tone_internal[672]}")

update_tone_data()

"""
bend range slider
"""


def update_bend_range_value():
    syx_messages["bend_range"][6] = bend_slider.value()


def update_bend_label_text(value):
    common_interval_names = {
        0: "perfect unison",
        1: "minor second",
        2: "major second",
        3: "minor third",
        4: "major third",
        5: "perfect fourth",
        7: "perfect fifth",
        8: "minor sixth",
        9: "major sixth",
        10: "minor seventh",
        11: "major seventh",
        12: "perfect octave",
        14: "minor ninth",
        15: "major ninth",
        16: "minor tenth",
        17: "major tenth",
        19: "perfect eleventh",
        20: "augmented eleventh",
        21: "perfect twelfth",
        23: "minor thirteenth",
        24: "major thirteenth",
        26: "minor fourteenth",
        27: "major fourteenth",
        28: "perfect octave",
        31: "minor seventeenth",
        32: "major seventeenth",
        33: "perfect eighteenth",
        36: "perfect fifth",
        48: "perfect octave"
    }

    if value in common_interval_names:
        bend_label.setText(common_interval_names[value].title())
    else:
        bend_label.setText(str(value) + " semitones")


bend_slider = QSlider(Qt.Horizontal)
bend_slider.setRange(0, 48)
bend_slider.setTickInterval(1)
bend_slider.setTickPosition(QSlider.TicksBelow)
bend_slider.valueChanged.connect(update_bend_label_text)
bend_slider.valueChanged.connect(update_bend_range_value)
bend_slider.valueChanged.connect(lambda: dialog.midiout.send_message(syx_messages["bend_range"]))
bend_slider.valueChanged.connect(lambda: print(syx_messages["bend_range"]))
bend_label = QLabel('Set bend range')
bend_label.setAlignment(Qt.AlignHCenter)


"""
keyboard transposition selector
"""
transpose_selector = QComboBox()
transpose_selector.addItems(syx_messages["key_trnspse"])
transpose_selector.setMaxVisibleItems(transpose_selector.count())
transpose_selector.setCurrentIndex(5)  # C
key = transpose_selector.currentIndex()
transpose_selector.currentIndexChanged.connect(
    lambda index: dialog.midiout.send_message(syx_messages["key_trnspse"][transpose_selector.itemText(index)])
)

"""
SYSEX sender
"""


def send_syx(message):
    dialog.midiout.send_message(syx_messages[message])
    print(message)



"""
Buttons
"""

button_height = 50

tone_button = QPushButton("Send Tone")
tone_button.clicked.connect(lambda: send_syx("tone_data"))

master_button = QPushButton("Tune to A4=440Hz")
master_button.clicked.connect(lambda: send_syx("master_tune"))

normal_button = QPushButton("Normal Mode")
normal_button.setMinimumHeight(button_height)
normal_button.clicked.connect(lambda: send_syx("normal_mode"))

combin_button = QPushButton("Combination Mode")
combin_button.setMinimumHeight(button_height)
combin_button.clicked.connect(lambda: send_syx("combin_mode"))

opmemo_button = QPushButton("Operation Memory Mode")
opmemo_button.setMinimumHeight(button_height)
opmemo_button.clicked.connect(lambda: send_syx("opmemo_mode"))

multch_button = QPushButton("Multi Channel Mode")
multch_button.clicked.connect(lambda: send_syx("multch_mode"))

multp0_button = QPushButton("Multi Channel Poly 0")
multp0_button.clicked.connect(lambda: send_syx("multp0_mode"))

multp1_button = QPushButton("Multi Channel Poly 1")
multp1_button.clicked.connect(lambda: send_syx("multp1_mode"))

card_b_1_button = QPushButton("Card Bank 1")
card_b_1_button.clicked.connect(lambda: send_syx("card_bank_1"))

card_b_2_button = QPushButton("Card Bank 2")
card_b_2_button.clicked.connect(lambda: send_syx("card_bank_2"))


"""
Voice selector
"""
bank_combo = QComboBox()
bank_combo.addItems(["Bank A", "Bank B", "Bank C", "Bank D", "Bank E", "Bank F", "Bank G", "Bank H"])
voice_combo = QComboBox()
voice_combo.addItems(["Voice 1", "Voice 2", "Voice 3", "Voice 4", "Voice 5", "Voice 6", "Voice 7", "Voice 8"])

bank_combo.currentIndexChanged.connect(lambda: send_program_change(bank_combo, voice_combo))
voice_combo.currentIndexChanged.connect(lambda: send_program_change(bank_combo, voice_combo))



def update_variable():
    tonedata.process_voicedata()
    tonedata.generate_checksum()
    update_tone_data()


class ToggleSwitch(QWidget):
    def __init__(self, variable_name, initial_state):
        super().__init__()

        self.variable_name = variable_name
        self.state = initial_state

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.toggle = QCheckBox(f"{self.variable_name} = {self.state}")
        self.toggle.setChecked(self.state)  # Set the initial state

        layout.addWidget(self.toggle)
        self.setLayout(layout)

        # Connect the stateChanged signal to a custom function
        self.toggle.stateChanged.connect(self.onStateChanged)

    def onStateChanged(self, state):
        self.state = bool(state)
        setattr(tonedata.voice, self.variable_name, self.state)
        print(f"Switch state changed: {self.variable_name} = {self.state}")
        update_variable()

def send_program_change(bank_combo, voice_combo):
    bank_index = bank_combo.currentIndex()  # Get the selected index for each combo box
    voice_index = voice_combo.currentIndex()
    value = (bank_index * 8) + voice_index  # Combine the indices into a single value
    program_change = [0xC0, value]
    dialog.midiout.send_message(program_change)


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


toggles = []
toggle_variables = ["m4_ext_phase", "m6_ext_phase", "m8_ext_phase"]

for variable in toggle_variables:
    initial_state = getattr(tonedata.voice, variable)
    toggle = ToggleSwitch(variable, initial_state)
    toggles.append(toggle)
    top_box.addWidget(toggle)


top_box.addWidget(transpose_selector)
top_box.addWidget(bend_slider)
top_box.addWidget(bend_label)
top_box.addWidget(tone_button)
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
