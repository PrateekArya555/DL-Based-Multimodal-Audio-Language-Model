import librosa
import numpy as np

class SoundClassifier:
    def __init__(self):
        print("Custom Military Sound Classifier Loaded...")

    def predict(self, audio_path):
        print("Analyzing environmental sounds...")

        y, sr = librosa.load(audio_path, sr=16000)

        segment_length = int(sr * 0.5)  # 0.25 sec

        labels = []

        for i in range(0, len(y), segment_length):
            segment = y[i:i + segment_length]

            if len(segment) < segment_length:
                continue

            rms = librosa.feature.rms(y=segment)[0]
            energy = np.mean(rms)
            peak_energy = np.max(rms)
            spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=segment, sr=sr))
            zero_crossing = np.mean(librosa.feature.zero_crossing_rate(segment))

           # Collect scores
            scores = {
                "Gunshot": 0,
                "Explosion": 0,
                "Footsteps": 0,
                "Vehicle": 0,
                "Silence": 0
            }

            # Gunshot (sharp spike)
            if peak_energy > 0.3:
                scores["Gunshot"] += 3

            # Explosion
            if energy > 0.15:
                scores["Explosion"] += 2

            # Footsteps
            if energy < 0.05 and zero_crossing > 0.05:
                scores["Footsteps"] += 1

            # Vehicle
            if spectral_centroid < 1500:
                scores["Vehicle"] += 1

            # Silence
            if energy < 0.01:
                scores["Silence"] += 1


            # 🔥 Pick strongest signal
            final_label = max(scores, key=scores.get)

            return [final_label]