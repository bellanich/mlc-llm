import base64
from io import BytesIO
from PIL import Image

from mlc_llm import MLCEngine
from mlc_llm.serve.config import EngineConfig

# Load image
image = Image.open("openai_api/images/cat.jpg")
image = image.resize((224, 224))
buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue())

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
            {"type": "text", "text": "Annotate this image. Avoid unnecessary descriptions."},
            {"type": "image_url", "image_url": "data:image/jpeg;base64," + img_str.decode("ascii")}
        ]}
    ],
    model=model,
    stream=True,
):
    for choice in response.choices:
        print(choice.delta.content, end="", flush=True)
print("\n")

engine.terminate()