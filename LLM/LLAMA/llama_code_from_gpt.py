import os
from huggingface_hub import hf_hub_download
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, AutoModelForSeq2SeqLM


model_name = "meta-llama/CodeLlama-7b-Python-hf"

generator = pipeline('text-generation', model=model_name)

res = generator("give me python code to read a file",
                max_length=100,
                num_return_sequences=2,
)

print(res)