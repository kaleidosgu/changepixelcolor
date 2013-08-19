import randomColor
class colorData():
    def __init__( self,red = 0, green = 0, blue = 0 ):
        self.log = ""
        self.red    = red
        self.green  = green
        self.blue   = blue
    def setColor( self, red, green, blue ):
         self.red   = red
         self.green = green
         self.blue  = blue
    def getColor( self ):
        return self.red,self.green,self.blue
    def isSameColor( self, colordata ):
        if colordata.red == self.red and colordata.green == self.green and colordata.blue == self.blue:
            return True
        return False
#rc = randomColor.randomColor()        
#rdata = colorData(rc.getRandomColor())
#print(rdata.getColor())
"""
c1 = colorData()
c1.setColor(1,1,1)
c2 = colorData()
c2.setColor(1,1,1)
"""

"""
sample_list = []
sample_list.append(c1)
sample_list.append(c2)
for data in sample_list: 
    print(data.getColor())
"""