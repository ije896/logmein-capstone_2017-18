import interface
# speech_file = '/Users/iegan/Documents/School/W18 Classes/CS189B/logmein-capstone_2017-18/audio_media/speech_audio/enigma_tc_snippet.wav'
speech_file = '/Users/iegan/Documents/School/W18 Classes/CS189B/logmein-capstone_2017-18/audio_media/nonsense.wav'
opts = {'run_all':True}
a = interface.Interface()
a.process_filepath(speech_file, opts)
