from pygame import mixer

mixer.init() #start the mixer

mixer.music.load("F:/Songs/01 First Time.mp3") #load the song
mixer.music.set_volume(0.9) #se the volume
mixer.music.play() #play the song

while True :
    print("Press 'p' to pause and 'r' to resume")
    print("Press 'e' to exit")
    query = input(">>>")

    if query == 'p':
        mixer.music.pause() #pause the song
    elif query == 'r':
        mixer.music.unpause() #resume the song
    elif query == 'e':
        mixer.music.stop() #stop the music
    else:
        print('Wrong Input')
        break
