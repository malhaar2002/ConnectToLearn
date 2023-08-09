import os

OPENAI_API_KEY = "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"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = "ls__aa9f7523e7774931b063c6d2194a30ac"