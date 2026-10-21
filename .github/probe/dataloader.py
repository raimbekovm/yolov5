import sys, torch
from torch.utils.data import DataLoader, Dataset
class D(Dataset):
    def __len__(self): return 64
    def __getitem__(self, i): return torch.zeros(3)
if __name__ == "__main__":
    print(sys.version.split()[0], torch.__version__)
    for b in DataLoader(D(), batch_size=8, num_workers=2): pass
    print("OK")
