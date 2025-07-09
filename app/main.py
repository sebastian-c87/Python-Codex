"""Simple Tkinter GUI for AI Code Debugger."""

import tkinter as tk
from tkinter import scrolledtext, messagebox

from .debugger import analyze_code
from .db import save_analysis
from .openai_client import get_refactor_suggestions


class DebuggerApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("AI Code Debugger")

        # Text area for Python code
        self.code_text = scrolledtext.ScrolledText(self, width=80, height=20)
        self.code_text.pack(padx=10, pady=10)

        self.analyze_button = tk.Button(self, text="Analyze", command=self.analyze)
        self.analyze_button.pack(pady=5)

        # Output area
        self.result_text = scrolledtext.ScrolledText(self, width=80, height=15, state="disabled")
        self.result_text.pack(padx=10, pady=10)

    def analyze(self) -> None:
        code = self.code_text.get("1.0", tk.END)
        analysis, ok = analyze_code(code)
        suggestions = get_refactor_suggestions(code)
        save_analysis(code, analysis, suggestions)
        result = f"Pyflakes output:\n{analysis}\n\nSuggestions:\n{suggestions}"
        self.result_text.configure(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.configure(state="disabled")
        if ok:
            messagebox.showinfo("Analysis Complete", "No issues detected by pyflakes.")
        else:
            messagebox.showwarning("Analysis Complete", "Issues detected in code.")


def main() -> None:
    app = DebuggerApp()
    app.mainloop()


if __name__ == "__main__":
    main()
