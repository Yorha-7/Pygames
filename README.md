# objective of this repo
I thought of using simulators before. gazebo was good, never got a chance to use isaac_sim ( i cant even set it up)
and just say this cool youtube channel known as green code. so if he is using pygames like that then, i should give it a try too.
first i will complete the basic to make a enivornment 
then i will try implementaing pid first, maybe i could make a tuner for the pid letting the user to visualize it.
its just the idea but i will work on it soon.
## something about the code_6
it contains a fine pid simulation code, though i was not sure about finding efficient way to calculate time only when the start object is completly overlapped to the finish objec and velocity vector is zero, but it would do.
if you are not using the Ki and want time till velocity vector becomes zero keep it as it is. but if ki is not equal to zero then you should remove the and pid() == 0 part cuz it will take simulation longer to finish
the line id marked by #changeme
<img width="2016" height="749" alt="Screenshot from 2025-08-27 14-34-15" src="https://github.com/user-attachments/assets/206e2847-4d2d-441e-bded-199f74fe1aba" />
# Snake game
you can use the agent.py to run the model and the game considering all dependencies are full fill. 
even the long hour training the ai model achive a highest score of 61. could be luch of Q factor but whatever, the model takes 11 parametrs as input, with 256 in hidden layer and 3 in output.
the 11 are the status of the head of the snake that contains things as the previouse direction, danger directions and the location of the food. after the highest score possible learning and performance was looking diminished. the total score algo collected looks less incresisng after some time. and snake was dying mostly due to it gets stuck in a loop.

<img width="1452" height="681" alt="Screenshot from 2025-08-29 20-53-55" src="https://github.com/user-attachments/assets/9946974e-2f89-45ca-998e-437b8ff73015" />
