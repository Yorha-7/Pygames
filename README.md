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
