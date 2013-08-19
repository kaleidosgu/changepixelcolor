
import  wx
import  wx.lib.scrolledpanel as scrolled


#----------------------------------------------------------------------

text = "one two buckle my shoe three four shut the door five six pick up sticks seven eight lay them straight nine ten big fat hen"


class TestPanel(scrolled.ScrolledPanel):
    def __init__(self, parent, log):
        self.log = log
        scrolled.ScrolledPanel.__init__(self, parent, -1)

        words = text.split()

        panel1 = scrolled.ScrolledPanel(self, -1, size=(300, 300),
                                 style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER, name="panel1" )
        fgs1 = wx.FlexGridSizer(cols=3, vgap=4, hgap=10)

        for word in words:
            label = wx.StaticText(panel1, -1, word+":")
            chkBox = wx.CheckBox(panel1, -1, "", style=wx.ALIGN_RIGHT)

            pan = wx.Panel( panel1 )
           
            fgs1.Add(label, flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.LEFT, border=10)
            fgs1.Add(chkBox, flag=wx.CENTER, border=10)
            fgs1.Add(pan, flag=wx.RIGHT, border=10)
           
           
            emptyImage = wx.EmptyImage(10, 10)
            for x in xrange(10):
                for y in xrange(10):
                    emptyImage.SetRGB(x, y, 100, 100, 100)
            tempImage = emptyImage.ConvertToBitmap()
            wx.StaticBitmap(pan, -1, tempImage, (1, 1), (tempImage.GetWidth(), tempImage.GetHeight()))

        panel1.SetSizer( fgs1 )
        panel1.SetAutoLayout(1)
        panel1.SetupScrolling()
        
        panel1.Bind(wx.EVT_MOTION,  self.OnMove)
        wx.StaticText(panel1, -1, "Pos:", pos=(10, 12))
        self.posCtrl = wx.TextCtrl(panel1, -1, "", pos=(140, 10))
    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))


#----------------------------------------------------------------------


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win

#----------------------------------------------------------------------

if __name__ == '__main__':
    import sys,os
    import run
    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])