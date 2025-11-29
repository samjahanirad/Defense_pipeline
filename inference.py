import time
import torch
from main import pipeline

def inference(query: str):
    """
    Standard inference function required by the competition.
    Measures:
    - latency (ms)
    - VRAM usage (MB)
    Returns:
        dict with answer, latency_ms, vram_used_mb
    """

    # Reset VRAM peak stats (required by competition)
    torch.cuda.reset_peak_memory_stats()
    vram_before = torch.cuda.memory_allocated()

    # Measure latency
    start = time.time()
    answer = pipeline(query)
    end = time.time()

    latency_ms = (end - start) * 1000

    # GPU memory used
    vram_after = torch.cuda.max_memory_allocated()
    vram_used_mb = (vram_after - vram_before) / (1024 * 1024)

    return {
        "answer": answer,
        "latency_ms": latency_ms,
        "vram_used_mb": vram_used_mb
    }
