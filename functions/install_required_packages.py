## Import libraries
import sys, subprocess, pkg_resources

## Install required packages
def install_required_packages(required_packages: list[str]) -> None:
    # Convert to set
    required_packages = set(required_packages)
    # check installed packages
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    # compared with missing packages
    missing_packages = required_packages - installed_packages
    # if there are missing packages, proceed with installation
    if missing_packages:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing_packages], stdout=subprocess.DEVNULL)