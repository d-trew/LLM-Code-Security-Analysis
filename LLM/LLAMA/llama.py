import os
from huggingface_hub import hf_hub_download
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, AutoModelForSeq2SeqLM



model_id = "meta-llama/CodeLlama-7b-Python-hf"
filenames = [
    "config.json",
    "generation_config.json",
    "model-00001-of-00002.safetensors",
    "model-00002-of-00002.safetensors",
    "model.safetensors.index.json",
    "pytorch_model-00001-of-00003.bin",
    "pytorch_model-00002-of-00003.bin",
    "pytorch_model-00003-of-00003.bin",
    "pytorch_model.bin.index.json",
    "special_tokens_map.json",
    "tokenizer.json",
    "tokenizer.model",
    "tokenizer_config.json"
]


for filename in filenames:
    downloaded_model_path = hf_hub_download(
        repo_id=model_id,
        filename=filename,
        revision="main",
        token=HUGGING_FACE_API_KEY,
    )
    print(downloaded_model_path)

tokenizer = AutoTokenizer.from_pretrained(model_id,legacy=False)
model = AutoModelForCausalLM.from_pretrained(model_id)

pipeline = pipeline('text-generation', model=model,device=1, tokenizer=tokenizer,max_length=1000)

pipeline("who are you?")