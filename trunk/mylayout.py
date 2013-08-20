import wx
import wx.lib.scrolledpanel as scrolled
import colorpanel as colp
import colorData as colda
import randomColor
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
        #testCtrl = wx.StaticText(self.graphicPanel1,-1,"ffff")
        #testCtrl2 = wx.StaticText(graphicPanel2,-1,"fd")
        
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
        self.Bind(wx.EVT_BUTTON, self.onGenerateImage, generateButton)

        btnBox=wx.BoxSizer(wx.HORIZONTAL)
        btnBox.Add(generateButton,proportion=0,flag=wx.LEFT,border=5)
        btnBox.Add(randomButton,proportion=1,flag=wx.LEFT,border=5)
        btnBox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)
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
        self.processImage( self.png )
    def onGenerateImage( self,evt ):
        self.colorLst = []
        self.panelLst = []
        self.png = wx.Image(opj('testimage.png'), wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        pos = 10
        wx.StaticBitmap(self, -1, self.png, (10, pos), (self.png.GetWidth(), self.png.GetHeight()))    
        self.fgs1.Clear(True)
        self.dstImage = wx.ImageFromBitmap( self.png )
        
        for x in xrange(self.png.GetWidth()):
            for y in xrange(self.png.GetHeight()):
                redColor = self.dstImage.GetRed(x,y)
                greenColor = self.dstImage.GetGreen(x,y)
                blueColor = self.dstImage.GetBlue(x,y)
                tempColor = colda.colorData(redColor,greenColor,blueColor)
                if self.isColorExist( tempColor ) == False:
                    self.colorLst.append( tempColor )
                    colorPanel = colp.ColorPanel(self.scrollPanel,-1,tempColor)
                    self.fgs1.Add(colorPanel, flag=wx.CENTER, border=10)
                    self.panelLst.append(colorPanel)
          
        self.scrollPanel.SetSizer( self.fgs1 )
        self.scrollPanel.SetAutoLayout(1)
        self.scrollPanel.SetupScrolling()
    def processImage( self, png ):
        emptyImage = wx.EmptyImage(png.GetWidth(), png.GetHeight())
        colorGenerate = randomColor.randomColor()
        randomColorLst = []
        for colorItem in self.colorLst:
            colorArray = colorGenerate.getRandomColor()
            randomColorLst.append(colda.colorData(colorArray[0],colorArray[1],colorArray[2]))
            
        for x in xrange(png.GetWidth()):
            for y in xrange(png.GetHeight()):
                tempColorData = colda.colorData(self.dstImage.GetRed(x,y),self.dstImage.GetGreen(x,y),self.dstImage.GetBlue(x,y))
                indexColor = 0
                findColor = False;
                c1,c2,c3 = 0,0,0;
                for dataColor in self.colorLst:
                    if dataColor.isSameColor(tempColorData) == True:
                        tempRandomColorData = randomColorLst[indexColor]
                        c1,c2,c3 = tempRandomColorData.getColor()
                        findColor = True
                        break;
                    indexColor = indexColor + 1
                if findColor == True:
                    panelInstance = self.panelLst[indexColor]
                    if panelInstance.isChecked() == False :
                        emptyImage.SetRGB(x, y, c1,c2,c3) 
                    else:
                        emptyImage.SetRGB(x, y, self.dstImage.GetRed(x,y), self.dstImage.GetGreen(x,y), self.dstImage.GetBlue(x,y)) 
                else:
                    emptyImage.SetRGB(x, y, self.dstImage.GetRed(x,y), self.dstImage.GetGreen(x,y), self.dstImage.GetBlue(x,y)) 
        pos = png.GetHeight() + 10
        self.tempImage = emptyImage.ConvertToBitmap()
        wx.StaticBitmap(self, -1, self.tempImage, (10, pos), (self.tempImage.GetWidth(), self.tempImage.GetHeight()))
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = mainFrame()
    frame.Show(True)
    app.MainLoop()