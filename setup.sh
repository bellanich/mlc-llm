#!/usr/bin/env bash


# install rust
echo "Installing rust and cargo..."
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

echo "Setting up python virtual env..."
poetry init
poetry shell

echo "Installing MLC LLM lib..."
python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu
# Validate installation
python -c "import mlc_llm; print(mlc_llm)"