try:
    from PyQt4.QtGui import *
except:
    from PyQt5.QtWidgets import *

class RadioButtonWidget(QWidget):
    """this class creates a group of radio buttons from a given list of labels"""

    #constructor
    def __init__(self,label,instruction,button_list):
        super().__init__() #call the super class constructor

        #create widget components
        self.title_label = QLabel(label)
        self.radio_group_box = QGroupBox(instruction)
        self.radio_button_group = QButtonGroup()

        #create the radio buttons
        self.radio_button_list = []
        for each in button_list:
            self.radio_button_list.append(QRadioButton(each))

        #set the default checked item
        self.radio_button_list[0].setChecked(True) 

        #create layout for radio buttons and add them
        self.radio_button_layout = QVBoxLayout()
        
        #add button to layout and button group
        counter = 1
        for each in self.radio_button_list:
            self.radio_button_layout.addWidget(each)
            self.radio_button_group.addButton(each)
            self.radio_button_group.setId(each,counter)
            counter += 1

        #add radio buttons to group box
        self.radio_group_box.setLayout(self.radio_button_layout)

        #create layout for whole widget
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.radio_group_box)
        self.setLayout(self.main_layout)

    def selected_button(self):
        return self.radio_button_group.checkedId()