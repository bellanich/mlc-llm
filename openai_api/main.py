from mlc_llm import MLCEngine
from mlc_llm.serve.config import EngineConfig
from openai_api.utils import img_as_str


# Create engine
model = "HF://bella-nich/llava-onevision-qwen2-0.5b-ov-q4f16_1-mlc"
engine = MLCEngine(
    model,
    mode="local",
    engine_config=EngineConfig(prefill_chunk_size=832)
)

# Run chat completion in OpenAI API.
for response in engine.chat.completions.create(
    messages=[
        {"role": "user",
         "content": [
            {"type": "text", "text": "What is in this image? Keep your answer brief."},
            {"type": "image_url", "image_url": img_as_str("openai_api/images/cat.jpg")}
        ]}
    ],
    model=model,
    stream=True,
):
    for choice in response.choices:
        print(choice.delta.content, end="", flush=True)
print("\n")

engine.terminate()