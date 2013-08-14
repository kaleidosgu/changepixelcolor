#wxpython2.8 python2.6
import  wx
import random
from Main import opj

#----------------------------------------------------------------------
class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        #self.tempImage = NONE;
        self.log = log
        wx.Panel.__init__(self, parent, -1)
        b = wx.Button(self, -1, "Change the color", (200,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
		
        saveButton = wx.Button(self, -1, "savebtn", (400,50))
        self.Bind(wx.EVT_BUTTON, self.onSaveButton, saveButton)
    def onSaveButton(self, evt ):
        self.saveFile( self.tempImage )
    def OnButton(self, evt):
        png = wx.Image(opj('bitmaps/testimage.png'), wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        pos = 10
        wx.StaticBitmap(self, -1, png, (10, pos), (png.GetWidth(), png.GetHeight()))

        dstImage = wx.ImageFromBitmap( png )

        emptyImage = wx.EmptyImage(png.GetWidth(), png.GetHeight())
        defaultRed 		= 138;
        defaultGreen 	= 102;
        defaultBlue 	= 110;
        defaultRed1 	= 183;
        defaultGreen2 	= 171;
        defaultBlue3 	= 173;
        randomRed,randomGreen,randomBlue 		= self.randomColor()
        randomRed1,randomGreen1,randomBlue1 		= self.randomColor()
        indexColor		= 0;
        for x in xrange(png.GetWidth()):
            for y in xrange(png.GetHeight()):
                if defaultRed == dstImage.GetRed(x,y) and defaultGreen == dstImage.GetGreen(x,y) and defaultBlue == dstImage.GetBlue(x,y):
                    emptyImage.SetRGB(x, y, randomRed, randomGreen, randomBlue)
                elif defaultRed1 == dstImage.GetRed(x,y) and defaultGreen2 == dstImage.GetGreen(x,y) and defaultBlue3 == dstImage.GetBlue(x,y):
                    emptyImage.SetRGB(x, y, randomRed1, randomGreen1, randomBlue1)
                else:
                    emptyImage.SetRGB(x, y, dstImage.GetRed(x,y), dstImage.GetGreen(x,y), dstImage.GetBlue(x,y))
                indexColor = indexColor + 1

        pos = pos + png.GetHeight() + 10
        self.tempImage = emptyImage.ConvertToBitmap()
        wx.StaticBitmap(self, -1, self.tempImage, (10, pos), (self.tempImage.GetWidth(), self.tempImage.GetHeight()))
        v1,v2,v3 = 1,2,3

    def randomColor( self ):
	    v1 = random.randint(0,255)
	    v2 = random.randint(0,255)
	    v3 = random.randint(0,255)
	    return v1,v2,v3
    def saveFile( self, saveImage ):
	    saveImage.SaveFile('bitmaps/save.png', wx.BITMAP_TYPE_PNG)
def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win

#----------------------------------------------------------------------

if __name__ == '__main__':
    import sys,os
    import run
    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])

