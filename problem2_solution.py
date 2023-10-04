import torch

def tensor_softmax(tensor):
    return torch.nn.functional.softmax(tensor, dim=1)