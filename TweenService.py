#this is for TweenService library, to tween values with easing styles
from time import sleep
import math
import EasingStyles


class TweenObject():
    
    def __init__(self,time,FinalDimension,Callback,StartValue = 0, style = 'Linear',direction='In',interval =000.1):
        self.style = style
        self.time = time
        self.FinalDimension = FinalDimension
        self.direction = direction
        self.interval = interval
        self.Callback = Callback
        self.CurrentValue  = StartValue
        self.StartValue = StartValue

    def Tween(self):
        StyleFunction = EasingStyles.GetEasingStyle(self.style,self.direction)

        TweenCounter = 0 
        TimeMultiplier = self.time / self.interval
        print(TimeMultiplier)
        for i in range(int(TimeMultiplier+1)):
            
            newVal = EasingStyles.lerp(self.StartValue,self.FinalDimension,StyleFunction(i/TimeMultiplier))
            self.Callback(newVal)
            self.CurrentValue = newVal
            print(f'I:{i} {newVal}')
            sleep(self.interval)


