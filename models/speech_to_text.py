import whisper

class SpeechToText:
    def __init__(self, model_size="medium"):
        print("Loading Whisper model...")
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_path):
        print("Processing multilingual audio...")

        # 🔥 Single-pass translation (stable)
        result = self.model.transcribe(audio_path, task="translate")

        translated_text = result["text"]
        detected_lang = result["language"]

        # Use same output for both
        original_text = translated_text

        return original_text, translated_text, detected_lang
        