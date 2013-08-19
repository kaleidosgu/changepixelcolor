import wx
import wx.lib.scrolledpanel as scrolled
import colorpanel as colp
import colorData as colda
from Main import opj
class mainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,title="simple",size=(600,335))
        mainPanel = wx.Panel(self)
        self.colorLst = []

        leftPanel = wx.Panel(mainPanel)
        rightPanel = wx.Panel(mainPanel)
        #------------------------LEFT----------------------------
        self.graphicPanel1 = wx.Panel( leftPanel )
        graphicPanel2 = wx.Panel( leftPanel )

        leftBox=wx.BoxSizer(wx.VERTICAL)
        testCtrl = wx.StaticText(self.graphicPanel1,-1,"ffff")
        testCtrl2 = wx.StaticText(graphicPanel2,-1,"fd")
        
        leftBox.Add(self.graphicPanel1,proportion=1,flag=wx.EXPAND |wx.ALL,border=15)
        leftBox.Add(graphicPanel2,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
        leftPanel.SetSizer(leftBox)

        #------------------------RIGHT---------------------------
        rightBox = wx.BoxSizer(wx.VERTICAL)
        posText = wx.TextCtrl(rightPanel, -1, "FDFD", pos=(0, 10))

        btnPanel = wx.Panel(rightPanel)

        randomButton = wx.Button(btnPanel,label='Random')
        saveButton = wx.Button(btnPanel,label='Save')
        generateButton = wx.Button(btnPanel,label='Generate')
        
        self.Bind(wx.EVT_BUTTON, self.OnButtonRandom, randomButton)

        btnBox=wx.BoxSizer(wx.HORIZONTAL)
        btnBox.Add(randomButton,proportion=1,flag=wx.LEFT,border=5)
        btnBox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)
        btnBox.Add(generateButton,proportion=0,flag=wx.LEFT,border=5)
        btnPanel.SetSizer(btnBox)
        
        self.scrollPanel = scrolled.ScrolledPanel(rightPanel, -1, size=(100, 200),
                                 style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER, name="panel1" )
        self.fgs1 = wx.FlexGridSizer(cols=1, vgap=4, hgap=10)

        rightBox.Add(posText,proportion=0,flag=wx.EXPAND |wx.ALL,border=15)
        rightBox.Add(self.scrollPanel,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
        rightBox.Add(btnPanel,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
        
        
        mainBox = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(leftPanel,proportion=0,flag=wx.EXPAND |wx.ALL,border=100)
        mainBox.Add(rightPanel,proportion=1,flag=wx.LEFT,border=5)

        rightPanel.SetSizer(rightBox)

        mainPanel.SetSizer(mainBox)
    def isColorExist( self, cdata ):
        for data in self.colorLst: 
            if data.isSameColor(cdata) == True:
                return True
        return False
    def OnButtonRandom(self, evt):
        self.colorLst = []
        png = wx.Image(opj('testimage.png'), wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        pos = 10
        wx.StaticBitmap(self, -1, png, (10, pos), (png.GetWidth(), png.GetHeight()))    
        
        dstImage = wx.ImageFromBitmap( png )
        
        for x in xrange(png.GetWidth()):
            for y in xrange(png.GetHeight()):
                redColor = dstImage.GetRed(x,y)
                greenColor = dstImage.GetGreen(x,y)
                blueColor = dstImage.GetBlue(x,y)
                tempColor = colda.colorData(redColor,greenColor,blueColor)
                if self.isColorExist( tempColor ) == False:
                    self.colorLst.append( tempColor )
                    colorPanel = colp.ColorPanel(self.scrollPanel,-1,tempColor)
                    self.fgs1.Add(colorPanel, flag=wx.CENTER, border=10)

        self.scrollPanel.SetSizer( self.fgs1 )
        self.scrollPanel.SetAutoLayout(1)
        self.scrollPanel.SetupScrolling()        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = mainFrame()
    frame.Show(True)
    app.MainLoop()