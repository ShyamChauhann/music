from pipeline import build_audiosep, separate_audio
import torch
import os
import time

device = torch.device("cpu")

MODEL = build_audiosep(
    config_yaml='config/audiosep_base.yaml',
    checkpoint_path='checkpoint/audiosep_base_4M_steps.ckpt',
    device=device
)

def run_separation(input_wav_path: str, text_query: str, out_dir: str = "gradio_outputs"):
    os.makedirs(out_dir, exist_ok=True)
    safe_query = text_query.strip().lower().replace(" ", "_")[:50]
    timestamp = int(time.time())
    output_filename = f"{timestamp}_{safe_query}.wav"
    output_path = os.path.join(out_dir, output_filename)

    separate_audio(MODEL, input_wav_path, text_query, output_path, device)
    return output_path
