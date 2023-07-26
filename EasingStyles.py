import math

#Easing Styles, For use in GetEasingStyles Method
#Credit to https://easings.net/ for the mathematical functions
class EasingStyles:
    
    def Linear(self,x:int):
        return x
    
    def InSine(self,x: int):
        return 1-math.cos((x*math.pi)/2)


    def OutSine(self,x:int):
        return math.sin((x*math.pi)/2)

    def InOutSine(self,x:int):
        return -(math.cos(math.pi*x)-1)/2

    def InCubic(self,x:int):
        return math.pow(x,3)

    def OutCubic(self,x:int):
        return 1- math.pow(1-x,3)

    def InOutCubic(self,x:int):
        toSend  = None 
        if x < 0.5:
            toSend = 2*x*x
        else:
            toSend = 1-math.pow(-2*x+2,2)/2
        return toSend
    
    def InQuint(self,x:int):
        return math.pow(x,5)

    def OutQuint(self,x:int):
        return 1- math.pow(1-x,5)

    def InOutQuint(self,x:int):
        toSend = None
        if x<.5:
            toSend = 16*math.pow(x,5)
        else:
            1-math.pow(-2*x+2,5)/2
        return toSend
    

    def InQuad(self,x:int):
        return math.pow(x,2)

    def OutQuad(self,x:int):
        return 1-(1-x)*(1-x)
    
    def InOutQuad(self,x:int):
        toSend = None
        if x <.5:
            toSend = 2*x*x
        else:
            toSend = 1- math.pow(-2*x+2,2)/2
        return toSend
    
    def InQuart(self,x:int):
        return math.pow(x,4)
    
    def OutQuart(self,x:int):
        return 1- math.pow(1-x,4)

    def InOutQuart(self,x:int):
        if x<.5:
            return 8*x*x*x*x
        else:
            return 1-math.pow(-2*x+2,4)/2
    
    def InExpo(self,x:int):
        if x ==0:
            return 0
        else:
            return math.pow(2,10*x-10)
        
    def OutExpo(self,x:int):
        if x==1: 
            return 1
        else:
            return 1-math.pow(2,-10*x)
        
    def __init__(self):
        self.EasingStyles = {'InSine' : self.InSine,'OutExpo':self.OutExpo,'InExpo':self.InExpo,'InOutQuart':self.InOutQuart,'OutQuart':self.OutQuart,'InQuart':self.InQuart,'InOutQuad':self.InOutQuad,'OutQuad':self.OutQuad,'InQuad':self.InQuad,
                             'InOutQuint':self.InOutQuint,'InQuint':self.InQuint,'OutQuint':self.OutQuint, 'OutSine':self.OutSine,'InOutSine':self.InOutSine,'OutCubic':self.OutCubic,'InCubic':self.InCubic,'InOutCubic':self.InOutCubic,'InLinear':self.Linear,'OutLinear':self.Linear,'InOutLinear':self.Linear}

def lerp(start,goal,c):
    return start + (goal-start)*c


def GetEasingStyle(Style:str,Direction:str):
    
    return EasingStyles().EasingStyles[f'{Direction}{Style}']


