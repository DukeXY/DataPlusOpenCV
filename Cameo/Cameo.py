import cv2
import filters
from Manager import WindowManager, CaptureManager

class Cameo(object):
	def __init__(self):
		self._windowManager=WindowManager('Cameo',self.onKeypress)
		self._captureManager=CaptureManager(cv2.VideoCapture(0),self._windowManager,True)
		#self._curveFilter=filters.BGRPortraCurveFilter()
	def run(self):
		self._windowManager.createWindow()
		while self._windowManager.isWindowCreated:
			self._captureManager.enterFrame()
			frame=self._captureManager.frame
			#filters.strokeEdges(frame,frame)
			#self._curveFilter.apply(frame,frame)
			self._captureManager.exitFrame()
			self._windowManager.processEvents()

	def onKeypress(self, keycode):
		if keycode==32:
			self._captureManager.writeImage('screenshot.png')
		elif keycode==9:
			if not self._captureManager.isWritingVideo:
				print "start" 
				self._captureManager.startWritingVideo('screencast.avi')
			else:
				print "end"
				self._captureManager.stopWritingVideo()
		elif keycode==27:
			self._windowManager.destroyWindow()

if __name__=="__main__":
	print 'lalala';
	Cameo().run()