
import torch

from torch.nn import Module, Sequential, Conv2d, ReLU,AdaptiveMaxPool2d, AdaptiveAvgPool2d, \
    NLLLoss, BCELoss, CrossEntropyLoss, AvgPool2d, MaxPool2d, Parameter, Linear, Sigmoid, Softmax, Dropout, Embedding
from torch.nn import functional as F
from torch.autograd import Variable
torch_ver = torch.__version__[:3]

__all__ = ['ATT_Module', 'CAM_Module']


class ATT_Module(Module):
    """ Position attention module"""
    def __init__(self, in_dim):
        super(ATT_Module, self).__init__()
        self.chanel_in = in_dim
#         self.query_conv = Conv2d(in_channels=in_dim, out_channels=in_dim, kernel_size=3,stride=1,padding=1)
#         self.key_conv = Conv2d(in_channels=in_dim, out_channels=in_dim, kernel_size=1,stride=1,padding=1)
#         self.value_conv = Conv2d(in_channels=in_dim, out_channels=in_dim, kernel_size=1,stride=1,padding=1)
        self.gamma = Parameter(torch.zeros(1))

        self.softmax = Softmax(dim=-1)
    def forward(self, x):
        """
            inputs :
                x : input feature maps( B X C X H X W)
            returns :
                out : attention value + input feature
                attention: B X \
                (HxW) X (HxW)
        """
        m_batchsize, C, height, width = x.size()
        proj_query = x.view(m_batchsize, C, -1)
        proj_key = x.view(m_batchsize, C, -1).permute(0, 2, 1)
        energy = torch.bmm(proj_query, proj_key)
        energy_new = torch.max(energy, -1, keepdim=True)[0].expand_as(energy) - energy
        attention = self.softmax(energy_new)
        attention = ((height * width) ** -.5) * attention
        proj_value = x.view(m_batchsize, C, -1)

        out = torch.bmm(attention, proj_value)
        out = out.view(m_batchsize, C, height, width)
        out = self.gamma * out + x
        return out



class GAM(Module):
    """ Position attention module"""
    def __init__(self, in_dim):
        super(GAM, self).__init__()
        self.chanel_in = in_dim
        self.query_conv = Conv2d(in_channels=in_dim, out_channels=in_dim, kernel_size=3, stride=1, padding=1)
        self.key_conv = Conv2d(in_channels=in_dim, out_channels=in_dim, kernel_size=3, stride=1, padding=1)
        self.value_conv = Conv2d(in_channels=in_dim, out_channels=in_dim, kernel_size=3, stride=1, padding=1)
        self.gamma = Parameter(torch.zeros(1))

        self.softmax = Softmax(dim=-1)
    def forward(self, x):
        """
            inputs :
                x : input feature maps( B X C X H X W)
            returns :
                out : attention value + input feature
                attention: B X \
                (HxW) X (HxW)
        """
        m_batchsize, C, height, width = x.size()
        proj_query = self.query_conv(x)
        proj_key = self.key_conv(x)
        attention = torch.exp(-((proj_query-proj_key)**2)/(2*0.5*0.5))
        proj_value = self.value_conv(x)
        out = torch.mul(proj_value, attention)
        out = self.gamma*out + x

        return out

