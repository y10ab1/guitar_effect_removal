import os
import torchaudio
import torch
from glob import glob

def normalize_audio_by_peak(audio_path):
    # Load audio file
    waveform, sample_rate = torchaudio.load(audio_path)
    
    # Normalize the waveform by its peak
    peak = waveform.abs().max()
    if peak > 0:
        waveform = waveform / peak
        
    # pad the waveform to have the same length (sr * 4)
    waveform = torch.nn.functional.pad(waveform, (0, sample_rate * 4 - waveform.size(1)), 'constant', 0)
    
    # Save the normalized waveform to the original file
    torchaudio.save(audio_path, waveform, sample_rate)



# seach all dir
for filename in glob('**/*.wav', recursive=True):
    normalize_audio_by_peak(filename)
    print(f'Normalized and saved: {filename}')

# # Define the directory containing audio samples
# audio_dir = 

# # Iterate over the files in the directory
# for filename in os.listdir(audio_dir):
#     if filename.endswith('.wav'):  # Change this to the appropriate file extension
#         file_path = os.path.join(audio_dir, filename)
#         normalize_audio_by_peak(file_path)
#         print(f'Normalized and saved: {file_path}')
