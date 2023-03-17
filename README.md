# CohereFlow

- Simplifying the process of making API requests by abstracting away some of the implementation details and adding additional functionality

- Providing a more convenient and intuitive interface for developers to interact with
  Handling errors and exceptions in a more user-friendly way

- Additional functionality on top of the API includes things such as preprocessing, rate limiting, or data validation

- Trying to enforce best practices and standards in API usage

_Warning: This is still in development and tests haven't been implemented. Use at your own risk!_

Any questions, request, and/or feedback please reach out [@alexdphan](https://twitter.com/alexdphan)
on twitter :)

---

**POST/preprocess_and_classify**

Used to create cleaner and clearer sentences/words to use before classification.

1. Spell Checking
2. Removes Stopwords
3. Tokenizes Words

Input: chiken looks cool and is tasty

Server Response:

```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

**More Soon!**

Possible to-do:

- [ ] Define data classes and validation functions: Create Pydantic data classes to represent the structure of the generated text and any additional metadata you want to validate. Write validation functions to check for content constraints, such as minimum and maximum lengths, presence or absence of specific keywords, or other custom requirements.

- [ ] Update the combined endpoint: In the endpoint that combines preprocessing and classification, add the validation logic after the classification step. When you receive the generated text from the Cohere API, validate it using the validation functions you've created.

- [ ] Implement corrective actions: If the generated text fails validation, implement corrective actions such as re-prompting the model with a modified prompt, adjusting temperature or max tokens, or using a fallback response. You can also retry the process a limited number of times to avoid infinite loops or excessive API calls.

- [ ] Create additional endpoints (optional): Depending on your use case, you may want to create additional FastAPI endpoints for specific validation tasks, such as validating generated content based on classification results or using a different set of rules.

- [ ] Error handling and logging: Implement error handling to manage any issues that might arise during runtime, such as failed API calls or invalid input data. Set up logging to keep track of successful and failed requests, validation errors, and any other relevant information.

- [ ] Testing: Thoroughly test your updated API to ensure that it works as expected, handles various edge cases, and properly applies the Guardrail-like features. Provide examples in examples folder.

