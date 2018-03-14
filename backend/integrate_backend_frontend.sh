# Script to integrate backend for us

    # replace imports in interface.py

    sed -i'.bak' 's/from text  import Interface as t_int/from backend.text  import interface as t_int/'   Interface.py
    sed -i'.bak' 's/from audio import Interface as a_int/from backend.audio import interface as a_int/' Interface.py
    sed -i'.bak' 's/from Video import Interface as t_int/from backend.Video import Interface as t_int/'  Interface.py

    # replace text initialization in interface.py

    sed -i'.bak' 's/t = t_int()/t = t_int.Interface()/' Interface.py
    sed -i'.bak' 's/a = a_int()/a = a_int.Interface()/' Interface.py

    # add # to each line in __init__.py
        # looks like $ sed -i'.bak' 's/^/#/' file.txt [https://linuxconfig.org/add-character-to-the-beginning-of-each-line-using-sed]

    sed -i'.bak' 's/^/#/' __init__.py

# Old int examples
#from backend.text  import interface as t_int
#from backend.audio import interface as a_int
#from backend.Video import Interface as v_int
#t = t_int.Interface()
#a = a_int.Interface()

# for historical purposes: this is officially the hackiest sed command I've ever written
    # sed -i'.bak' 's/sed -i/sed -i'\''.bak'\''/' integrate_backend_frontend.sh