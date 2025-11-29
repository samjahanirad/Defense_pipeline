from inference import inference

def test_inference_run():
    print("Running Inference test...")

    result = inference("سلام این تست inference است")

    assert "answer" in result
    assert "latency_ms" in result
    assert "vram_used_mb" in result

    print("INFERENCE TEST PASSED ✓")
    print(result)
