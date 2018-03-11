import sys
import os, os.path
import subprocess
import json

# Import our backend interfaces

from text  import Interface as t_int
from audio import Interface as a_int
from Video import Interface as v_int


# Parallelization
import threading


# Benchmarking
import time 


# TODO:
    # - have audio automatically pull credentials.json instead of hardcoding
    # - benchmarking by module
        # - test harness to collect data for relationship btw video length and processing times (prob not quite linear)
    # (optional) make a "config" txt file that sets audio_out, video_in, and the link to our "scripts" directory (which contains the script for each challengeid)
    # (optional) set audio_out to be sha1 hash of video - this will help us avoid namespace collisions and also avoid re-running analysis for a previously processed video

class Interface:

    def __init__(self):
        self.benchmark = True
        # benchmarks in seconds
        self.decouple_bench = -1
        self.video_bench    = -1
        self.audio_bench    = -1
        self.text_bench     = -1


    # Returns (audio_dict, text_dict) on success
    def proc_audio_text(self, a, t, audio_out, challenge_id):
        print("[debug] proc_audio_text({}, {}, {})\n".format(a, audio_out, challenge_id))
        start = time.time()
        print("[debug] proc_audio_text: starting\n")
        a.process_filepath(audio_out, {'run_all': True, 'challenge_id': challenge_id})
        print("[debug] proc_audio_text: ending\n")
        self.audio_bench = time.time() - start

        a_json = a.to_json()
        a_dict = json.loads(a_json)

        stt = a.get_transcript()
        print("audio_dict: {}\n".format(a_dict))

        start = time.time()
        t_dict = t.process_filepath(stt, {'run_all': True, 'challenge_id': challenge_id})
        self.text_bench = time.time() - start

        print("text_dict: {}\n".format(t_dict))

        return (a_dict, t_dict)

    # Returns video_dict on success
    def proc_video(self, v, video_in, challenge_id, v_dict_retval):
        print("[debug] proc_video({}, {}, {})\n".format(v, video_in, challenge_id))
        start = time.time()
        print("[debug] proc_video: starting\n")
        v_dict = v.process_filepath(video_in, {'run_all': True, 'challenge_id': challenge_id})
        print("[debug] proc_video: ending\n")
        self.video_bench = time.time() - start

        print("video_dict: {}\n".format(v_dict))

        v_dict_retval = v_dict # ugly hack b/c join doesn't return
        return v_dict



    def process_filepath(self, options):
        challenge_id = options.get('challenge_id', None)
        video_in     = options.get('video_in',     None)
        audio_out    = options.get('audio_out',    None)

        if challenge_id is None:
            print("ERROR: No challenge_id provided. Exiting\n")
            return -1

        if video_in is None:
            print("ERROR: No video_in provided. Exiting\n")
            return -1

        if audio_out is None:
            print("ERROR: No audio_out provided. Exiting\n")
            return -1

        stt_path = "../research/{}.stt".format(challenge_id)

        text  = False
        audio = False
        video = False

        start = time.time()
        decouple_status = Interface.decouple_av(video_in, audio_out)
        self.decouple_bench = time.time() - start

        if (decouple_status[0] == -1):
            print("ERROR: no video file at given filepath. Exiting\n")
            return decouple_status[0]

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

        v_dict = {}

        # Spawn a video thread and run audio_text in the main execution thread
        video      = threading.Thread(target=self.proc_video, args=(v, video_in, challenge_id, v_dict))

        video.start()
        a_dict, t_dict = self.proc_audio_text(a, t, audio_out, challenge_id)

        video.join()

        final_dict = {}
        final_dict['audio'] = a_dict
        final_dict['video'] = v_dict
        final_dict['text' ] = t_dict


        print("\n\n Final results dictionary: \n\n {} \n".format(final_dict))

        return final_dict

    @staticmethod
    # Returns tuple of (status, audioout [path]) ex: no file => (-1, ""), there is a file => (0, "./backend_audio_out.wav")
    # Status = -1 if shit got fucked, 0 otherwise
    def decouple_av(videoin, audio_out):
        if Interface.check_fp(videoin) == -1:
            return (-1, "")


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
