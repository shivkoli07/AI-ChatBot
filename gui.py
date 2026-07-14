import tkinter as tk
from tkinter import font as tkfont

# Assuming this is in your same directory
from chatbot import get_bot_response

# =========================================================
# THEME — Sleek Black & Silver
# =========================================================

BG_APP = "#050505"        # Pure deep black/grey background
BG_PANEL = "#121212"      # Slightly elevated black for chat area
BG_HEADER = "#0A0A0A"     # Pitch black header
BUBBLE_BOT = "#242424"    # Dark grey bot bubble
BUBBLE_USER = "#D4D4D8"   # Bright silver user bubble
BORDER_SOFT = "#3F3F46"   # Metallic dark grey border
ACCENT = "#A1A1AA"        # Base silver accent
ACCENT_HOVER = "#F4F4F5"  # Bright white-silver for hover state
TEXT_PRIMARY = "#F8FAFC"  # White text for dark backgrounds
TEXT_USER_BUBBLE = "#050505" # Black text for the silver user bubble
TEXT_MUTED = "#71717A"    # Muted grey for subtext and footer
TEXT_LABEL_BOT = "#A1A1AA"
TEXT_LABEL_USER = "#D4D4D8"

FONT_FAMILY = "Segoe UI"

# =========================================================
# Helper: rounded rectangle on a Canvas
# =========================================================

def draw_rounded_rect(canvas, x1, y1, x2, y2, radius=16, **kwargs):
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1,
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

# =========================================================
# A single chat bubble — sized to fit its own text
# =========================================================

class ChatBubble(tk.Canvas):

    MAX_TEXT_WIDTH = 440

    def __init__(self, parent, text, is_user):
        super().__init__(parent, bg=BG_PANEL, highlightthickness=0, bd=0)

        fill = BUBBLE_USER if is_user else BUBBLE_BOT
        outline = ACCENT if is_user else BORDER_SOFT
        text_color = TEXT_USER_BUBBLE if is_user else TEXT_PRIMARY
        pad_x, pad_y = 18, 12 

        msg_font = tkfont.Font(family=FONT_FAMILY, size=11)

        # Measure the wrapped text size
        probe = self.create_text(
            0, 0,
            text=text,
            font=msg_font,
            width=self.MAX_TEXT_WIDTH,
            anchor="nw"
        )
        bbox = self.bbox(probe)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        self.delete(probe)

        width = text_w + pad_x * 2
        height = text_h + pad_y * 2

        self.configure(width=width, height=height)

        draw_rounded_rect(
            self, 1, 1, width - 1, height - 1,
            radius=18,
            fill=fill,
            outline=outline,
            width=1
        )

        self.create_text(
            pad_x, pad_y,
            text=text,
            font=msg_font,
            fill=text_color,
            anchor="nw",
            width=self.MAX_TEXT_WIDTH
        )

# =========================================================
# A rounded, hover-reactive button drawn on a Canvas
# =========================================================

class GlassButton(tk.Canvas):

    def __init__(self, parent, text, command, width=100, height=40,
                 fill=ACCENT, hover_fill=ACCENT_HOVER, text_color="#050505"):
        super().__init__(parent, width=width, height=height,
                          bg=BG_APP, highlightthickness=0, bd=0, cursor="hand2")

        self.command = command
        self.fill = fill
        self.hover_fill = hover_fill
        self.text_color = text_color
        self.w = width
        self.h = height
        self.label = text

        self._render(fill)

        self.bind("<Enter>", lambda e: self._render(self.hover_fill))
        self.bind("<Leave>", lambda e: self._render(self.fill))
        self.bind("<Button-1>", lambda e: self.command())

    def _render(self, color):
        self.delete("all")
        draw_rounded_rect(self, 1, 1, self.w - 1, self.h - 1,
                           radius=self.h // 2, fill=color, outline="")
        self.create_text(
            self.w / 2, self.h / 2,
            text=self.label,
            font=tkfont.Font(family=FONT_FAMILY, size=10, weight="bold"),
            fill=self.text_color
        )

# =========================================================
# Main application window
# =========================================================

class ChatbotGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot — AI Assistant")
        
        # Center window on screen (Reduced height to 700 to prevent bottom cutoff on smaller screens)
        window_width, window_height = 720, 700
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        self.root.configure(bg=BG_APP)
        self.root.resizable(False, False)

        self.create_widgets()
        
        # Startup greeting
        self.root.after(500, lambda: self.display_bot_message("System initialized. Hello! I'm ChatBot, ready to assist you."))

    # --------------------------------------------------
    # Layout
    # --------------------------------------------------

    def create_widgets(self):

        # ---------------- Header (Packed First, anchors to TOP) ----------------
        self.header = tk.Frame(self.root, bg=BG_HEADER, height=78)
        self.header.pack(side=tk.TOP, fill=tk.X)
        self.header.pack_propagate(False)

        title_wrap = tk.Frame(self.header, bg=BG_HEADER)
        title_wrap.pack(side=tk.LEFT, padx=24, pady=14)

        tk.Label(
            title_wrap,
            text="🤖  ChatBot",
            font=(FONT_FAMILY, 18, "bold"),
            bg=BG_HEADER,
            fg=TEXT_PRIMARY
        ).pack(anchor="w")

        tk.Label(
            title_wrap,
            text="AI Assistant",
            font=(FONT_FAMILY, 9),
            bg=BG_HEADER,
            fg=TEXT_MUTED
        ).pack(anchor="w")

        # Status pill
        status_wrap = tk.Frame(self.header, bg=BG_HEADER)
        status_wrap.pack(side=tk.RIGHT, padx=24)

        self.status_dot = tk.Canvas(status_wrap, width=10, height=10,
                                     bg=BG_HEADER, highlightthickness=0)
        self.status_dot.pack(side=tk.LEFT, pady=20)
        self.status_dot.create_oval(1, 1, 9, 9, fill="#10B981", outline="") # Green online indicator

        tk.Label(
            status_wrap,
            text="Online",
            font=(FONT_FAMILY, 9, "bold"),
            bg=BG_HEADER,
            fg="#10B981"
        ).pack(side=tk.LEFT, padx=(6, 0), pady=20)

        # Thin silver divider
        tk.Frame(self.root, bg=BORDER_SOFT, height=1).pack(side=tk.TOP, fill=tk.X)

        # ---------------- Footer (Packed Second, anchors strictly to BOTTOM) ----------------
        self.footer = tk.Label(
            self.root,
            text="Developed by Shiv Koli",
            bg=BG_APP,
            fg=TEXT_MUTED,
            font=(FONT_FAMILY, 9, "bold")
        )
        self.footer.pack(side=tk.BOTTOM, fill=tk.X, pady=(0, 12))

        # ---------------- Bottom input bar (Packed Third, anchors to BOTTOM above footer) ----------------
        bottom_wrap = tk.Frame(self.root, bg=BG_APP)
        bottom_wrap.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=(10, 10))

        input_card = tk.Frame(bottom_wrap, bg=BG_PANEL, highlightthickness=1,
                               highlightbackground=BORDER_SOFT, highlightcolor=ACCENT)
        input_card.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6)

        self.user_input = tk.Entry(
            input_card,
            font=(FONT_FAMILY, 12),
            bg=BG_PANEL,
            fg=TEXT_PRIMARY,
            insertbackground=TEXT_PRIMARY,
            relief=tk.FLAT,
            highlightthickness=0,
            border=0
        )
        self.user_input.pack(fill=tk.BOTH, expand=True, padx=16, pady=6)
        self.user_input.bind("<Return>", lambda event: self.send_message())
        self.user_input.focus_set()

        self.send_button = GlassButton(
            bottom_wrap, "Send ➤", self.send_message, width=110, height=44
        )
        self.send_button.pack(side=tk.RIGHT, padx=(12, 0))

        # ---------------- Scrollable chat area (Packed Last, fills remaining space) ----------------
        chat_outer = tk.Frame(self.root, bg=BG_PANEL)
        chat_outer.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=0, pady=0)

        self.chat_canvas = tk.Canvas(chat_outer, bg=BG_PANEL, highlightthickness=0, bd=0)
        self.scrollbar = tk.Scrollbar(chat_outer, orient="vertical", command=self.chat_canvas.yview)
        
        self.chat_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.messages_frame = tk.Frame(self.chat_canvas, bg=BG_PANEL)
        self.messages_window = self.chat_canvas.create_window(
            (0, 0), window=self.messages_frame, anchor="nw"
        )

        self.messages_frame.bind(
            "<Configure>",
            lambda e: self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))
        )
        self.chat_canvas.bind(
            "<Configure>",
            lambda e: self.chat_canvas.itemconfig(self.messages_window, width=e.width)
        )

        # Mouse-wheel scrolling
        self.chat_canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    # --------------------------------------------------
    # Scrolling helper
    # --------------------------------------------------

    def _on_mousewheel(self, event):
        self.chat_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # --------------------------------------------------
    # Message rendering
    # --------------------------------------------------

    def _add_bubble(self, text, is_user):
        row = tk.Frame(self.messages_frame, bg=BG_PANEL)
        row.pack(fill=tk.X, padx=20, pady=8)

        label_text = "You" if is_user else "ChatBot"
        label_color = TEXT_LABEL_USER if is_user else TEXT_LABEL_BOT
        anchor_side = tk.RIGHT if is_user else tk.LEFT

        col = tk.Frame(row, bg=BG_PANEL)
        col.pack(side=anchor_side)

        tk.Label(
            col,
            text=label_text,
            font=(FONT_FAMILY, 8, "bold"),
            bg=BG_PANEL,
            fg=label_color
        ).pack(anchor="e" if is_user else "w", padx=4, pady=(0, 2))

        bubble = ChatBubble(col, text, is_user)
        bubble.pack(anchor="e" if is_user else "w")

        # Scroll to bottom smoothly
        self.root.after(10, self._scroll_to_bottom)

    def _scroll_to_bottom(self):
        self.chat_canvas.update_idletasks()
        self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))
        self.chat_canvas.yview_moveto(1.0)

    def display_bot_message(self, message):
        self._add_bubble(message, is_user=False)

    def display_user_message(self, message):
        self._add_bubble(message, is_user=True)

    # --------------------------------------------------
    # Sending
    # --------------------------------------------------

    def send_message(self):
        message = self.user_input.get().strip()

        if message == "":
            return

        self.display_user_message(message)
        self.user_input.delete(0, tk.END)

        # Assuming get_bot_response is imported from chatbot.py
        response = get_bot_response(message)
        self.display_bot_message(response)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()