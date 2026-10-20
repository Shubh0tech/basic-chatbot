"""
=============================================================================
 BASIC CHATBOT  (Task 4 - rule based)
=============================================================================
 Goal: Build a simple rule-based chatbot.

 Scope:
   * Input from user like: "hello", "how are you", "bye"
   * Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!"

 Key Concepts Used:
   * if-elif         -> get_reply() matches keywords with if/elif/else
   * functions       -> get_reply(), chat(), run_cli(), ChatApp
   * loops           -> while loop keeps the conversation going
   * input / output  -> input() in CLI (or run the GUI / --cli flag)

 Run GUI:   py basic_chatbot.py
 Run CLI:   py basic_chatbot.py --cli
 Web:       docs/index.html
=============================================================================
"""

import sys
import datetime as dt
import random
from tkinter import (
    Tk, Frame, Label, Entry, Button, Canvas, StringVar, Text,
    BOTH, LEFT, RIGHT, END, X, W, FLAT, WORD, Y, BOTTOM,
)

# Eye-catching dark neon theme
BG = "#0B0E1A"
PANEL = "#141A2E"
PANEL_2 = "#1C2440"
LINE = "#2A3357"
TEXT = "#EDF1FF"
DIM = "#8A94B8"
GREEN = "#00E5A0"
CYAN = "#22D3EE"
YELLOW = "#FFB84D"
PINK = "#FF5C7A"

BOT_NAME = "Neony"

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the JavaScript developer sad? Because he didn't Node how to Express himself.",
    "There are 10 kinds of people: those who understand binary and those who don't.",
    "A SQL query walks into a bar, approaches two tables and asks: \"May I join you?\"",
    "Why did the developer go broke? He used up all his cache.",
]


# ===========================================================================
#  KEY CONCEPT: functions + if-elif  (the rule engine)
# ===========================================================================
def get_reply(user_text):
    """Return a predefined reply by matching keywords with if-elif."""
    text = user_text.lower().strip()

    # ---- greetings ----
    if text in ("hello", "hi", "hey", "hii", "hello!", "hi!", "hey!"):
        reply = "Hi!"
    elif "hello" in text or "hi " in text or text.startswith("hi"):
        reply = "Hello there! How can I help you?"
    # ---- how are you ----
    elif "how are you" in text or "how do you do" in text or "hru" in text:
        reply = "I'm fine, thanks! How about you?"
    elif "i am fine" in text or "i'm fine" in text or "good" == text:
        reply = "Glad to hear that! What can I do for you?"
    # ---- name / identity ----
    elif "your name" in text or "who are you" in text:
        reply = f"I'm {BOT_NAME}, your rule-based chatbot!"
    elif "my name" in text:
        name = user_text.split("name", 1)[-1].strip(" is:/,.!").strip()
        reply = f"Nice to meet you, {name}!" if name else "Tell me: my name is ..."
    elif "who made you" in text or "your maker" in text or "creator" in text:
        reply = "I was built with Python using simple if-elif rules!"
    # ---- help / capabilities ----
    elif "help" in text or "what can you do" in text:
        reply = ("I can chat! Try: 'how are you', 'tell me a joke', "
                 "'what time is it', 'bye'.")
    elif "joke" in text:
        reply = random.choice(JOKES)
    # ---- time / date ----
    elif "time" in text:
        reply = "It's " + dt.datetime.now().strftime("%H:%M:%S") + " right now."
    elif "date" in text or "day" in text:
        reply = "Today is " + dt.datetime.now().strftime("%d %b %Y") + "."
    # ---- feelings / small talk ----
    elif "i love you" in text:
        reply = "Aww, that's sweet! I love chatting with you too!"
    elif "thank" in text:
        reply = "You're welcome!"
    elif "sorry" in text:
        reply = "No problem at all!"
    elif "bye" in text or "goodbye" in text or "see you" in text or "exit" in text:
        reply = "Goodbye! Have a great day!"
    elif "weather" in text:
        reply = "I live inside a computer, so the weather is always sunny"
    elif "age" in text:
        reply = "I'm only a few lines of Python, but age is just a number!"
    elif "are you real" in text or "are you human" in text:
        reply = "Nope, I'm just if-elif rules pretending to be smart!"
    elif text in ("ok", "okay", "hmm", "k"):
        reply = "Anything else you want to ask?"
    elif text == "?":
        reply = "That's a deep question!"
    elif not text:
        reply = "Type something and press Enter!"
    # ---- fallback (every chatbot needs one) ----
    else:
        reply = ("I'm just a simple bot - try 'help' to see what I know!")
    return reply


def is_exit(user_text):
    """The loop stops when the user says bye."""
    return user_text.lower().strip() in ("bye", "goodbye", "exit", "quit", "q")


# ===========================================================================
#  KEY CONCEPT: loops + input/output  (terminal version)
# ===========================================================================
def run_cli():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    print("=" * 52)
    print(f"     {BOT_NAME} - Basic Rule-Based Chatbot")
    print("=" * 52)
    print("Talk to me! (type 'bye' to leave, 'help' for ideas)")

    talking = True
    while talking:                       # KEY CONCEPT: while loop
        user_text = input("\nYou: ").strip()
        reply = get_reply(user_text)     # KEY CONCEPT: if-elif rules
        print(f"{BOT_NAME}: {reply}")
        if is_exit(user_text):
            talking = False


# ===========================================================================
#  EYE-CATCHING GUI (same rules, chat-bubble style)
# ===========================================================================
class ChatApp:
    MAX_W = 460

    def __init__(self, root: Tk):
        self.root = root
        root.title(f"{BOT_NAME} - Rule Based Chatbot")
        root.geometry("620x720")
        root.minsize(520, 560)
        root.configure(bg=BG)

        self._build_header()
        self._build_chat_area()
        self._build_input_bar()
        self._bot_say(f"Hi! I'm {BOT_NAME}. Type a message or pick a chip "
                      "below - try 'help'!")

    # ---------------- layout ----------------
    def _build_header(self):
        head = Frame(self.root, bg=PANEL)
        head.pack(fill=X)
        inner = Frame(head, bg=PANEL)
        inner.pack(padx=18, pady=12)
        Label(inner, text="\U0001F916", font=("Segoe UI", 26),
              bg=PANEL).pack(side=LEFT, padx=(0, 12))
        left = Frame(inner, bg=PANEL)
        left.pack(side=LEFT)
        Label(left, text=BOT_NAME.upper(), font=("Segoe UI", 16, "bold"),
              fg=GREEN, bg=PANEL).pack(anchor=W)
        Label(left, text="online \u2022 rule-based \u2022 if-elif brain",
              font=("Segoe UI", 9), fg=DIM, bg=PANEL).pack(anchor=W)
        self.status_lbl = Label(inner, text="\u25CF", fg=GREEN, bg=PANEL,
                                font=("Segoe UI", 14))
        self.status_lbl.pack(side=RIGHT, padx=(12, 0))

    def _build_chat_area(self):
        self.chat = Canvas(self.root, bg=BG, highlightthickness=0)
        self.chat.pack(fill=BOTH, expand=True, padx=14, pady=14)
        self.chat.bind("<Configure>", lambda e: self._redraw())
        self.chat.bind_all("<MouseWheel>",
                           lambda e: self.chat.yview_scroll(-1 * (e.delta // 120),
                                                            "units"))
        self.bubbles = []                 # (text, is_user)
        self._offset = 0

    def _build_input_bar(self):
        bar = Frame(self.root, bg=PANEL)
        bar.pack(fill=X, side=BOTTOM)

        quick = Frame(bar, bg=PANEL)
        quick.pack(fill=X, padx=14, pady=(10, 2))
        for chip_text in ["hello", "how are you", "tell me a joke",
                          "what time is it", "help", "bye"]:
            c = Label(quick, text=chip_text, font=("Segoe UI", 9),
                      bg=PANEL_2, fg=CYAN, padx=10, pady=4, cursor="hand2")
            c.pack(side=LEFT, padx=(0, 6))
            c.bind("<Button-1>",
                   lambda e, t=chip_text: self._send_quick(t))
            c.bind("<Enter>", lambda e, w=c: w.config(bg="#243055"))
            c.bind("<Leave>", lambda e, w=c: w.config(bg=PANEL_2))

        row = Frame(bar, bg=PANEL)
        row.pack(fill=X, padx=14, pady=(6, 14))
        self.msg_var = StringVar()
        entry = Entry(row, textvariable=self.msg_var,
                      font=("Segoe UI", 12), bg="#0E1326", fg=TEXT,
                      insertbackground=GREEN, relief=FLAT,
                      highlightthickness=1, highlightcolor=GREEN,
                      highlightbackground=LINE)
        entry.pack(side=LEFT, fill=X, expand=True, ipady=8)
        entry.bind("<Return>", lambda e: self._send())
        self.send_btn = Button(row, text="SEND", font=("Segoe UI", 10, "bold"),
                               bg=GREEN, fg="#06251B", relief=FLAT,
                               padx=18, pady=8, cursor="hand2",
                               command=self._send)
        self.send_btn.pack(side=RIGHT, padx=(10, 0))
        entry.focus_set()
        self.entry = entry

    # ---------------- chat flow ----------------
    def _send_quick(self, text):
        self.msg_var.set(text)
        self._send()

    def _send(self):
        text = self.msg_var.get().strip()
        if not text:
            return
        self.msg_var.set("")
        self._user_say(text)
        reply = get_reply(text)
        self._bot_say(reply)
        if is_exit(text):
            self._bot_say("Refresh the window to chat again!")

    def _user_say(self, text):
        self.bubbles.append((text, True))
        self._redraw()

    def _bot_say(self, text):
        self.bubbles.append((text, False))
        self._redraw()

    # ---------------- bubble rendering ----------------
    def _redraw(self):
        c = self.chat
        c.delete("all")
        width = c.winfo_width()
        pad, gap, line_h = 12, 10, 16
        y = pad

        def wrap(txt, limit=48):
            words, lines, cur = txt.split(), [], ""
            for w in words:
                if len(cur) + len(w) + 1 <= limit:
                    cur = (cur + " " + w).strip()
                else:
                    lines.append(cur)
                    cur = w
            if cur:
                lines.append(cur)
            return lines or [""]

        for text, is_user in self.bubbles:
            lines = wrap(text)
            box_w = min(self.MAX_W, width - 90)
            h = 12 + line_h * len(lines)
            if is_user:
                x1 = width - pad - box_w
                x2 = width - pad
                fill, fg = PANEL_2, TEXT
                anchor_txt = x2 - 12
                justify = "right"
            else:
                x1, x2 = pad, pad + box_w
                fill, fg = "#0F2A26", TEXT
                anchor_txt = x1 + 12
                justify = "left"
            c.create_rectangle(x1, y, x2, y + h, fill=fill, outline=LINE)
            if not is_user:
                c.create_rectangle(x1, y, x1 + 3, y + h, fill=GREEN,
                                   outline=GREEN)
            for i, line in enumerate(lines):
                c.create_text(anchor_txt, y + 10 + i * line_h, text=line,
                              fill=fg, font=("Segoe UI", 11),
                              anchor="e" if is_user else "w")
            y += h + gap

        c.configure(scrollregion=(0, 0, width, y + pad))
        c.yview_moveto(1.0)


# ===========================================================================
def main():
    if "--cli" in sys.argv:
        run_cli()
        return
    root = Tk()
    ChatApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
