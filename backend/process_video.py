#!/usr/bin/env python3
from interface import Interface
import subprocess
import re           # to get video duration, bitrate
import time         # Benchmarking
import os


class Process_Video:

    def __init__(self, video_path, audio_path):
        self.video_in    = video_path
        self.audio_out   = audio_path
        self.debug_level = 2
        self.log_results = True

        self.duration = self.get_vid_duration()   # secs
        self.bitrate  = self.get_vid_bitrate ()   # kbps 

        self.results_iface = None                 # Will get initialized following analyze_video() call
        self.results       = self.analyze_video() # analyze_video(self) => result as dictionary

        self.outp_bench = True # Determines if we print out benchmarks

    def analyze_video(self):
        self.results_iface = Interface()
        return self.results_iface.process_filepath({'run_all':True, 'challenge_id':'sally_sells_twister.txt', 'video_in':self.video_in, 'audio_out':self.audio_out})

    # Returns duration of video in seconds by parsing an ffmpeg cmd
    def get_vid_duration(self):

        if Interface.check_fp(self.video_in) == -1:
            return -1

        av_cmd = "ffmpeg -i {} 2>&1 | grep 'Duration'".format(self.video_in)

        result = subprocess.getoutput(av_cmd)


        duration_regex = re.compile('\d\d:\d\d:\d\d\.\d\d')
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

        bitrate_str = re.findall('bitrate: \d+', result)[0] # grab the bitrate part, which should only have 1 result

        self.debug("get_vid_bitrate(): bitrate_str = {}\n".format(bitrate_str), 2)

        bitrate_match = re.findall('\d+', bitrate_str)
        if (len(bitrate_match) <= 0):
            print("\nWARNING: could not match on bitrate.\n")
        bitrate = int(bitrate_match[0])

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

    video_in  = "../research/sally_sells_twister.mp4"
    audio_out = "./backend_audio_out.wav"
    start = time.time()
    pv = Process_Video(video_in, audio_out)
    end   = time.time()

    print("\n\nBENCHMARKS\n\n")
    dc = pv.get_decouple_bench()
    au = pv.get_audio_bench   ()
    vi = pv.get_video_bench   ()
    tx = pv.get_text_bench    ()

    # TODO: fix metrics now that we're parallelizing (numbers are wrong)
    
    real_time = end - start
    linear_time = dc + au + vi + tx
    # threaded metric: Assume we run audio/video at same time (text is too fast to benefit from async threading)
    if (au + tx > vi):
        threaded = linear_time - vi     
    else:
        threaded = linear_time - au - tx
    dur = pv.duration
    bit = pv.bitrate

    dur_bit = dur * bit

    outp = "\n\n"

    outp += "[modules times] decouple: {}s, audio: {}s, video: {}s, text: {}s\n".format(dc, au, vi, tx)
    outp += "[module times] total linear time: {}s \t [parallel times] (actual time): {}s \t TIME SAVED:{}\n".format(linear_time, real_time, linear_time-real_time)
    outp += ("duration: {}s, bitrate: {} kb/s\n".format(dur, bit))

    outp += ("[ACTUAL] thread_time / duration: {}, thread_time / (duration * bitrate): {}, [LINEAR] real_time / duration: {}, real_time / (duration * bitrate): {}\n".format(real_time/dur, real_time/dur_bit, linear_time/dur, linear_time/dur_bit))

    print(outp)

    if (pv.log_results):
        import hashlib

        sha1 = hashlib.sha1()

        BUF_SIZE = 65536  # read stuff in 64kb chunks!
        with open(video_in, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha1.update(data)

        vid_hash = sha1.hexdigest()

        print("\nVideo={} => SHA1={}\n".format(video_in, vid_hash))

        vid_results_path = "./results/{}".format(vid_hash)        
        # write results to video_path

        print("\n[process_video] about to write results to {}\n".format(vid_results_path))
        os.makedirs(os.path.dirname(vid_results_path), exist_ok=True) # Will make dir if it doesn't exist, won't complain if it does exist
        with open (vid_results_path, 'a') as report:
            report.write(outp)
            print("\n done writing \n")


# TEST VIDEOS
    # "../research/enigma_rkemper_take2.mov"
    # "../research/Enigma_Rallen.mov"

# VIRTUAL ENVIRONMENT
    # pip3 install watson-developer-cloud           # Text and Audio
    # pip3 install opencv-python                    # Video
    # pip3 install --upgrade google-cloud-vision    # Video
    # export GOOGLE_APPLICATION_CREDENTIALS=$HOME/logmein-capstone_2017-18/Backend/Video/google_api_credentials.json
    # pip3 install google-cloud                     # Video, not positive if needed (probably not)


