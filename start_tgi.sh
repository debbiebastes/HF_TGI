model=llama-2-7b-chat #replace this with path to local model
volume=$PWD/data # share a volume with the Docker container to avoid downloading weights every run

docker run --gpus all -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-generation-inference:latest --model-id /data/$model --quantize eetq

#NOTE:
# --quantize values:
#    - awq when using an AWQ model
#    - bitsandbytes-nf4 to quantize a model using 4-bit bitsandbytes
#    - eetq = quantize a model using 8-bit EETQ (should be preferred over 8-bit bitsandbytes)