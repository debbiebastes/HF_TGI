from huggingface_hub import InferenceClient

client = InferenceClient("http://127.0.0.1:8080")
for token in client.text_generation("who were the first five presidents of the USA?", max_new_tokens=300, stream=True, temperature=0.6):
    print(token, end='')

print()
print("*****THE END*****")
print()