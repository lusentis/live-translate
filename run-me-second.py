# /bin/env python3

from whisper_live.client import TranscriptionClient
client = TranscriptionClient(
    "localhost", 9090, is_multilingual=True, lang="it", translate=True)
client()
