from picamera import PiCamera
camera=PiCamera()
camera.start_preview(fullscreen=False,window=(960,0,960,540))
u=255 #THIS VALUE WE GET FROM A COMPOSITE SLIDER CALLED UWE
v=255# THIS VALUE WE ASO GET FROM A COMPOSITE SLIDER CALLED VE
colouron=input('color effect?')#this would be  a tick box
if colouron== 't': #this would be isChecked property
    camera.color_effects=(u,v)
else: camera.color_effects=None

