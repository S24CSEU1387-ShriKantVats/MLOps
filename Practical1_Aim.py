import sys
import importlib.metadata

#Python version installed and used.
print("Python Version Installed And Currently Being Used:")
print("_________________________________________________")
print(f"Python version: {sys.version}") 
print("_________________________________________________")

print("##################################################")

print("Python Modules Installed:")
print("_________________________________________________")

#List all installed libraries and their versions.
print("Library Used:")  
for dist in importlib.metadata.distributions():
    print(f"{dist.metadata['Name']}=={dist.version}")
 
print("_________________________________________________")
