## Reference to the common python packages folder
import sys, pathlib, os 
path = str(pathlib.Path(pathlib.Path(__file__).parent.absolute()).parent.absolute()) + os.sep+'Python-packages'
sys.path.insert(0, path)
print(path)