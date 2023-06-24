import os
import time
import openai
from openai.api_resources import Completion
import numpy as np

from rich import box
from rich import print
from rich.text import Text

from rich.panel import Panel
from rich.prompt import Prompt
from rich.layout import Layout
from rich.progress import Progress
from rich.traceback import install
install(show_locals=True)



caption_prompt = Prompt.ask("Enter your caption prompt")
with Progress() as progress:
    
    task1 = progress.add_task("[red]Downloading...", total=100)
    task2 = progress.add_task("[yellow]Processing...", total=100)
    task3 = progress.add_task("[green]Writing...", total=100)
    
    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.4)
        progress.update(task3, advance=0.7)
        time.sleep(0.02)
        
caption_prompt_panel = Panel(f"{caption_prompt}", box = box.SQUARE, border_style="bold white")
print(caption_prompt_panel)



openai.api_key = os.environ["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"]

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=caption_prompt,
    max_tokens=50,
    temperature=0.8,
    n = 1,
    stop=None,
)

generated_caption = response.choices[0].text.strip()
print("Generated Caption:", generated_caption)