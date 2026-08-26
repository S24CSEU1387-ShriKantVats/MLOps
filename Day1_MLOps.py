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
print("Standard Library Modules:") 
std_lib_modules = sorted(sys.stdlib_module_names) 
for mod in std_lib_modules:
    print(mod)
 
print("_________________________________________________")
