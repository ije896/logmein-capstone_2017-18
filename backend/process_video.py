#!/usr/bin/env python3
from interface import Interface
import subprocess
import re           # to get video duration, bitrate

class Process_Video:

    def __init__(self, video_path, audio_path):
        self.video_in    = video_path
        self.audio_out   = audio_path
        self.debug_level = 2

        self.duration = self.get_vid_duration() # secs
        self.bitrate  = self.get_vid_bitrate () # kbps 

        self.results_iface = None # Will get initialized in following analyze_video() call
        self.results       = self.analyze_video() # analyze_video() => result as dictionary

        self.outp_bench = True # Determines if we print out benchmarks

    def analyze_video(self):
        self.results_iface = Interface()
        return self.results_iface.process_filepath({'run_all':True, 'challenge_id':'enigma_tc_transcript.txt', 'video_in':self.video_in, 'audio_out':self.audio_out})

    # Returns duration of video in seconds by parsing an ffmpeg cmd
    def get_vid_duration(self):

        if Interface.check_fp(self.video_in) == -1:
            return -1

        av_cmd = "ffmpeg -i {} 2>&1 | grep 'Duration'".format(self.video_in)

        result = subprocess.getoutput(av_cmd)


        duration_regex = re.compile('\d\d:\d\d:\d\d.\d\d')
        duration = duration_regex.findall(result)[0] # grab the duration part, which should only have 1 result
        self.debug("get_vid_duration(): result = {}".format(duration), 1)

        hours = int(duration[0:2])
        mins  = int(duration[3:5])

        whole_secs = int(duration[-5:-3]) # chop off  the fractional part
        fract_secs = int(duration[-2:])   # keep only the fractional part

        total_secs = (hours * 60**2) + (mins * 60) + whole_secs + fract_secs/100

        self.debug("hours = {}, mins = {}, whole_secs = {}, fract_secs = {}, total_secs = {}".format(hours, mins, whole_secs, fract_secs, total_secs), 1)

        return total_secs

    def get_vid_bitrate(self):
        if Interface.check_fp(self.video_in) == -1:
            return -1

        av_cmd = "ffmpeg -i {} 2>&1 | grep 'Duration'".format(self.video_in)

        result = subprocess.getoutput(av_cmd)

        bitrate_str = re.findall('bitrate: \d*', result)[0] # grab the bitrate part, which should only have 1 result

        self.debug("get_vid_bitrate(): bitrate_str = {}\n".format(bitrate_str), 2)

        bitrate = int(re.findall('\d\d\d\d', bitrate_str)[0])

        kbps_regex = re.compile('kb')
        kbps = kbps_regex.findall(result)

        if len(kbps) <= 0:
            print("\nWARNING: ffmpeg did not give result in kbps. Bitrate values cannot be trusted. \n")
            return -1

        self.debug("get_vid_bitrate(): bitrate_val = {} kb/s\n".format(bitrate), 1)

        return bitrate

    def get_decouple_bench(self):
        return self.results_iface.decouple_bench

    def get_audio_bench(self):
        return self.results_iface.audio_bench

    def get_video_bench(self):
        return self.results_iface.video_bench

    def get_text_bench(self):
        return self.results_iface.text_bench

    def debug(self, debug_message, debug_flag):
        if (self.debug_level >= debug_flag):
            print(debug_message)

if __name__ == "__main__":

    video_in  = "../research/Enigma_Rallen.mov"
    audio_out = "./backend_audio_out.wav"
    pv = Process_Video(video_in, audio_out)

    print("\n\nBENCHMARKS\n\n")
    print("decouple: {}s, audio: {}s, video: {}s, text: {}s".format(pv.get_decouple_bench(), pv.get_audio_bench(), pv.get_video_bench(), pv.get_text_bench()))


# TEST VIDEOS
    # "../research/enigma_rkemper_take2.mov"
    # "../research/Enigma_Rallen.mov"

# VIRTUAL ENVIRONMENT
    # pip3 install watson-developer-cloud           # Text and Audio
    # pip3 install opencv-python                    # Video
    # pip3 install --upgrade google-cloud-vision    # Video
    # export GOOGLE_APPLICATION_CREDENTIALS=$HOME/logmein-capstone_2017-18/Backend/Video/google_api_credentials.json
    # pip3 install google-cloud                     # Video, not positive if needed (probably not)


