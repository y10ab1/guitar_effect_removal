import torch
import torchaudio
import numpy as np
import lightning as l
import os

from auraloss.time import SISDRLoss, ESRLoss
from auraloss.freq import MultiResolutionSTFTLoss
from frechet_audio_distance import FrechetAudioDistance

from collections import defaultdict

class TestModel():
    def __init__(self, sample_rate=44100, **kwargs) -> None:
        super().__init__()
        self.sisdr = SISDRLoss()
        self.esr = ESRLoss()
        self.mrstftloss = MultiResolutionSTFTLoss(
            fft_sizes=[1024, 2048, 8192],
            hop_sizes=[256, 512, 2048],
            win_lengths=[1024, 2048, 8192],
            scale="mel",
            n_bins=128,
            sample_rate=sample_rate,
            perceptual_weighting=True,
        )
        

    def compute_metrics(self, pred, dry):
        sisdr_value = torch.round(self.sisdr(pred, dry).cpu(), decimals=3)
        esr_value = torch.round(self.esr(pred, dry).cpu(), decimals=3)
        mrstft_value = torch.round(self.mrstftloss(pred, dry).cpu(), decimals=3)
        return sisdr_value, esr_value, mrstft_value

    def test_model(self, dry_folder, recovered_folder):
        results = defaultdict(list)
        for wav in os.listdir(recovered_folder):
            recovered_path = os.path.join(recovered_folder, wav)
            dry_path = os.path.join(dry_folder, wav)
            assert recovered_path.split('/')[-1] == dry_path.split('/')[-1], "File names do not match"
            if os.path.exists(dry_path):
                pred = torchaudio.load(recovered_path)[0].unsqueeze(0)
                dry = torchaudio.load(dry_path)[0]

                sisdr_value, esr_value, mrstft_value = self.compute_metrics(pred, dry)
                results['sisdr'].append(sisdr_value.item())
                results['esr'].append(esr_value.item())
                results['mrstft'].append(mrstft_value.item())
        
        avg_sisdr = np.mean(results['sisdr'])
        avg_esr = np.mean(results['esr'])
        avg_mrstft = np.mean(results['mrstft'])
        print(f"Average SISDR: {round(avg_sisdr, 3)}")
        print(f"Average ESR: {round(avg_esr, 3)}")
        print(f"Average MRSTFT: {round(avg_mrstft, 3)}")

if __name__ == '__main__':
    l.pytorch.seed_everything(42)
    model = TestModel(44100)
    frechet = FrechetAudioDistance(
        model_name="clap",
        sample_rate=48000,
        submodel_name="630k-audioset",  # for CLAP only
        verbose=False,
        enable_fusion=False,            # for CLAP only
    )
    print("----------Testing----------")
    dry_folder = '/home/yuehpo/coding/gremfx/output_EGDB_ft2/tmp_dry'
    recovered_folder = '/home/yuehpo/coding/gremfx/output_EGDB_ft2/tmp_Fastspeech_pred'
    recovered_folder = '/home/yuehpo/coding/gremfx/output_EGDB_ft2/tmp_Demucs_pred'
    model.test_model(dry_folder, recovered_folder)
    

    
    fad_score = frechet.score(dry_folder, recovered_folder, dtype="float32")
    print(f"FAD Score: {round(fad_score, 3)}")