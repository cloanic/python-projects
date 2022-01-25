import time
#define the countdown function
def countdown(t):
    #while loop for t
    while t:
        #takes minutes and seconds and gets the correct output for the user
        mins, secs = divmod(t, 60)
        #timer formatted
        timer = '{:02d}:{:02d}'.format(mins,secs)
        #prints the timer on screen
        print(timer, end="\r")
        #sleep after the time gets to zero and prints timer completed
        time.sleep(1)
        t-=1
    print('Timer completed!')

#input for the user to add time in seconds
t= input("Enter the time in seconds:")
#call the main countdown function with an integer expected
countdown(int(t))