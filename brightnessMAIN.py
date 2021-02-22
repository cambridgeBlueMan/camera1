from PyQt5 import QtCore, QtGui, QtWidgets

# insert appropriate names here
from brightnessGui import Ui_Dialog
#
from picamera import PiCamera
from time import sleep
import sys
import datetime
import json
import cameraFunctions
class Code_Dialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        #load a settings file
        self.fileObj = open("settings.json")
        self.cs = json.loads(self.fileObj.read())
        self.camera = PiCamera()
        #print (type (self.cs))
        # you might then declare and initialise some variable which will be available across the class
        self.framerate = 30.0
        self.resolution = (1920,1080)
        # you might then invoke some methods of your camera object
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        # or set sone attributes
        self.ui.sharpness.setRanges(-100,100,self.camera.sharpness)
        #print(type(self.ui.contrast))
        self.ui.contrast.setRanges(-100,100,self.camera.sharpness)
        self.ui.saturation.setRanges(-100,100,self.camera.saturation)
        self.ui.brightness.setRanges(0,100,self.camera.brightness)
        #set vales for color effects composite sliders u and v values
        self.ui.color_effects_u.setRanges(0,255,128)
        self.ui.color_effects_v.setRanges(0,255,128)
        
        self.camera.sensor_mode = 1
        self.ui.image_effect.addItems(self.camera.IMAGE_EFFECTS)
        self.ui.image_effect.setCurrentText('none')
        self.ui.awb_mode.addItems(self.camera.AWB_MODES)
        self.ui.awb_mode.setCurrentText('auto')
        self.ui.drc_strength.addItems(self.camera.DRC_STRENGTHS)
        self.ui.drc_strength.setCurrentText('off')
        self.ui.exposure_mode.addItems(self.camera.EXPOSURE_MODES)
        self.ui.exposure_mode.setCurrentText('auto')
        self.ui.flash_mode.addItems(self.camera.FLASH_MODES)
        self.ui.flash_mode.setCurrentText('off')
        self.ui.meter_mode.addItems(self.camera.METER_MODES)
        self.ui.meter_mode.setCurrentText('average')
        #self.camera.color_effects=(190,190)
        self.image_effect = 'none' 
        
        self.color_effects = None #option box true or false
        self.rotation = 0
        self.hflip = self.vflip = False
        self.zoom = (0.0, 0.0, 1.0, 1.0)
       
        """
        Note the following line:
        
        self.framerate is a variable you named and initialised.
        self.camera.framerate is an attribute of the camera object
        the code line sets the camera's framerate to the value held in the framerate variable
        """
        #for each key in the settings dictionery 
        for key in self.cs:
        #check if widget with the same name exists in the GUI
            if hasattr(self.ui,key):
                pass
                #print(key)
        #Depending on the type of the GUI or UI widget update the GUI
            if key == "color_effects":
        #get the value of color_effects from the dictionery
                    #print(self.cs[key])
                    self.ui.color_effects_u.setValue(self.cs[key][0])
                    self.ui.color_effects_v.setValue(self.cs[key][1])
        # This should automatically update through to the camera
        self.camera.framerate = self.framerate
        #self.ui.brightness.sendValue(self.cs["brightness"])
        #self.cs["brightness"]
        ##print(self.cs["brightness"])
        
        
        self.ui.image_effect.setCurrentText(self.cs ["image_effect"])
        
        # add your own method functions below

    def takePhoto(self):
        ##print(self)
        vwPhoto = cameraFunctions.generateFileName('s')
        #print(vwPhoto)
        self.camera.capture(vwPhoto)
    def startRecording(self):
        ##print(self)
        vwVideo = cameraFunctions.generateFileName('v')
        #print(vwVideo)
        self.camera.start_recording(vwVideo)
    def stopRecording(self):
        ##print(self)
        ##print(vwVideo)
        self.camera.stop_recording()
    def showPreview(self):
        #self.camera.start_preview()
        #print(self)
        #print(self.sender().isChecked())
        if self.sender().isChecked()==True:
            self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        else:self.camera.stop_preview()
    def changeCameraValue(self, value):
        control = self.sender().objectName()
        #value = args[1]
        if control == "brightness":
            self.camera.brightness = value
        elif control == "saturation":
            #print("in saturation")
            self.camera.saturation = value
        elif control == "contrast":
            self.camera.contrast = value
        elif control == "sharpness":
            self.camera.sharpness  = value
        else:
            pass
            #print("Unknown control!")
    def doColorEffect(self,value):
        #get the name of the sending control
        control = self.sender().objectName()
        #if we find the control is to set the u value
        #set the first element of the "color effects" dictionary item to value
        if control == "color_effects_u":
            self.cs["color_effects"][0] = value
            #if "color effects" is set to none in the GUI 
            if self.ui.color_effects_none.isChecked:
                pass #don't do anything
            else: #otherwise set the "color effects" to the value held in the color effects element of the settings dictionary
                #note that this dictionary item is a 2 element python list although the camera expects a 2 element tuple
                #however, it seems to buy this
                self.camera.color_effects = self.cs["color_effects"]
        if control == "color_effects_v":
            self.cs["color_effects"][1] = value
            if self.ui.color_effects_none.isChecked:
                pass
            else:
                self.camera.color_effects = self.cs["color_effects"]
        if control =="color_effects_none":
            print(value)
            if value == 2:
                
                self.camera.color_effects = None
            else:
                self.camera.color_effects = self.cs["color_effects"]
                
        
    def setImageEffect(self):
        #print(self)
        #print(self.camera.IMAGE_EFFECTS.values())
        #print(type(self.camera.IMAGE_EFFECTS))
        #print(self.camera.IMAGE_EFFECTS.keys)
        self.camera.image_effect = self.sender().currentText()
    def setAwbMode(self):
        self.camera.awb_mode = self.sender().currentText()
        #print(self)
    def setDrcStrength(self):
        self.camera.drc_strength = self.sender().currentText()
        #print(self)
    def setExposureMode(self):
        self.camera.exposure_mode = self.sender().currentText()
        #print(self)
    def setFlashMode(self):
        self.camera.flash_mode = self.sender().currentText()
        #print(self)
    def setMeterMode(self):
        self.camera.meter_mode = self.sender().currentText()
        #print(self)


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
                                                                                                                                                                                                                 
QtWidgets.QComboBox.acceptDrops
