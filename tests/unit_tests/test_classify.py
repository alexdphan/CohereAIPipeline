from cohere.classify import Example
from classification import compute_classification, compute_confidence_score, get_classification_results

def test_get_classification_results():
    text = "This is a test sentence."
    examples = [
        Example(text="This is great!", label="positive"),
        Example(text="I love it!", label="positive"),
        Example(text="This is amazing!", label="positive"),
        Example(text="This is amazing!", label="positive"),
        Example(text="I love it so much!", label="positive"),
        Example(text="This is fabulous!", label="positive"),
        Example(text="This is awful!", label="negative"),
        Example(text="I hate it!", label="negative"),
        Example(text="This is terrible!", label="negative"),
        Example(text="This is disgusting!", label="negative"),
        Example(text="I hate it so much!", label="negative"),
        Example(text="This is not good at all!", label="negative"),
    ]
    predicted_label = get_classification_results(text, examples)
    assert predicted_label == {"predicted_label": "negative", "confidence_score": 0.8638854}

def test_compute_confidence_score():
    text = "I love eating pizza!"
    examples = [
    Example(text="This is great!", label="positive"),
    Example(text="I love it!", label="positive"),
    Example(text="This is amazing!", label="positive"),
    Example(text="This is amazing!", label="positive"),
    Example(text="I love it so much!", label="positive"),
    Example(text="This is fabulous!", label="positive"),
    Example(text="This is awful!", label="negative"),
    Example(text="I hate it!", label="negative"),
    Example(text="This is terrible!", label="negative"),
    Example(text="This is disgusting!", label="negative"),
    Example(text="I hate it so much!", label="negative"),
    Example(text="This is not good at all!", label="negative"),
    ]
    confidence_score = compute_confidence_score(text, examples)
    assert 0.8 <= confidence_score <= 1.0

def test_compute_classification():
    examples = [
        Example(text="This is a positive example.", label="positive"),
        Example(text="This is a positive example 1.", label="positive"),
        Example(text="This is a negative example.", label="negative"),
        Example(text="This is a negative example 1.", label="negative"),
        Example(text="This is a neutral example.", label="neutral"),
        Example(text="This is a neutral example 1.", label="neutral"),
    ]
    text = "This is a positive sentence."
    classification = compute_classification(text, examples)
    assert classification == "positive"
    text = "This is a negative sentence."
    classification = compute_classification(text, examples)
    assert classification == "negative"
