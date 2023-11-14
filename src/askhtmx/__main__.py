from typing import Annotated

import typer
from funcchain import settings
from .ask import ask_htmx


app = typer.Typer()

settings.MODEL_NAME = "gpt-4-1106-preview"


@app.command()
def ask(
    question: Annotated[str, typer.Argument(help="Question to ask.")],
) -> None:
    """
    Ask a question about the codebase or relevant libraries.
    """
    print(ask_htmx(question))


if __name__ == "__main__":
    app()
