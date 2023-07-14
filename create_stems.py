from pydub import AudioSegment
from pathlib import Path


def main():
    input_folder = Path('input/')
    output_folder = Path('output/')
    mp3_file = input_folder / 'Limelight.mp3'
    wav_file = input_folder / 'Limelight.wav'

    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format='wav')


    from spleeter.separator import Separator

    input_file = input_folder / 'Limelight.wav'
    

    separator = Separator('spleeter:4stems')
    separator.separate_to_file(input_file, output_folder)

if __name__ == '__main__':
    # Add the freeze_support() call
    from multiprocessing import freeze_support
    freeze_support()

    main()
