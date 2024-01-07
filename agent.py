import os
os.environ["OPENAI_API_KEY"] = "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"
from dotenv import load_dotenv
load_dotenv()
import openai
import os
openai.api_key= os.environ.get("OPENAI_API_KEY")
