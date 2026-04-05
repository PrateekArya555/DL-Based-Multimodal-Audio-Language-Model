from models.speech_to_text import SpeechToText
from models.sound_classifier import SoundClassifier
from models.reasoning import ReasoningEngine

def main():
    audio_path = "data/audio.wav"

    # 🌍 Speech
    stt = SpeechToText()
    original, translated, lang = stt.transcribe(audio_path)

    print("\n🌍 Detected Language:", lang)
    print("🗣️ Original Speech:", original)
    print("🔁 Translated Speech:", translated)

    # 🔊 Sound
    sound_model = SoundClassifier()
    sounds = sound_model.predict(audio_path)
    print("Detected Sounds:", sounds)

    # 🧠 Reasoning
    reasoning = ReasoningEngine()
    result = reasoning.analyze(translated, sounds)

    print("\n🧠 Scene Analysis:")
    print(result)

if __name__ == "__main__":
    main()