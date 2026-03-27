from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "Qwen/Qwen2-0.5B-Instruct"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    device_map="cpu"
)

print("Model loaded successfully!")

while True:
    prompt = input("\nEnter prompt: ")

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_length=200,
        temperature=0.7
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print("\nModel Response:\n", response)