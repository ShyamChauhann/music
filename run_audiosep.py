from pipeline import build_audiosep, separate_audio
import torch  # type: ignore

# Use CPU for safety on macOS
device = torch.device('cpu')

# Load AudioSep model
model = build_audiosep(
    config_yaml='config/audiosep_base.yaml',
    checkpoint_path='checkpoint/audiosep_base_4M_steps.ckpt',
    device=device
)

# Input audio file (must be 32 kHz mono WAV)
audio_file = 'input.wav'

# List of textual prompts and output filenames
tasks = [
    ("separate the vocals", "output_vocals.wav"),
    ("separate the instruments", "output_instruments.wav"),
    ("separate the drums", "output_drums.wav"),
    ("separate the bass", "output_bass.wav"),
    ("separate the noise", "output_noise.wav"),
]

# Run all separations
for text, output_file in tasks:
    print(f"\n🔹 Running: {text}")
    separate_audio(model, audio_file, text, output_file, device)
    print(f"Saved: {output_file}")

print("\n🎵 All separations complete!")
