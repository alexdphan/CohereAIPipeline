rail_spec = """
<rail version="0.1">



<output>
    <pythoncode
        name="python_code"
        format="cohere-python-generate"
        on-fail-cohere-python-generate="reask"
    />
</output>

<constraint>
    <regex match="import cohere" />
</constraint>

<prompt>
Using Cohere's 'generate' API endpoint with the 'cohere-python' package, generate realistic text conditioned on a given input.

API Key: {{api_key}}
Model: {{model}}
Prompt: {{prompt}}
Max Tokens: {{max_tokens}}

</prompt>

</rail>
"""
