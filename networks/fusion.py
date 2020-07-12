import torch
import torch.nn as nn

class Fusion(nn.Module):
    def __init__(self,channel_inputs,channel_outputs):
        super(Fusion,self).__init__()
        self.channel_inputs = channel_inputs
        self.channel_outputs = channel_outputs
        self.conv1 = nn.Conv2d(self.channel_inputs,16,kernel_size=1)
        self.bn1 = nn.BatchNorm2d(16)
        self.conv2 = nn.Conv2d(16,16,kernel_size=3,stride=1,padding=1)
        self.bn2 = nn.BatchNorm2d(16)
        self.conv3 = nn.Conv2d(16,3,kernel_size=3,stride=1,padding=1)
        self.relu = nn.ReLU()
    def forward(self, x):
        x = self.relu(self.bn1(self.conv1(x)))
        x = self.relu(self.bn2(self.conv2(x)))
        x = self.conv3(x)
        return x
