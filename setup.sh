#!/usr/bin/env bash


# install rust
echo "Installing rust and cargo..."
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install STABLE version of MLC LLM lib
echo "Installing MLC LLM lib..."
python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-cpu mlc-ai-cpu
# Add in custom model definitions
cp ios/MLCChat/models/siglip_vision.py .venv/lib/python3.10/site-packages/mlc_llm/model/vision/siglip_vision.py
cp -r ios/MLCChat/models/llava_onevision .venv/lib/python3.10/site-packages/mlc_llm/model/llava_onevision

# Validate installation
python -c "import mlc_llm; print(mlc_llm)"
