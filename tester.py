
path = "/Users/deepakmishra/work/llm-scratch/huggingface-llm/out/checkpoint-3"


from transformers import pipeline

# fill_mask = pipeline(
#     "fill-mask",
#     model=path,
#     tokenizer=path
# )


# print(fill_mask("नमस्ते <mask>."))

text_gen_pipeline = pipeline("text-generation", model=path, tokenizer=path)
#text_gen_pipeline = pipeline("text-generation")


# Generate text given a prompt
prompt = "नमस्ते"
generated_text = text_gen_pipeline(prompt, max_length=60)

print(generated_text)
