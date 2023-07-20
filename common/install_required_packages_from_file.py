#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-07-20
#####

## Import libraries
import sys, subprocess, traceback


## Install required packages
def install_required_packages_from_file(requirements_file_path = './requirements.txt') -> bool:
    # Initialise output
    required_packages_installed = False
    try:
        # Install
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', '-r', requirements_file_path], stdout=subprocess.DEVNULL)
    except:
        traceback.print_exc()
    # return
    return required_packages_installed