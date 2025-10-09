from transformers import GPT2LMHeadModel, GPT2Tokenizer 

name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(name)
model = GPT2LMHeadModel.from_pretrained(name)

prompt = ""
while True:
    prompt = input(">> ")
    if prompt == "quit":
        break
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=60, do_sample=True)
    print("\n" + tokenizer.decode(outputs[0], skip_special_tokens=True))
print(">> user exited")