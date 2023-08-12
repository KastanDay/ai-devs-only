import torch
import torch.nn as nn

def transformer_model(input_dim, num_heads, num_layers, ff_dim):
    transformer_layer = nn.TransformerEncoderLayer(d_model=input_dim, nhead=num_heads, dim_feedforward=ff_dim)
    transformer = nn.TransformerEncoder(transformer_layer, num_layers=num_layers)
    return transformer