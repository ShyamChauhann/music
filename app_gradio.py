import gradio as gr  # type: ignore
import os
from audio_interface import run_separation
from evaluate_metrics import compute_metrics

def separate_and_evaluate(audio_file, text_prompt, ref_file=None):
    """
    Run AudioSep separation and optionally compute SDR, SIR, SAR
    if a reference (ground-truth) file is provided.
    """
    output_audio = run_separation(audio_file, text_prompt)

    if ref_file and os.path.exists(ref_file):
        try:
            metrics = compute_metrics(ref_file, output_audio)  # use reference
            metrics_str = (
                f"**SDR:** {metrics['SDR']:.2f}\n"
                f"**SI-SDR:** {metrics['SIR']:.2f}\n"
                f"**SAR:** {metrics['SAR']:.2f}"
            )
        except Exception as e:
            metrics_str = f"⚠️ Metric computation failed: {str(e)}"
    else:
        metrics_str = "Reference file not provided. Metrics unavailable."

    return output_audio, metrics_str

PROMPT_OPTIONS = [
    "vocals", "bass", "drums", "background sounds"
]

# ------------------------------
# Gradio App
# ------------------------------
with gr.Blocks() as demo:
    gr.Markdown("## 🎵 AudioSep - Audio Source Separation")

    with gr.Row():
        audio_input = gr.Audio(label="🎧 Upload Audio File", type="filepath")
        prompt_dropdown = gr.Dropdown(
            choices=PROMPT_OPTIONS,
            label="🎚️ Select Separation Type",
            value="vocals"
        )
        ref_input = gr.Audio(label="Optional: Reference (Ground Truth) File", type="filepath")

    output_audio = gr.Audio(label="🎶 Separated Output")
    metrics_box = gr.Markdown(label="📊 Objective Metrics")

    # 🟩 Styled Run Button
    run_button = gr.Button("🔊 Run Separation + Evaluate", elem_id="run-btn")

    run_button.click(
        separate_and_evaluate,
        inputs=[audio_input, prompt_dropdown, ref_input],
        outputs=[output_audio, metrics_box]
    )

    # Add custom CSS for button styling
    demo.load(None, None, None)
    demo.css = """
        #run-btn {
            background-color: #28a745 !important;
            color: white !important;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 18px;
            transition: 0.3s;
        }
        #run-btn:hover {
            background-color: #218838 !important;
            transform: scale(1.05);
        }
    """

demo.launch()

# import gradio as gr  # type: ignore
# import os
# from audio_interface import run_separation
# from evaluate_metrics import compute_metrics

# def separate_and_evaluate(audio_file, ref_file=None):
#     """
#     Run AudioSep separation using a placeholder text prompt,
#     then compute SDR, SIR, SAR if a ground-truth reference is provided.
#     """
#     if audio_file is None:
#         return None, "Please upload a mixture audio file."

#     # Ensure output folder exists
#     output_dir = "gradio_outputs"
#     os.makedirs(output_dir, exist_ok=True)
#     output_audio_path = os.path.join(output_dir, os.path.basename(audio_file))

#     # Dummy text prompt (required by AudioSep model)
#     text_prompt = "vocals"

#     # Run separation
#     output_audio = run_separation(audio_file, text_prompt)

#     # Compute metrics if reference file provided
#     if ref_file and os.path.exists(ref_file):
#         try:
#             metrics = compute_metrics(ref_file, output_audio)
#             metrics_str = (
#                 f"**SDR:** {metrics['SDR']:.2f} dB\n"
#                 f"**SIR:** {metrics['SIR']:.2f} dB\n"
#                 f"**SAR:** {metrics['SAR']:.2f} dB"
#             )
#         except Exception as e:
#             metrics_str = f"⚠️ Metric computation failed: {str(e)}"
#     else:
#         metrics_str = "Reference file not provided. Metrics unavailable."

#     return output_audio, metrics_str


# # ------------------------------
# # Gradio App
# # ------------------------------
# with gr.Blocks() as demo:
#     gr.Markdown("## 🎵 AudioSep - Audio Source Separation")

#     with gr.Row():
#         audio_input = gr.Audio(label="🎧 Upload Mixture Audio", type="filepath")
#         ref_input = gr.Audio(label="Optional: Ground Truth Reference Audio", type="filepath")

#     output_audio = gr.Audio(label="🎶 Separated Output")
#     metrics_box = gr.Markdown(label="📊 Objective Metrics")

#     # Styled Run Button
#     run_button = gr.Button("🔊 Run Separation + Evaluate", elem_id="run-btn")

#     run_button.click(
#         separate_and_evaluate,
#         inputs=[audio_input, ref_input],
#         outputs=[output_audio, metrics_box]
#     )

#     # Custom button CSS
#     demo.css = """
#         #run-btn {
#             background-color: #28a745 !important;
#             color: white !important;
#             font-weight: bold;
#             border-radius: 10px;
#             padding: 10px 18px;
#             transition: 0.3s;
#         }
#         #run-btn:hover {
#             background-color: #218838 !important;
#             transform: scale(1.05);
#         }
#     """

# demo.launch()


