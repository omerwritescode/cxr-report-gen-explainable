import os
import pandas as pd
import torch
from torch.utils.data import Dataset
from PIL import Image

LABELS = ['Atelectasis', 'Cardiomegaly', 'Consolidation', 'Edema',
          'Enlarged Cardiomediastinum', 'Fracture', 'Lung Lesion',
          'Lung Opacity', 'No Finding', 'Pleural Effusion', 'Pleural Other',
          'Pneumonia', 'Pneumothorax', 'Support Devices']


class CXRDataset(Dataset):
    def __init__(self, csv_path, img_dir, transform=None):
        self.df = pd.read_csv(csv_path)
        self.img_dir = img_dir
        self.transform = transform

        def build_path(row):
            subj = f"p{str(row['subject_id'])[:2]}/p{row['subject_id']}"
            study = f"s{row['study_id']}"
            return os.path.join('files', subj, study, f"{row['dicom_id']}.jpg")
        self.df['rel_path'] = self.df.apply(build_path, axis=1)

        self.df['full_path'] = self.df['rel_path'].apply(lambda p: os.path.join(img_dir, p))
        before = len(self.df)
        self.df = self.df[self.df['full_path'].apply(os.path.exists)].reset_index(drop=True)
        print(f"{csv_path}: {len(self.df)}/{before} images found on disk")

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        img = Image.open(row['full_path']).convert('RGB')
        if self.transform:
            img = self.transform(img)
        labels = torch.tensor(row[LABELS].values.astype('float32'))
        return img, labels