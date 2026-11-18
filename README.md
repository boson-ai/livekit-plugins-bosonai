# livekit-plugins-bosonai

[LiveKit Agents](https://docs.livekit.io/agents/) plugin for [Boson AI](https://www.boson.ai):
Higgs Realtime (speech-to-speech) and Higgs Avatar (a talking face that follows the agent's voice).

```bash
pip install "livekit-plugins-bosonai @ https://github.com/boson-ai/livekit-plugins-bosonai/releases/download/v0.1.0/livekit_plugins_bosonai-0.1.0-py3-none-any.whl"
```

This installs `livekit-agents` too. Set `BOSON_API_KEY` (create one at
https://www.boson.ai/workspace/api-key) plus your LiveKit credentials
(`LIVEKIT_URL`, `LIVEKIT_API_KEY`, `LIVEKIT_API_SECRET`).

```python
from livekit.agents import Agent, AgentServer, AgentSession, JobContext, cli
from livekit.plugins import bosonai

server = AgentServer()


@server.rtc_session()
async def entrypoint(ctx: JobContext):
    session = AgentSession(
        llm=bosonai.realtime.RealtimeModel(input_audio_transcription_model="higgs-stt-3.1")
    )
    avatar = bosonai.AvatarSession(avatar_id="builtin_claire_v1")
    await avatar.start(session, room=ctx.room)
    await session.start(agent=Agent(instructions="You are a friendly assistant."), room=ctx.room)


if __name__ == "__main__":
    cli.run_app(server)
```

The code comes from the Boson plugins in [livekit/agents](https://github.com/livekit/agents)
(Apache-2.0). Once `livekit-agents[boson]` installs from PyPI, it replaces this package.
