import wx
class mainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,title="simple",size=(500,335))
        mainPanel = wx.Panel(self)

        leftPanel = wx.Panel(mainPanel)
        rightPanel = wx.Panel(mainPanel)
        #------------------------LEFT----------------------------
        graphicPanel1 = wx.Panel( leftPanel )
        graphicPanel2 = wx.Panel( leftPanel )

        leftBox=wx.BoxSizer(wx.VERTICAL)
        testCtrl = wx.StaticText(graphicPanel1,-1,"dffdd")
        testCtrl2 = wx.StaticText(graphicPanel2,-1,"fd")
        leftBox.Add(graphicPanel1,proportion=0,flag=wx.EXPAND |wx.ALL,border=15)
        leftBox.Add(graphicPanel2,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
        leftPanel.SetSizer(leftBox)

        #------------------------RIGHT---------------------------
        rightBox = wx.BoxSizer(wx.VERTICAL)
        posText = wx.TextCtrl(rightPanel, -1, "FDFD", pos=(0, 10))

        btnPanel = wx.Panel(rightPanel)

        randomButton = wx.Button(btnPanel,label='Random')
        saveButton = wx.Button(btnPanel,label='Save')
        generateButton = wx.Button(btnPanel,label='Generate')
        tempColor = ColorPanel(btnPanel,-1,255,0,0)

        btnBox=wx.BoxSizer(wx.HORIZONTAL)
        btnBox.Add(randomButton,proportion=1,flag=wx.LEFT,border=5)
        btnBox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)
        btnBox.Add(generateButton,proportion=0,flag=wx.LEFT,border=5)
        btnBox.Add(tempColor,proportion=0,flag=wx.LEFT,border=5)
        btnPanel.SetSizer(btnBox)

        rightBox.Add(posText,proportion=0,flag=wx.EXPAND |wx.ALL,border=15)
        rightBox.Add(btnPanel,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

        mainBox = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(leftPanel,proportion=0,flag=wx.EXPAND |wx.ALL,border=55)
        mainBox.Add(rightPanel,proportion=1,flag=wx.LEFT,border=5)

        rightPanel.SetSizer(rightBox)

        mainPanel.SetSizer(mainBox)
class ColorPanel(wx.Panel):
    def __init__(self, parent, id=-1 ,red=3,green=255,blue=255):
        self.colorSize = 10
        wx.Panel.__init__(self, parent, id)
        destroyBtn = wx.Button(self,label='Destroy')
        
        self.emptyImage = wx.EmptyImage(self.colorSize, self.colorSize)
        self.setColor(red,green,blue)
        self.tempImage = self.emptyImage.ConvertToBitmap()
        self.staticBmp = wx.StaticBitmap(self, -1, self.tempImage, (0, 0), (self.colorSize, self.colorSize))
        
        self.boxsize = wx.BoxSizer(wx.HORIZONTAL)
        self.boxsize.Add(self.staticBmp,proportion=0,flag=wx.EXPAND |wx.ALL,border=1)
        self.boxsize.Add(destroyBtn,proportion=1,flag=wx.LEFT,border=5)
        self.SetSizer(self.boxsize)
        
    def setColor( self, red, green, blue ):
        for colorx in xrange(self.colorSize):
            for colory in xrange(self.colorSize):
                self.emptyImage.SetRGB(colorx, colory, red, green, blue)
                
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = mainFrame()
    frame.Show(True)
    app.MainLoop()