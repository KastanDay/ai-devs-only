import torch
import torch.nn as nn

def transformer_model(input_dim=512, num_heads=8, num_layers=6, ff_dim=2048, dropout=0.1):
    transformer_layer = nn.TransformerEncoderLayer(d_model=input_dim, nhead=num_heads, dim_feedforward=ff_dim, dropout=dropout)
    transformer_norm = nn.LayerNorm(normalized_shape=input_dim)
    transformer = nn.TransformerEncoder(transformer_layer, num_layers=num_layers, norm=transformer_norm)
    return transformer