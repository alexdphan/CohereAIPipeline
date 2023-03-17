from cohereflow.classify import classify_text
from cohereflow.utils.classify_utils import examples

def test_classify_text():
    text = "The movie was absolutely fantastic!"
    expected_output = {
        "input_text": text,
        "predicted_label": "Positive",
        "confidence_score": 0.999
    }
    output = classify_text(text, examples)
    assert output["input_text"] == expected_output["input_text"]
    assert output["predicted_label"] == expected_output["predicted_label"]
    assert output["confidence_score"] >= expected_output["confidence_score"] - 0.001
    assert output["confidence_score"] <= expected_output["confidence_score"] + 0.001
