class ReasoningEngine:
    def analyze(self, speech, sounds):
        analysis = ""

        speech_lower = speech.lower()

        # 🔥 THREAT KEYWORDS
        threat_words = ["fire", "gun", "attack", "blast", "explosion", "shoot", "danger"]

        # ⚠️ Threat detection (speech-based)
        if any(word in speech_lower for word in threat_words):
            analysis += "⚠️ Threat-related communication detected. "

        # 🔫 Sound-based threat
        if "Gunshot" in sounds:
            analysis += "⚠️ Gunfire detected. "

        if "Explosion" in sounds:
            analysis += "🚨 Explosion detected. "

        # 👣 Movement
        if "Footsteps" in sounds:
            analysis += "👣 Movement detected. "

        # 🚗 Vehicle
        if "Vehicle" in sounds:
            analysis += "🚗 Vehicle activity detected. "

        # 🗣️ Speech urgency
        urgency_words = ["run", "fast", "move", "hurry", "quick"]

        if any(word in speech_lower for word in urgency_words):
            analysis += "🗣️ Urgent communication detected. "

        elif speech.strip() != "":
            analysis += "🗣️ Communication detected. "

        # Default
        if analysis == "":
            analysis = "✅ Environment appears calm."

        return analysis