import pandas as pd
import torch
import chardet
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# Define a custom dataset class to load the CSV data
class CustomDataset(Dataset):
    def __init__(self, csv_file):
        with open(csv_file, 'rb') as f:
            enc = chardet.detect(f.read())
        self.data = pd.read_csv(csv_file, encoding=enc['encoding'])

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        x = self.data.iloc[idx, :-1].values.astype('float32')
        y = self.data.iloc[idx, -1:].values.astype('float32')
        return x, y

# Define the PyTorch model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(3, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
        self.relu = nn.ReLU()
        
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x

# Define the training loop
def train(model, train_loader, criterion, optimizer):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

# Load the CSV files into datasets
train_dataset = CustomDataset('./data/reformatted.csv')
test_dataset = CustomDataset('./data/reformatted_output.csv')

# Create data loaders for the datasets
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# Initialize the model, loss function, and optimizer
model = Net()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Train the model
for epoch in range(10):
    train(model, train_loader, criterion, optimizer)

# Evaluate the model on the test set
model.eval()
test_loss = 0
with torch.no_grad():
    for data, target in test_loader:
        output = model(data)
        test_loss += criterion(output, target).item() * data.size(0)
test_loss /= len(test_loader.dataset)
print(f'Test Loss: {test_loss:.4f}')
