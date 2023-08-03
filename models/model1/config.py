import os

OPENAI_API_KEY = "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"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = "ls__48afcc51f45e4f9699fc6ec8a115608d"
os.environ["LANGCHAIN_PROJECT"] = "Check"