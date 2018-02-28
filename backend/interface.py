import sys
import os, os.path
import subprocess
import json

# Import our backend interfaces

from text  import Interface as t_int
from audio import Interface as a_int
from Video import Interface as v_int

# TODO:
    # - have audio automatically pull credentials.json
    # - benchmarking by module
        # - test harness to collect data for relationship btw video length and processing times (prob not quite linear)

class Interface:

    def __init__(self):
        print("__init__ [backend]: STUB")
        self.audio_out = "./backend_audio_out.wav"

    def process_filepath(self, fp, options):
        challenge_id = options['challenge_id']
        stt_path = "../research/{}.stt".format(challenge_id)

        if challenge_id is None:
            print("ERROR: No challenge_id provided. Exiting\n")
            return -1


        text  = False
        audio = False
        video = False

        decouple_status = Interface.decouple_av(fp)

        if (decouple_status[0] == -1):
            print("ERROR: no video file at given filepath. Exiting\n")
            return decouple_status

        # # No errors, so proceed w/ interfaces
        # for (opt, val) in options.items():
        #     if val:
        #         if opt = 'run_all':
        #             text  = True
        #             audio = True
        #             video = True
        #             break
        #         elif opt = 'text':
        #             text = True
        #         elif opt = 'audio':
        #             audio = True
        #         elif opt = 'video':
        #             video = True

        t = t_int()
        a = a_int()
        v = v_int()

        a.process_filepath(self.audio_out, {'run_all': True, 'challenge_id': challenge_id})
        a_json = a.to_json()
        a_dict = json.loads(a_json)

        stt = a.get_transcript()
        #print("text_to_speech: {}".format(stt))
        print("audio_dict: {}\n".format(a_dict))

        t_json = t.process_filepath(stt, {'run_all': True, 'challenge_id': challenge_id})
        t_dict = json.loads(t_json)
        print("text_dict: {}\n".format(t_dict))

        v_dict = v.process_filepath(fp, {'run_all': True, 'challenge_id': challenge_id})
        print("video_dict: {}\n".format(v_dict))

        final_dict = {}
        final_dict['audio'] = a_dict
        final_dict['video'] = v_dict
        final_dict['text' ] = t_dict


        print("\n\n Final results dictionary: \n\n {} \n".format(final_dict))
        return final_dict


        

    @staticmethod
    # Returns tuple of (status, audioout [path]) ex: no file => (-1, "./backend_audio_out.wav"), there is a file => (0, "./backend_audio_out.wav")
    # Status = -1 if shit got fucked, 0 otherwise
    def decouple_av(videoin):
        audio_out = "./backend_audio_out.wav"
        if Interface.check_fp(videoin) == -1:
            return (-1, audio_out)


        av_cmd = "ffmpeg -i " + videoin + " -ab 160k -ac 2 -ar 44100 -vn -y " + audio_out

        subprocess.call(av_cmd, shell=True)
        return (0, audio_out)

    @staticmethod
    def check_fp(path):
        if os.path.isfile(path) and os.access(path, os.R_OK):
            return 0
        else:
            print("Warning: Either file is missing or is not readable")
            return -1

video_in = "../research/enigma_rkemper_take2.mov"
i = Interface()
i.process_filepath(video_in, {'run_all':True, 'challenge_id':'enigma_tc_transcript.txt'})

# Virtual Environment
	# pip3 install watson-developer-cloud 	        # Text and Audio
	# pip3 install opencv-python		            # Video
    # pip3 install --upgrade google-cloud-vision    # Video
    # export GOOGLE_APPLICATION_CREDENTIALS=YOUR_LOCAL_DIRECTORY/logmein-capstone_2017-18/Backend/Video/google_api_credentials.json
	# pip3 install google-cloud		                # Video, not positive if needed
