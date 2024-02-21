from huggingface_hub import InferenceClient

client = InferenceClient("http://127.0.0.1:8080")

#load prompt from text file
with open('/home/debbie/Dev/llm_localbench_data/PT-SL02_v022024.txt', 'r') as f:
    prompt = f.read()
    f.close()

for token in client.text_generation(prompt, max_new_tokens=1024, stream=True, temperature=0.6):
    print(token, end='')

print()
print("*****THE END*****")
print()