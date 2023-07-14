from pydub import AudioSegment


def main():
    mp3_file = 'Limelight.mp3'
    wav_file = 'Limelight.wav'

    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format='wav')


    from spleeter.separator import Separator

    input_file = 'Limelight.wav'
    output_folder = 'output/'

    separator = Separator('spleeter:4stems')
    separator.separate_to_file(input_file, output_folder)

if __name__ == '__main__':
    # Add the freeze_support() call
    from multiprocessing import freeze_support
    freeze_support()

    main()
