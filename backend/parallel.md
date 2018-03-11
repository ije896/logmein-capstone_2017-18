MULTIPROCESS - decouple & convert to mp4 (if necessary) at same time
THREADING    - audio->text, video
    (Python has a Global Interpreter Lock restricting execution within process to 1 core, but our api calls are IO bound and so the lock should get relesaed while waiting for IO)

TODO:
    - fix audio interval error (short videos crash)
    - multiprocess decouple and convert to mp4 if necessary