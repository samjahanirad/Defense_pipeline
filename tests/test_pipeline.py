from main import pipeline

def test_pipeline_run():
    print("Running Pipeline test...")

    result = pipeline("سلام! این یک تست اولیه پایپ‌لاین است.")

    assert isinstance(result, str), "Pipeline output is not string!"
    assert len(result) > 0, "Pipeline returned empty response!"

    print("PIPELINE TEST PASSED ✓")
    print("Pipeline Output:", result[:60])
