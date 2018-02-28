import sys
import os, os.path
import subprocess
import json

# Import our backend interfaces

from text  import Interface as t_int
from audio import Interface as a_int
from Video import Interface as v_int


class Interface:

    def __init__(self):
        print("__init__ [backend]: STUB")
        self.audio_out = "./backend_audio_out.wav"

    def process_filepath(self, fp, options):
        challenge_id = options['challenge_id']
        tts_path = "../research/{}.tts".format(challenge_id)

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

        tts = a.get_transcript()
        #print("text_to_speech: {}".format(tts))
        print("audio_dict: {}\n".format(a_dict))

        #tts = "I want to show you the new money is also about discovering new data sets you need to know where relevant or existed right so you can see this growing all this that you can build a rich portrait of a company like Google checkout FCC licenses maybe the latest registration for Google classes in there or you know loving records you would use Google's behind how much money is actually committing to them you know private investments where you can knock out all of Google's subsidiaries but there's something that caught our attention and we actually saw Google popping up in this department energy data set let's go take a look okay now we're looking at each and every single electricity contract purchase agreement in the United States and relearning Google's actually operating like utility buying electricity directly for itself as a registered utility and let's see who is buying electricity from there's a lot of good companies in there and they're all right and we know the tools and really really been pushing toward sustainability and all its operations but now now we see it play out data we can do things with enigma like break down how many megawatts were delivered to which facilities and how far these contracts are hedged on the future let's stop for a second I want to show you how we get to this sort of insight without even being on the web right so what if I were just browsing the internet and going to the Google green baskets webpage where this browser plugin soon as you activate all the entities and page just light up companies people locations in this case we can just click on clean power finance which Google invested in and year out about to everywhere it hits an enigma let's go check out you know government grants for the specific project see what sort of money was received and there you have it that's just a taste of what we can do the neck not you know so many companies a pioneer how analyze the world with data but what we're trying to do what we're trying to stir up to something much deeper in the stock right so fundamental issues in the structure and content itself"


        t_json = t.process_filepath(tts, {'run_all': True, 'challenge_id': challenge_id})
        t_dict = json.loads(t_json)
        print("text_dict: {}\n".format(t_dict))

        v_json = v.process_filepath(fp, {'run_all': True, 'challenge_id': challenge_id})
        v_dict = json.loads(v_json)
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
i.process_filepath(video_in, {'run_all':True, 'challenge_id':'enigma_tc_transcript.txt'})

# Virtual Environment
	# pip3 install watson-developer-cloud 	        # Text and Audio
	# pip3 install opencv-python		            # Video
    # pip3 install --upgrade google-cloud-vision    # Video
    # export GOOGLE_APPLICATION_CREDENTIALS=YOUR_LOCAL_DIRECTORY/logmein-capstone_2017-18/Backend/Video/google_api_credentials.json
	# pip3 install google-cloud		                # Video, not positive if needed
