from demucs import demucs
from pydub import AudioSegment
from pathlib import Path
import os
import threading

def separate_audio(input_file, output_folder):
    model = demucs()
    # Load the model weights
    model_path = os.path.join(output_folder, "demucs.th")
    model.load(model_path)

    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Separate the audio sources
    sources = model(audio)

    # Save the separated sources
    for i, source in enumerate(sources):
        source_path = os.path.join(output_folder, f"source_{i+1}.wav")
        source.export(source_path, format='wav')

def main():
    input_folder = Path('C:/Users/mikes/Desktop/Create Stems Testing/Audio In/')
    output_folder = Path('C:/Users/mikes/Desktop/Create Stems Testing/Audio Out/demucs')

    mp3_file = input_folder / 'Gel - Collective Soul.mp3'
    wav_file = input_folder / 'Gel - Collective Soul.wav'

    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format='wav')

    input_file = str(wav_file)
    output_folder = str(output_folder)

    separate_thread = threading.Thread(target=separate_audio, args=(input_file, output_folder))
    separate_thread.start()
    separate_thread.join()

if __name__ == '__main__':
    main()
