---
name: bale
description: "Private, local Bale bot for agents: read, search and answer messages, ask and wait, files. Use when the user asks about Bale Bot (bale.ai) or wants to run their own Bale messenger bot in Iran."
---

# Bale Bot

Private, local Bale bot for agents: read, search and answer messages, ask and wait, files.

The tools below come from the `bale-mcp` MCP server. If they are not available, install it with `claude mcp add bale -- uvx bale-mcp`, or add `"bale": {"command": "uvx", "args": ["bale-mcp"], "env": {"BALE_BOT_TOKEN": "${BALE_BOT_TOKEN:-}"}}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `bot_get_me`: Check BALE_BOT_TOKEN and show the bot's id, username and name. Use first to confirm the bot works.
- `bot_get_chat`: Get a chat's type, title or name, username and description, as seen by the bot.
- `bot_get_webhook_info`: Show whether a webhook is set (url empty = the reading tools work), pending updates and the last error.
- `bot_send_message`: Send a text message from the bot. Sends a real message. Confirm recipient and text with the user before calling.
- `bot_send_file`: Send a photo, document, video, audio or voice file from the bot. Sends a real message. Confirm recipient and file with the user before calling.
- `bot_edit_message`: Replace the text of a message the bot sent earlier. Changes a real message. Confirm with the user before calling.
- `bot_delete_message`: Delete a message in a chat where the bot may delete it (its own messages, or as admin). Cannot be undone; confirm with the user first.
- `bot_get_new_messages`: Get messages people sent the bot since the last check, from all chats, oldest first, and mark them read.
- `bot_list_chats`: List the chats this bot has talked in, newest first, with unread count and last message. Use to find chat ids.
- `bot_read_chat`: Show a chat's recent messages in both directions, oldest first, and mark the chat read.
- `bot_search_messages`: Search stored messages by text, newest first. Arabic and Persian yeh/kaf, Persian and Latin digits,
- `bot_wait_for_reply`: Wait until someone writes in a chat or presses a button, then return the new messages (marked read).
- `bot_download_file`: Download a file someone sent the bot to this computer (max 20 MB) and return its local path.

## Rules

- This server acts on the user's own account (`BALE_BOT_TOKEN`). Confirm with the user before any call that creates, sends, edits or deletes something.
- On timeouts or HTTP 403 outside Iran, set `BALE_MCP_PROXY` to an HTTP proxy with an Iranian IP.
