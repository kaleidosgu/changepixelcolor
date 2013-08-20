import wx
import colorData
class ColorPanel(wx.Panel):
    def __init__(self, parent, id=-1 ,crData = None):
        self.colorWidth = 200
        self.colorHeight = 10
        wx.Panel.__init__(self, parent, id)
        #destroyBtn = wx.Button(self,label='Destroy')
        self.checkBox = wx.CheckBox(self, -1, "Checked", (0, 0), (50, 20))
        self.checkBox.SetValue( True )
        
        self.emptyImage = wx.EmptyImage(self.colorWidth, self.colorHeight)
        self.crData = crData
        red,green,blue = crData.getColor()
        self.setColor(red,green,blue)
        self.tempImage = self.emptyImage.ConvertToBitmap()
        self.staticBmp = wx.StaticBitmap(self, -1, self.tempImage, (0, 0), (self.colorWidth, self.colorHeight))
        
        self.boxsize = wx.BoxSizer(wx.HORIZONTAL)
        self.boxsize.Add(self.staticBmp,proportion=0,flag=wx.EXPAND |wx.ALL,border=1)
        self.boxsize.Add(self.checkBox,proportion=1,flag=wx.LEFT,border=5)
        self.SetSizer(self.boxsize)
    def setColor( self, red, green, blue ):
        for colorx in xrange(self.colorWidth):
            for colory in xrange(self.colorHeight):
                self.emptyImage.SetRGB(colorx, colory, red, green, blue)
    def isChecked( self ):
        return self.checkBox.IsChecked()
                