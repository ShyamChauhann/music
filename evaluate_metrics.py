import soundfile as sf  # type: ignore
import numpy as np
import museval  # type: ignore
import librosa  # type: ignore

def compute_metrics(ref_file, est_file):
    try:
        # Load audio with at least 2D shape (nsamples, nchannels)
        ref, sr_ref = sf.read(ref_file, always_2d=True)
        est, sr_est = sf.read(est_file, always_2d=True)
    except Exception as e:
        raise RuntimeError(f"Error reading audio files: {e}")

    # 🔄 Resample if sampling rates differ
    if sr_ref != sr_est:
        est = librosa.resample(est.T, orig_sr=sr_est, target_sr=sr_ref).T
        sr_est = sr_ref

    # 🎧 Match number of channels
    if ref.shape[1] != est.shape[1]:
        if est.shape[1] == 1 and ref.shape[1] == 2:
            est = np.repeat(est, 2, axis=1)  # mono -> stereo
        elif est.shape[1] == 2 and ref.shape[1] == 1:
            est = np.mean(est, axis=1, keepdims=True)  # stereo -> mono
        else:
            min_channels = min(ref.shape[1], est.shape[1])
            ref = ref[:, :min_channels]
            est = est[:, :min_channels]

    # 🔁 Convert to (nchan, nsamples) as museval expects
    ref = ref.T
    est = est.T

    # 🚨 Check for silent reference or estimated signals
    if np.all(ref == 0) or np.all(est == 0):
        return {"SDR": float("nan"), "SIR": float("nan"), "SAR": float("nan")}

    try:
        sdr, isr, sir, sar = museval.evaluate(ref, est)
        metrics = {
            "SDR": float(np.mean(sdr)),
            "SIR": float(np.mean(sir)),
            "SAR": float(np.mean(sar))
        }
    except Exception as e:
        metrics = {"SDR": float("nan"), "SIR": float("nan"), "SAR": float("nan")}
        print(f"⚠️ Metric computation failed: {e}")

    return metrics

if __name__ == "__main__":
    # Example usage
    ref_file = "data/reference_vocals.wav"    # ground truth
    est_file = "outputs/estimated_vocals.wav" # model output

    metrics = compute_metrics(ref_file, est_file)
    print("\n--- Audio Separation Metrics ---")
    print(f"SDR: {metrics['SDR']}")
    print(f"SIR: {metrics['SIR']}")
    print(f"SAR: {metrics['SAR']}")
