import time
from numpy as numpy

from rich import box
from rich import print
from rich.text import Text

from rich.panel import Panel
from rich.prompt import Prompt
from rich.layout import Layout
from rich.progress import Progress
from rich.traceback import install
install(show_locals=True)

def caption_generations():
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