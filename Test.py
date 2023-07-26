from TweenService import TweenObject
from time import sleep
def test (x):
    print(x)
Tween = TweenObject(4,100,test)

#use this to start the tween
Tween.StartTween()

for i in range(1000):
    print(i)
    sleep(.01)