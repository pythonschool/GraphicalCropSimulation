try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *

from radio_button_widget import * #provides the radio button widget
from manual_grow_dialog_class import * #provides the manual grow dialog window class
from crop_view_class import * #provides the graphical crop status display

from wheat_class import * 
from potato_class import *

import sys
import random

class CropWindow(QMainWindow):
    """this class creates a main window to observe the growth of a simulated crop"""

    #constructor
    def __init__(self):
        super().__init__() #call super class constructor
        self.setWindowTitle("Crop Simulator") #set window title

        self.create_select_crop_layout() #create the initial layout to choose the crop type

        self.stackedLayout = QStackedLayout() #this holds the various layouts this window needs
        self.stackedLayout.addWidget(self.select_crop_widget)

        #set the central widget to display the layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.central_widget)



    def create_select_crop_layout(self):
        #this is the initial layout of the window - to select the crop type

        self.crop_radio_buttons = RadioButtonWidget("Crop Simulation","Please select a crop",("Wheat","Potato")) #create crop selector 
        self.instantiate_button = QPushButton('Create Crop')

        #create layout to hold the widgets
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        #create a widget to display the layout
        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)

        #connections
        self.instantiate_button.clicked.connect(self.instantiate_crop)

    def create_view_crop_layout(self,crop_type):
        #this is the second layout of the window - view the crop growth

        self.growth_label = QLabel("Growth")
        self.days_label = QLabel("Days Growing")
        self.status_label = QLabel("Crop Status")

        self.growth_line_edit = QLineEdit()
        self.days_line_edit = QLineEdit()
        self.status_line_edit = QLineEdit()

        if crop_type == 1:
            self.crop_view = WheatView() #create a view to display graphical status of crop
        elif crop_type == 2:
            self.crop_view = PotatoView()

        #ensure the crop view appears a certain size
        self.crop_view.setHorizontalScrollBarPolicy(1)
        self.crop_view.setVerticalScrollBarPolicy(1)
        self.crop_view.setFixedHeight(182)
        self.crop_view.setFixedWidth(242)

        self.manual_grow_button = QPushButton("Manually Grow")
        self.automatic_grow_button = QPushButton("Automatically Grow")

        self.grow_grid = QGridLayout()
        self.status_grid = QGridLayout()

        #add label widgets to the status layout
        self.status_grid.addWidget(self.growth_label,0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)

        #add line edit widgets to the status layout
        self.status_grid.addWidget(self.growth_line_edit,0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit,2,1)

        #add widgets/layouts to the grow layout
        self.grow_grid.addWidget(self.crop_view,0,0)
        self.grow_grid.addLayout(self.status_grid,0,1)
        self.grow_grid.addWidget(self.manual_grow_button,1,0)
        self.grow_grid.addWidget(self.automatic_grow_button,1,1)

        #create a widget to display the grow layout
        self.view_crop_widget = QWidget()
        self.view_crop_widget.setLayout(self.grow_grid)

        #connections
        self.manual_grow_button.clicked.connect(self.manually_grow_crop)
        self.automatic_grow_button.clicked.connect(self.automatically_grow_crop)


    def instantiate_crop(self):
        print("hello")
        crop_type = self.crop_radio_buttons.selected_button() #get the radio button that was selected
        if crop_type == 1:
            self.simulated_crop = Wheat()
        elif crop_type == 2:
            self.simulated_crop = Potato()

        self.create_view_crop_layout(crop_type) #create the second layout (to view crop growth)
        self.stackedLayout.addWidget(self.view_crop_widget) #add this new widget to the stacked layout
        self.stackedLayout.setCurrentIndex(1) #change the visible layout in the stack

    def update_crop_view_status(self):
        crop_status_report = self.simulated_crop.report() #get the crop report

        #update the text fields
        self.growth_line_edit.setText(str(crop_status_report["growth"]))
        self.days_line_edit.setText(str(crop_status_report["days growing"]))
        self.status_line_edit.setText(str(crop_status_report["status"]))

        #change the visual representation graphic
        if crop_status_report["status"] == "Seed":
            self.crop_view.switch_scene(0)
        elif crop_status_report["status"] == "Seedling":
            self.crop_view.switch_scene(1)
        elif crop_status_report["status"] == "Young":
            self.crop_view.switch_scene(2)
        elif crop_status_report["status"] == "Mature":
            self.crop_view.switch_scene(3)
        elif crop_status_report["status"] == "Old":
            self.crop_view.switch_scene(4)

    def manually_grow_crop(self):
        manual_values_dialog = ManualGrowDialog()
        manual_values_dialog.exec_() #run the dialog window
        light, water = manual_values_dialog.values()
        self.simulated_crop.grow(light,water)
        self.update_crop_view_status()

    def automatically_grow_crop(self):
        for days in range(30):
            light = random.randint(1,10)
            water = random.randint(1,10)
            self.simulated_crop.grow(light,water)
        self.update_crop_view_status()

def main():
    crop_simulation = QApplication(sys.argv) #create new application
    crop_window = CropWindow() #create new instance of main window
    crop_window.show() #make instance visible
    crop_window.raise_() #raise instance to top of window stack
    crop_simulation.exec_() #monitor application for events


if __name__ == "__main__":
    main()
