from typing import Annotated

import typer
from funcchain import settings
from .chat import chat_htmx, chat_loop


app = typer.Typer()

settings.MODEL_NAME = "gpt-4-1106-preview"


@app.command()
def ask(
    question: Annotated[str, typer.Argument(help="Question to ask.")],
) -> None:
    """
    Ask a question about htmx or relevant things.
    """
    print(chat_htmx(question))


@app.command()
def chat() -> None:
    """
    Chat with the htmx expert.
    """
    print("Welcome to the htmx expert chat. Ask me anything about htmx.")
    print("Type 'exit' to exit, 'clear' to clear the history.")
    chat_loop()


if __name__ == "__main__":
    app()
