## Integrating backend with frontend

1) Pull fresh copy of (new) backend from github (master branch)

2) (in stagepresence) move backend to oldbackend

3) move (new) backend directory to stagepresence

4) cd into the directory above stage presence

5) make sure your paths_CONST.py is also in the dir above stagepresence

6) Change the two filepaths in integrate\_fresh\_pull.sh to match your structure

6) run integrate\_fresh\_pull.sh. It will copy your paths_CONST to backend, then use sed to modify \_\_init\_\_.py and backend/interface.py, then optionally autorun router.py for integration testing

## You should be done now.