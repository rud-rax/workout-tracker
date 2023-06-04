# from playsound import playsound
# import required modules
from pydub import AudioSegment
from pydub.playback import play

# for playing wav file


SOUND_PATH = "exercises/beep1.wav"
SOUND = AudioSegment.from_wav(SOUND_PATH)


def ringring(song) :
    # print("Playing sound")
    # playsound("../exercises/beep1.wav")
    # print("Done")

    print('playing sound using pydub')
    play(song)

if __name__ == "__main__" :

    ringring(SOUND)