from cohere.classify import Example
from typing import List

# Define the examples (text and label pairs)
examples = [
    Example(text="The movie was absolutely fantastic!", label="Positive"),
    Example(text="I really enjoyed the film.", label="Positive"),
    Example(text="The film was terrible and boring.", label="Negative"),
    Example(text="I didn't like the movie at all.", label="Negative"),
]
