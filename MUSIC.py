import webbrowser,random
import os
import os.path
def func(choice):
    DIR1="C:\Users\user\Desktop\Devotional songs"  //directory corresponding to where the music is 
    DIR2="C:\Users\user\Desktop\Dev"
    music1=filter(lambda x:x.lower().endswith("mp3"),os.listdir(DIR1)) //we can have many functions in this manner
    music1=list(music1)
    music2=filter(lambda x:x.lower().endswith("mp3"),os.listdir(DIR2))
    music2=list(music2)

    if choice==1:                                           //similarly we can have many if statements
            song=random.choice(music1)
            webbrowser.open(os.path.join(DIR1,song))
    if choice==2:
            song=random.choice(music2)
            webbrowser.open(os.path.join(DIR2,song))



