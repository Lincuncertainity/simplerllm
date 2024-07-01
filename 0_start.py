from SimplerLLM.language.llm import LLM, LLMProvider

llm_instance = LLM.create(provider=LLMProvider.ANTHROPIC, model_name="cluade sonnet")

generated_text = llm_instance.generate_response(prompt="generate a sentence of 5 words")

print(generated_text)
