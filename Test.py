#this is for TweenService library, to tween values with easing styles
from time import sleep
import math


#Easing Styles, For use in GetEasingStyles Method
#Credit to https://easings.net/ for the mathematical functions
class EasingStyles():
    def InSine(x: int):
        return 1-math.cos((x*math.pi)/2)


    def OutSine(x:int):
        return math.sin((x*math.pi)/2)

    def InOutSine(x:int):
        return -(math.cos(math.pi*x)-1)/2

    def InCubic(x:int):
        return math.pow(x,3)

    def OutCubic(x:int):
        return 1- math.pow(1-x,3)

    def InOutCubic(x:int):
        toSend  = None 
        if x < 0.5:
            toSend = 2*x*x
        else:
            toSend = 1-math.pow(-2*x+2,2)/2

    def InQuint(x:int):
        return math.pow(x,5)

    def OutQuint(x:int):
        return 1- math.pow(1-x,5)

    def InOutQuint(x:int):
        toSend = None
        if x<.5:
            toSend = 16*math.pow(x,5)
        else:
            1-math.pow(-2*x+2,5)/2

    def InQuad(x:int):
        return math.pow(x,2)

    def OutQuad(x:int):
        return 1-(1-x)*(1-x)


class TweenObject():
    
    def __init__(self,style,time,FinalDimension,direction,interval):
        self.style = style
        self.time = time
        self.FinalDimension = FinalDimension
        self.direction = direction
        self.interval = interval

    def Tween(self):



