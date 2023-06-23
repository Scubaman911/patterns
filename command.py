from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
import logging

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class PrintCommand(Command):
    def __init__(self, print_msg) -> None:
        self._msg = print_msg

    def execute(self) -> None:
        print(self._msg)


class PrintLogCommand(Command):
    def __init__(self, receiver: MessageLogger, msg) -> None:
        self._msg = msg
        self._receiver = receiver

    def execute(self) -> None:
        self._receiver.log_dated_msg(self._msg)


class MessageLogger:
    def log_dated_msg(self, msg):
        logging.info(f"Time: {datetime.now()} Msg: {msg}")


class Invoker:
    """
    The Invoker is associated with one or several commands. It sends a request
    to the command.
    """

    _on_start = None
    _on_finish = None

    """
    Initialize commands.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes. The
        Invoker passes a request to a receiver indirectly, by executing a
        command.
        """

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    invoker = Invoker()
    invoker.set_on_start(PrintCommand("Simple message to print!"))
    receiver = MessageLogger()
    invoker.set_on_finish(PrintLogCommand(receiver, "Complex message to print!"))
    invoker.do_something_important()
