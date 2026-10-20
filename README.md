# Basic Chatbot (Task 4 — rule based)

A simple **rule-based chatbot** in Python (CLI + eye-catching Tkinter GUI)
plus a matching **web version** you can chat with in the browser.
Standard library only — no pip installs.

## Run

```
py basic_chatbot.py          # GUI chat window (dark neon, chat bubbles)
py basic_chatbot.py --cli    # terminal chat
```

Web version: open `docs/index.html` in a browser, or use the live GitHub Pages site.

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
