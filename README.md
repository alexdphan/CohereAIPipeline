# CohereAPIPipeline

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
