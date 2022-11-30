#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-30
#####

## Import libraries
import sys, subprocess, pkg_resources


## Install required packages
def install_required_packages(list_of_packages: list[str]) -> None:
    # Convert to set
    required_packages = set(list_of_packages)
    # check installed packages
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    # compared with missing packages
    missing_packages = required_packages - installed_packages
    # if there are missing packages, proceed with installation
    if missing_packages:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing_packages], stdout=subprocess.DEVNULL)