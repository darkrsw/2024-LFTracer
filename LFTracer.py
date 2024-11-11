from typing import Any, Optional, Callable, Dict, List, Type, TextIO, cast
from types import FrameType, TracebackType
import sys


class LFTracer():
  def __init__(self, target_func: str):
        self.target_func = target_func

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_tp: Type, exc_value: BaseException,
                 exc_traceback: TracebackType) -> Optional[bool]:
        return None

    def getLFMap(self):
        return {}

    def getLFStat(self):
        return {}
