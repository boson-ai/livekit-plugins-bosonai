"""Boson AI plugin for LiveKit Agents: Higgs Realtime speech-to-speech and Higgs Avatar.

Packages `livekit-plugins-boson` (realtime, livekit/agents#6340) and
`livekit-plugins-boson-avatar` (avatar, livekit/agents#7019 + #7886) from LiveKit
Agents into one install until those ship on PyPI.
"""

from __future__ import annotations

from livekit.agents import Plugin

from . import realtime
from .api import AvatarInfo, list_avatars
from .avatar import AvatarSession
from .errors import BosonAvatarException
from .log import logger
from .version import __version__

__all__ = [
    "AvatarInfo",
    "AvatarSession",
    "BosonAvatarException",
    "__version__",
    "list_avatars",
    "realtime",
]


class BosonAIPlugin(Plugin):
    def __init__(self) -> None:
        super().__init__(__name__, __version__, __package__, logger)


Plugin.register_plugin(BosonAIPlugin())
