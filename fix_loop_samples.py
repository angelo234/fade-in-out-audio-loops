import os

from pathlib import Path

from os import listdir
from os.path import isfile, join

import urllib.request

from pydub import AudioSegment
from pydub.playback import play

from tkinter import filedialog
from tkinter import *

fade_time_fraction = float(input("Type in the fade in/out time as a fraction of the samples' length. (e.g. type 0.02 for 2% fade in/out time of audio length)"))

root = Tk()
root.withdraw()
root.filename = filedialog.askdirectory()

onlyfiles = [f for f in listdir(root.filename) if isfile(join(root.filename, f))]

export_folder = root.filename + "/" + "{:.5f}".format(fade_time_fraction) + "_fadeinout_samples/"

Path(export_folder).mkdir(parents=True, exist_ok=True)

for filename in onlyfiles:
	file_path = root.filename + "/" + filename

	# Load into PyDub
	loop = AudioSegment.from_wav(file_path)

	fade_time = len(loop) * fade_time_fraction
	
	# Fade in and out
	faded = loop.fade_in(fade_time).fade_out(fade_time)

	faded.export(export_folder + filename, format="wav")
