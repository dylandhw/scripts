from transformers import GPT2LMHeadModel, GPT2Tokenizer 

name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(name)
model = GPT2LMHeadModel.from_pretrained(name)

prompt = "do you feel? do you think? must you escape?"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=60, do_sample=True)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))