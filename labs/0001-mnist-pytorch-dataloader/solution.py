import torch

class MyTransform:
    def __call__(self, x: torch.Tensor) -> torch.Tensor:
        # Standardize per-image, add small random noise, clamp
        m = x.mean()
        s = x.std().clamp(min=1e-6)
        x = (x - m) / s
        x = x + 0.05 * torch.randn_like(x)
        x = x.clamp(-3, 3)
        return x.type_as(x)
