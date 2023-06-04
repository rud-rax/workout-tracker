from pydub import AudioSegment

SOUND_FOLDER_PATH = "exercises/sounds/"
COUNTER_SOUND_FOLDER_PATH = SOUND_FOLDER_PATH + "counting_sounds/"


COUNTER_SOUNDS = { k : AudioSegment.from_wav(COUNTER_SOUND_FOLDER_PATH + str(k) + ".wav") for k in range(1,31) }

# Audio sound paths
HANDS_STRAIGHT = SOUND_FOLDER_PATH +"put_your_hands_straight.wav"
LEFT_HAND_DOWN= SOUND_FOLDER_PATH+ "left_hand_down.wav"
LEFT_HAND_UP=  SOUND_FOLDER_PATH+ "left_hand_up.wav"
RIGHT_HAND_DOWN=  SOUND_FOLDER_PATH+ "right_hand_down.wav"
RIGHT_HAND_UP=  SOUND_FOLDER_PATH+ "right_hand_up.wav"
START_REP_COUNT= SOUND_FOLDER_PATH+ "starting_repcount.wav"
HANDS_DOWN=  SOUND_FOLDER_PATH+ "hands_down.wav"
WELL_DONE=  SOUND_FOLDER_PATH+ "well_done_you_did_a_good_job.wav"
HALF_WAY= SOUND_FOLDER_PATH+ "half_way.wav"

# Audio sound objects
HANDS_STRAIGHT_SOUND = AudioSegment.from_wav(HANDS_STRAIGHT)
LEFT_HAND_DOWN_SOUND=AudioSegment.from_wav(LEFT_HAND_DOWN)
LEFT_HAND_UP_SOUND=AudioSegment.from_wav(LEFT_HAND_UP) 
RIGHT_HAND_DOWN_SOUND=AudioSegment.from_wav(RIGHT_HAND_DOWN)
RIGHT_HAND_UP_SOUND=AudioSegment.from_wav(RIGHT_HAND_UP)
START_REP_COUNT_SOUND=AudioSegment.from_wav(START_REP_COUNT)
HANDS_DOWN_SOUND=AudioSegment.from_wav(HANDS_DOWN)
WELL_DONE_SOUND = AudioSegment.from_wav(WELL_DONE)
HALF_WAY_SOUND = AudioSegment.from_wav(HALF_WAY)

