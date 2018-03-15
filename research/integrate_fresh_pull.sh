# Requires your paths_CONST.py in directory above stagepresence
# Copies paths const => uses sed to fix import differences between backend and frontend => optionally runs router.py

echo "Copying paths_CONST.py over\n"
cp $HOME/CS189AB/paths_CONST.py $HOME/CS189AB/stagepresence/web-services/backend/paths_CONST.py
cd $HOME/CS189AB/stagepresence/web-services/backend/
echo "Done copying paths_CONST.py over\n"
pwd
echo "About to run integrate_backend_frontend.sh\n"
source ./integrate_backend_frontend.sh
echo "Done running integrate_backend_frontend.sh\n\n"

read -p "Press any key to autorun router.py, or hit CTRL+C to gtfo" -n1 -s
cd ../../
python3 web-services/router.py

