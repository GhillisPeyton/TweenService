# TweenService
Thank you for checking this project out! This is my first actual Python project, and my first time using Git and Git Hub to manage projects.
This can be used to generate numbers between two points, using different easing styles [taken from https://easings.net/], although not all styles are implemented yet (as I have trouble converting the JS source code into Python)

This uses threading to run concurrently, the StartTween() will return the thread, but it can also be accessed through TweenObject.CurrentThread

Through EasingStyles.py, you can view, modify and add your own easing styles more a more custom experience. 

The basic Syntax is:

#importing
from TweenService import TweenObject

#here we define a callback function to get called every generation
def Test(x:float):
  print(x)

Tween = TweenObject(
time = the time it takes to get to the endpoint
FinalDimension = the final number that will be the end result of the tween
Callback = the function that is fired every generation
OnFinish = the function that is fired when the tween is completed, and passes the current value. Will still fire if the tween is stopped early
StartValue = the value that is the start point of the tween - Default 0
style - the easing style of the tween - Default linear
direction - the easing direction of the tween - Default In (doesn't matter for linear)
interval - how often a new generation is made, ( ex: if equal to one, and time is set to 4, then it will generate four values, 0, 25,50,75,100) -default = .001
)

#to start the tween, simply

Tween.StartTween()

To end the tween prematurely,
Tween.StopTween()
this will do nothing if the tween is dead.

