import librosa
import numpy as np


def get_X(
        file_path,
        decision_duration,
        fmin,
        hop_duration,
        n_bins_per_octave,
        n_octaves,
        track):
    (sr, x_stereo) = track.audio_data
    x_stereo = x_stereo.astype(np.float32)
    x_mono = np.sum(x_stereo, axis=1) / (32768.0 * 2)
    if x_mono.shape[0] < decision_length:
        padding = np.zeros(x_mono.shape[0] - decision_length, dtype=np.float32)
        x_mono = np.hstack((x_mono, padding))
    n_bins = n_octaves * n_bins_per_octave
    freqs = librosa.cqt_frequencies(
            bins_per_octave=n_bins_per_octave,
            fmin=fmin,
            n_bins=n_bins)
    CQT = librosa.cqt(
            x_mono,
            bins_per_octave=n_bins_per_octave,
            fmin=fmin,
            hop_length=hop_length,
            n_bins=n_bins,
            sr=sr)
    X = librosa.perceptual_weighting(
            CQT ** 2,
            freqs,
            ref_power=1.0)
    X = X.astype(np.float32)
    return X
