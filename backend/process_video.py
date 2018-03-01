#!/usr/bin/env python3
from interface import Interface

video_in = "../research/enigma_rkemper_take2.mov"
i = Interface()
i.process_filepath(video_in, {'run_all':True, 'challenge_id':'enigma_tc_transcript.txt'})

# VIRTUAL ENVIRONMENT
    # pip3 install watson-developer-cloud           # Text and Audio
    # pip3 install opencv-python                    # Video
    # pip3 install --upgrade google-cloud-vision    # Video
    # export GOOGLE_APPLICATION_CREDENTIALS=$HOME/logmein-capstone_2017-18/Backend/Video/google_api_credentials.json
    # pip3 install google-cloud                     # Video, not positive if needed (probably not)