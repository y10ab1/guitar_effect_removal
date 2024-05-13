---
layout: post
title: Guitar effect removal
---

# Distortion Recovery: A Two-Stage Method for Guitar Effect Removal

Listen to the samples below to compare the results of different guitar effect removal models.

## Contents:
- [Section 1: Comparison of different models](#section-1)

## Notes:
- All samples are provided for demonstration purposes.
- For the best experience, use headphones or high-quality speakers.

---

## Section 1: Comparison of different models

Description of the samples.

### Samples

| Wet | Dry | Ours | HifiGAN denoiser | Demucs V3 | DCUnet |
|-----|-----|------|------------------|-----------|--------|
| {% include audio_player.html filename="samples/wet/632f4bd7ec54540015a63a0a-aug_57.wav"%} | {% include audio_player.html filename="samples/dry/632f4bd7ec54540015a63a0a-aug_57.wav"%} | {% include audio_player.html filename="samples/mel2mel_hifigan_finetune/632f4bd7ec54540015a63a0a-aug_57.wav"%} | {% include audio_player.html filename="samples/hifigan-denoiser/632f4bd7ec54540015a63a0a-aug_57.wav"%} | {% include audio_player.html filename="samples/Demucs_pred/632f4bd7ec54540015a63a0a-aug_57.wav"%} | {% include audio_player.html filename="samples/DCUNet_pred/632f4bd7ec54540015a63a0a-aug_57.wav"%} |
| {% include audio_player.html filename="samples/wet/631f6fe629df2500152e47ef-aug_43.wav"%} | {% include audio_player.html filename="samples/dry/631f6fe629df2500152e47ef-aug_43.wav"%} | {% include audio_player.html filename="samples/mel2mel_hifigan_finetune/631f6fe629df2500152e47ef-aug_43.wav"%} | {% include audio_player.html filename="samples/hifigan-denoiser/631f6fe629df2500152e47ef-aug_43.wav"%} | {% include audio_player.html filename="samples/Demucs_pred/631f6fe629df2500152e47ef-aug_43.wav"%} | {% include audio_player.html filename="samples/DCUNet_pred/631f6fe629df2500152e47ef-aug_43.wav"%} |
| {% include audio_player.html filename="samples/wet/6328b0b53467be00153923f4-aug_17.wav"%} | {% include audio_player.html filename="samples/dry/6328b0b53467be00153923f4-aug_17.wav"%} | {% include audio_player.html filename="samples/mel2mel_hifigan_finetune/6328b0b53467be00153923f4-aug_17.wav"%} | {% include audio_player.html filename="samples/hifigan-denoiser/6328b0b53467be00153923f4-aug_17.wav"%} | {% include audio_player.html filename="samples/Demucs_pred/6328b0b53467be00153923f4-aug_17.wav"%} | {% include audio_player.html filename="samples/DCUNet_pred/6328b0b53467be00153923f4-aug_17.wav"%} |

Note: Add more rows as needed for your samples.
