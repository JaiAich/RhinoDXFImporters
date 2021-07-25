#! python3
import subprocess
import sys
import os
import tkinter
from tkinter import Tk
from tkinter.filedialog import askdirectory
import shutil

'''
How to run this script (README):

->Run from command line / WIN + R and select folder containing DXF files (no containing subfolders).
->Once the parts have imported copy them from their current rhino file to second open rhino file named
something like all parts etc.
-> Repeat this for all DXF files as required which should result in all parts contained within the all parts
file.
-> Manual renaming of parts is required e.g. MLD32 104F etc.
-> Once complete proceed with nesting onto sheets and finish by running parts labeler script.
'''

print("\nPlease select the folder containing all the DXF files to be imported using the pop up selection box")

# Select folder contatining all DXF files
while True:
	try:
		tkinter.Tk().withdraw()
		DXF_folder = askdirectory(title='Select folder')
		extensions = ['.dxf']
		DXF_files = [fn for fn in os.listdir(DXF_folder) if any(fn.endswith(ext) for ext in extensions)]
		break
	except:
		print("\nFolder selection did not register please try again!")


DXF_folder = DXF_folder.replace("/","\\")
f = open(#~~~'DXF files reference text file'~~~,'w')
f.write(DXF_folder + "\\" + "\n")

for i in range(len(DXF_files)):
        f.write(DXF_files[i]+"\n")

f.close()

# Define rhino.exe path and rhinoscript path
rhinoPath = #~~~"Rhino.exe path"~~~
scriptName = #~~~"Path to DXF importer.py file~~~\\DXFimporter.py"
scriptCall = "-_RunPythonScript {0}".format(scriptName)

# Opens a single instance of Rhino with no splash screen
callscript = '"{0}" /nosplash /runscript="{1}"'.format(rhinoPath, scriptCall)
subprocess.call(callscript)
