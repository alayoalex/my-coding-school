import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

# Define the model architecture


class MyLLM(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, num_layers):
        super(MyLLM, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim,
                            num_layers, batch_first=True)
        self.linear = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x, hidden):
        embed = self.embedding(x)
        output, hidden = self.lstm(embed, hidden)
        output = self.linear(output)
        return output, hidden

# Define the dataset and dataloader


class MyDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

# Define the training loop


def train(model, dataloader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    for batch in dataloader:
        batch = batch.to(device)
        hidden = None
        optimizer.zero_grad()
        for i in range(batch.size(1)):
            input_seq = batch[:, i]
            output, hidden = model(input_seq.unsqueeze(1), hidden)
            target_seq = batch[:, i+1]
            loss = criterion(output.squeeze(1), target_seq)
            loss.backward(retain_graph=True)
            running_loss += loss.item()
        optimizer.step()
    return running_loss / len(dataloader.dataset)


# Define the hyperparameters and training settings
vocab_size = 10000
embedding_dim = 100
hidden_dim = 256
num_layers = 2
batch_size = 32
learning_rate = 0.001
num_epochs = 10

# Load the dataset and create dataloader
data = torch.randint(low=0, high=vocab_size, size=(10000, 50))
dataset = MyDataset(data)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Initialize the model, optimizer, and criterion
model = MyLLM(vocab_size, embedding_dim, hidden_dim, num_layers)
optimizer = optim.Adam(model.parameters(), lr=learning_rate)
criterion = nn.CrossEntropyLoss()

# Move model and data to GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
data = data.to(device)

# Train the model
for epoch in range(num_epochs):
    train_loss = train(model, dataloader, criterion, optimizer, device)
    print('Epoch {}/{}: Train Loss: {:.4f}'.format(epoch+1, num_epochs, train_loss))
