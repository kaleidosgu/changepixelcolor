import random
class randomColor():
    def __init__( self ):
        self.log = ""
    def getRandomColor( self ):
         color1 = random.randint(0,255)
         color2 = random.randint(0,255)
         color3 = random.randint(0,255)
         return color1,color2,color3
                