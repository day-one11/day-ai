from dotenv import load_dotenv
load_dotenv()
import openai
import os
openai.api_key= os.environ.get("OPENAI_API_KEY")
