
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="text-davinci-001",
          temperature=0.7,
          max_tokens=300)


# Define UI configuration
config = UIConfig(description="Enter instruction",
                  button_text="Generate",
                  placeholder="Explain the moonlanding to a 6 year old.")

demo_web_app(gpt, config)
