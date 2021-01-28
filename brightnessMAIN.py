from PyQt5 import QtCore, QtGui, QtWidgets

# insert appropriate names here
from brightnessGui import Ui_Dialog
#
from picamera import PiCamera
from time import sleep
import sys
import datetime
import cameraFunctions

class Code_Dialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        
        # now instantiate a camera object. 
        self.camera = PiCamera()
        # you might then declare and initialise some variable which will be available across the class
        self.framerate = 30.0
        self.resolution = (1920,1080)
        # you might then invoke some methods of your camera object
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        
        # or set some ranges and default values for composite sliders and dials
        self.ui.sharpness.setRanges(-100,100,self.camera.sharpness)
        self.ui.contrast.setRanges(-100,100,self.camera.contrast)
        self.ui.saturation.setRanges(-100,100,self.camera.saturation)
        self.ui.brightness.setRanges(0,100,self.camera.brightness)
        # 
        self.camera.sensor_mode = 1
        # camera dictionarys provide entries for drop down lists
        self.ui.imageEffect.addItems(self.camera.IMAGE_EFFECTS)
        self.ui.awbMode.addItems(self.camera.AWB_MODES)
        self.ui.drcStrength.addItems(self.camera.DRC_STRENGTHS)
        self.ui.exposureMode.addItems(self.camera.EXPOSURE_MODES)
        self.ui.exposureMode.setCurrentText('auto')
        self.ui.flashMode.addItems(self.camera.FLASH_MODES)
        self.ui.meterMode.addItems(self.camera.METER_MODES)
        self.camera.color_effects=(190,190)
        #this portion of code refers to some pi camera attributes in the camera class
        '''def _init_defaults(self):
        self.sharpness = 0
        self.contrast = 0
        self.brightness = 50
        self.saturation = 0
        self.iso = 0 # auto
        
        self.video_stabilization = False #code using tick box
        
        self.exposure_compensation = 0 # range -25 to +25 
        self.exposure_mode = 'auto' # set defaults for this
        
        self.meter_mode = 'average' # set defaults for this
        self.awb_mode = 'auto' # set defaults for this
        self.image_effect = 'none' # set defaults for this
        
        self.color_effects = None #option box true or false
        self.rotation = 0
        self.hflip = self.vflip = False
        self.zoom = (0.0, 0.0, 1.0, 1.0)
        these are the defaults from the pi camera documentation'''
        

        
    
        """
        Note the following line:
        
        self.framerate is a variable you named and initialised.
        self.camera.framerate is an attribute of the camera object
        the code line sets the camera's framerate to the value held in the framerate variable
        """
        self.camera.framerate = self.framerate

        # add your own method functions below

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
     
    def changeCameraValue(self, value):
        control = self.sender().objectName()
        #value = args[1]
        if control == "brightness":
            self.camera.brightness = value
        elif control == "saturation":
            print("in saturation")
            self.camera.saturation = value
        elif control == "contrast":
            self.camera.contrast = value
        elif control == "sharpness":
            self.camera.sharpness  = value
        else:
            print("Unknown control!")
    def setImageEffect(self):
        print(self)
        print(self.camera.IMAGE_EFFECTS.keys())
        print(self.camera.IMAGE_EFFECTS.values())
        print(type(self.camera.IMAGE_EFFECTS))
        print(self.camera.IMAGE_EFFECTS.keys)
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
                                                                                                                                                                                                                 
                                                                                                                                                                                                                 