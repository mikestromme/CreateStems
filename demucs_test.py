import torch
from demucs import pretrained
import librosa

# Load a pre-trained model
model = pretrained.load_pretrained('demucs')

# Load an audio file and resample it to 44100 Hz
audio, _ = librosa.load('Gel - Collective Soul.wav', sr=44100)

# Convert the audio data to a torch tensor
audio = torch.tensor(audio)

# Separate the audio into stems
with torch.no_grad():
    stems = model(audio)
