from PyQt5 import QtCore, QtGui, QtWidgets

# insert appropriate names here
from vwBrightnessGui import Ui_Dialog
#
from picamera import PiCamera
from time import sleep
import sys
import datetime
import cameraFunctions
"""
You may need to change the line declaring the class below. It will depend on the choice you make
for your containing window: main window, dialog box etc)
"""
class Code_Dialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        # Ui_Form is the main designer generated class. so instantiate one. Precede the variable name with
        # the word 'self'

        self.ui = Ui_Dialog()
        # now pass the main window object to it so that the setupUi method can draw all
        # the widgets into the window
        self.ui.setupUi(self)
        #self.ui.imageEffect.addItem('none')
        #self.ui.imageEffect.addItem('negative')
        #vwlist=['tom','dick','harry']
        #self.ui.imageEffect.addItems(vwlist)
        self.show()
        # now instantiate a camera object. Again the variable name is preceded by the word 'self'
        self.camera = PiCamera()
        # you might then declare and initialise some variable which will be available across the class
        self.framerate = 30.0
        self.resolution = (1920,1080)
        # you might then invoke some methods of your camera object
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        # or set sone attributes
        self.camera.sensor_mode = 1
        self.ui.imageEffect.addItems(self.camera.IMAGE_EFFECTS)
        self.ui.awbMode.addItems(self.camera.AWB_MODES)
        self.ui.drcStrength.addItems(self.camera.DRC_STRENGTHS)
        self.ui.exposureMode.addItems(self.camera.EXPOSURE_MODES)
        self.ui.flashMode.addItems(self.camera.FLASH_MODES)
        self.ui.meterMode.addItems(self.camera.METER_MODES)
        #this portion of code refers to some pi camera attributes in the camera class
        

        
    
        """
        Note the following line:
        
        self.framerate is a variable you named and initialised.
        self.camera.framerate is an attribute of the camera object
        the code line sets the camera's framerate to the value held in the framerate variable
        """
        self.camera.framerate = self.framerate

        # add your own method functions below

    def someMethodName(self):
        print(self)

    def AnotherMethod(self):
        print(self)
    def takePhoto(self):
        #print(self)
        vwPhoto = cameraFunctions.generateFileName('s')
        print(vwPhoto)
        self.camera.capture(vwPhoto)
    def startRecording(self):
        #print(self)
        vwVideo = cameraFunctions.generateFileName('v')
        print(vwVideo)
        self.camera.start_recording(vwVideo)
    def stopRecording(self):
        #print(self)
        #print(vwVideo)
        self.camera.stop_recording()
    def showPreview(self):
        #self.camera.start_preview()
        print(self)
        print(self.sender().isChecked())
        if self.sender().isChecked()==True:
            self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        else:self.camera.stop_preview()
    
    def changeBrightness(self):
        #print(self)
        print(self.sender().value())
        self.camera.brightness = self.sender().value()
        
    def changeContrast(self):
        #print(self.sender().value())
        self.camera.contrast = self.sender().value()
    def changeSharpness(self):
        #print(self.sender().value())
        self.camera.contrast = self.sender().value()
    def changeSaturation(self):
        #print(self.sender().value())
        self.camera.saturation = self.sender().value()
    def setImageEffect(self):
        print(self)
        print(self.camera.IMAGE_EFFECTS.keys())
        print(self.camera.IMAGE_EFFECTS.values())
        print(type(self.camera.IMAGE_EFFECTS))
        print(self.camera.IMAGE_EFFECTS.keys)
        print(values().camera.IMAGE_EFFECTS)
        self.camera.image_effect = self.sender().currentText()
    def setAwbMode(self):
        self.camera.awb_mode = self.sender().currentText()
        print(self)
    def setDrcStrength(self):
        self.camera.drc_strength = self.sender().currentText()
        print(self)
    def setExposureMode(self):
        self.camera.exposure_mode = self.sender().currentText()
        print(self)
    def setFlashMode(self):
        self.camera.flash_mode = self.sender().currentText()
        print(self)
    def setMeterMode(self):
        self.camera.meter_mode = self.sender().currentText()
        print(self)


#######################################################################################
    #                           END OF CLASS
#######################################################################################
if __name__ == "__main__":
    import sys
    # instiantiate an app object from the QApplication class 
    app = QtWidgets.QApplication(sys.argv)
    # instantiate an object containing the logic code
    MainWindow = Code_Dialog()
    sys.exit(app.exec_())
                                                                                                                                                                                                                 
                                                                                                                                                                                                                 