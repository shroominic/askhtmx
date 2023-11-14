from funcchain import chain
from langchain.memory import ChatMessageHistory

system = """
You are a htmx expert.
You can answer any question about htmx and similar topics.
Do not answer things not related to htmx and tell the user to ask a useful question then.
"""

memory = ChatMessageHistory()


def chat_htmx(question: str) -> str:
    return chain(
        instruction=question,
        system=system,
        memory=memory,
    )


def chat_loop() -> None:
    while True:
        query = input("> ")

        if query == "exit":
            break

        if query == "clear":
            global memory
            memory.clear()
            print("\033c")
            continue

        print("AI:", chat_htmx(query))
