# Guitar Effect Removal Evaluation

This repository contains code for evaluating the recovery of clean guitar tones from wet guitar tones using various metrics. The script calculates metrics such as SISDR, ESR, and MRSTFTLoss, and also computes the Frechet Audio Distance (FAD) score.

## Installation

To install pytorch, run the following command:

```bash
pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu118
```

To install the other required packages, run the following command:

```bash
pip install -r requirements.txt
```

## Data

To evaluate the additional experiments on the EGDB dataset, download the dry siganl and recovered results from this [Google Drive](https://drive.google.com/drive/folders/1_NOPoomWlIWAks_41EpMvWx7sboGJF4I?usp=drive_link).

## Usage

To evaluate the recovery of clean guitar tones from wet guitar tones, run the following command:

```bash
python test.py --dry_folder /path/to/dry/folder --recovered_folder /path/to/recovered/folder
```