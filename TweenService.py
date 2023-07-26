#this is for TweenService library, to tween values with easing styles

from time import sleep
from TweenService import EasingStyles
import threading

class TweenObject():
    
    def __init__(self,time,FinalDimension,Callback,OnFinish = None,StartValue = 0, style = 'Linear',direction='In',interval =.001):
        self.style = style
        self.time = time
        self.FinalDimension = FinalDimension
        self.direction = direction
        self.interval = interval
        self.Callback = Callback
        self.CurrentValue  = StartValue
        self.StartValue = StartValue
        self.OnFinish = OnFinish
        self.CurrentThread = None
        self.StopCondition = False
        self.Finished = False

    def ProccessTween(self):
        StyleFunction = EasingStyles.GetEasingStyle(self.style,self.direction)
        TimeMultiplier = self.time / self.interval
    
        for i in range(int(TimeMultiplier+1)):      
            if self.StopCondition:
                break

            newVal = EasingStyles.lerp(self.StartValue,self.FinalDimension,StyleFunction(i/TimeMultiplier))
            self.Callback(newVal)
            self.CurrentValue = newVal
            
            sleep(self.interval)
        self.Finished = True
        if self.OnFinish:
            self.OnFinish(self.CurrentValue)

    def StartTween(self):
        self.CurrentThread = threading.Thread(target=self.ProccessTween,daemon= True)
        self.CurrentThread.start()

        return self.CurrentThread
      
    def StopTween(self):
        self.StopCondition = True

    def Wait(self):
        while not self.Finished:
            sleep(.01)

        
        

        