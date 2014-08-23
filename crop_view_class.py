try:
    from PyQt4.QtGui import *
except:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    
import crop_resources

class CropView(QGraphicsView):
    """this class provides a graphics view that has the required resources for displaying status of wheat and potato crops"""

    def __init__(self):
        super().__init__()

    def resources(self,name):
        #get the graphics
        seed = QPixmap(":/{0}_seed.png".format(name))
        seedling = QPixmap(":/{0}_seedling.png".format(name))
        young = QPixmap(":/{0}_young.png".format(name))
        mature = QPixmap(":/{0}_mature.png".format(name))
        old = QPixmap(":/{0}_old.png".format(name))
        crop_pictures = [seed, seedling, young, mature, old]

        #add the graphics to scenes
        self.crop_scenes = []
        for each in crop_pictures:
            self.crop_scenes.append(QGraphicsScene())
            self.crop_scenes[-1].addPixmap(each)
        self.setScene(self.crop_scenes[0]) #set the initial scene

    def switch_scene(self,scene):
        self.setScene(self.crop_scenes[scene])

class WheatView(CropView):
    def __init__(self):
        super().__init__()
        self.resources("wheat")

class PotatoView(CropView):
    def __init__(self):
        super().__init__()
        self.resources("potato")