import sys
import os, os.path
import subprocess
import json

# Import our backend interfaces

from text  import Interface as t_int
from audio import Interface as a_int
#from Video import Interface as v_int


class Interface:

    def __init__(self):
        print("__init__ [backend]: STUB")
        self.audio_out = "./backend_audio_out2.wav"

    def process_filepath(self, fp, options):
        text  = False
        audio = False
        video = False

        status = Interface.decouple_av(fp)

        if (status[0] == -1):
            print("Shit is seriously fucked. We don't have a video file.")
            return status

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
        # v = v_int()

        a.process_filepath(self.audio_out, {'run_all': True})
        a_json = a.to_json()
        a_dict = json.loads(a_json)

        script = a.get_transcript()
        print("text_to_speech: {}".format(script))

        t_json = t.process_filepath(script, {'run_all': True})
        t_dict = json.loads(t_json)

        final_dict = {}
        final_dict.append(t_dict)
        final_dict.append(a_dict)

        print(final_dict)
        #return final_dict




        

    @staticmethod
    # Returns tuple of (status, audioout [path]) ex: no file => (-1, "./backend_audio_out.wav"), there is a file => (0, "./backend_audio_out.wav")
    # Status = -1 if shit got fucked, 0 otherwise
    def decouple_av(videoin):
        audio_out = "./backend_audio_out2.wav"
        if Interface.check_fp(videoin) == -1:
            return (-1, audio_out)


        av_cmd = "ffmpeg -i " + videoin + " -ab 160k -ac 2 -ar 44100 -vn " + audio_out

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
i.process_filepath(video_in, {'run_all':True})