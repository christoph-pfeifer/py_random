import numpy as np
import webbrowser

list_number = np.arange(6)+1
x = np.random.choice(list_number)
#print(list_number)

def workout_session(x):
    if x == 1:
        webbrowser.open('https://www.youtube.com/watch?v=JkVHrA5o23o')
        print('enjoy the workout')
    elif x == 2:
        webbrowser.open('https://www.youtube.com/watch?v=uyFjMupI5B0')
        print('enjoy the workout')   
    elif x == 3:
        webbrowser.open('https://www.youtube.com/watch?v=obiX6uGNCEc')
        print('enjoy the workout')
    elif x == 4:
        webbrowser.open('https://www.youtube.com/watch?v=l4vErU2pT0U')
        print('enjoy the workout')   
    elif x == 5:
        webbrowser.open('https://www.youtube.com/watch?v=Emu7uB59E2g')
        print('enjoy the workout')
    elif x == 6:
        webbrowser.open('https://www.youtube.com/watch?v=HVV84F_Zn5s')
        print('enjoy the workout')
    elif x == 7:
        print('it seems today is rest-day!') 
    else:
        print('try again')

#further tasks:
#put youtube links in a seperate txt file
#video should play automatically
#deactivate autoplay after video is finished

workout_session(x)