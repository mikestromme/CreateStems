from spleeter.separator import Separator
from pydub import AudioSegment
from pathlib import Path
import tensorflow as tf 
import numpy as np
import os


def main():

    # Set the paths to ffmpeg and ffprobe in your script
    os.environ["PATH"] += os.pathsep + "C:/ffmpeg/bin"
    AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"
    AudioSegment.ffprobe   = "C:/ffmpeg/bin/ffprobe.exe"


    input_folder = Path(f'C:/Users/mstromme/OneDrive/Music/Create Stems Testing/Audio In')
    output_folder = Path(f'C:/Users/mstromme/OneDrive/Music/Create Stems Testing/Audio Out/spleeter')
    mp3_file = input_folder / 'Gel - Collective Soul.mp3'
    wav_file = input_folder / 'Gel - Collective Soul.wav'

    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format='wav')
    

    input_file = input_folder / 'Gel - Collective Soul.wav'    

    separator = Separator('spleeter:4stems')
    separator.separate_to_file(input_file, output_folder)

if __name__ == '__main__':
    # Add the freeze_support() call
    from multiprocessing import freeze_support
    freeze_support()

    main()
