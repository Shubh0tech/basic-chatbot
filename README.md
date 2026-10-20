# Basic Chatbot (Task 4 — rule based)

## 🚀 Try it live → https://shubh0tech.github.io/basic-chatbot/

Open the link above and chat with Neony right in your browser — no install needed.
This is the direct-use link for submission.

A simple **rule-based chatbot** in Python (CLI + eye-catching Tkinter GUI)
plus a matching **web version** you can chat with in the browser.
Standard library only — no pip installs.

## Run locally

```
py basic_chatbot.py          # GUI chat window (dark neon, chat bubbles)
py basic_chatbot.py --cli    # terminal chat
```

## Scope (matches the task)

- Input from user like: "hello", "how are you", "bye"
- Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!"

## Key concepts used

| Concept | Where |
|---|---|
| **if-elif** | `get_reply()` matches keywords with an if / elif / else chain |
| **functions** | `get_reply()`, `is_exit()`, `run_cli()`, `ChatApp` methods, `getReply()` in JS |
| **loops** | `while` loop keeps the CLI conversation going |
| **input/output** | `input()` / `print()` in the CLI, chat box in the GUI/web |

## What it understands

greetings, "how are you", your name, who made you, help, jokes,
time, date, thanks, sorry, love, weather, age, "are you real", ok,
and "bye" to end the conversation — plus a fallback reply for anything else.

## Project layout

```
basic_chatbot.py   # Python chatbot (GUI + CLI, single file)
docs/index.html    # web version (GitHub Pages)
```

## Links

- **Live web app:** https://shubh0tech.github.io/basic-chatbot/
- **Source:** https://github.com/Shubh0tech/basic-chatbot
