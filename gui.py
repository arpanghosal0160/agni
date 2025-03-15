import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk
import speech_recognition as sr
import webbrowser
from core.weather import get_weather
from core.news import get_news, categorize_news, summarize_text
from core.ai_tasks import answer_question
from core.desktop_ops import open_file, search_files
from styles import apply_styles

class AagniApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aagni - AI-Powered Desktop Assistant")
        self.root.geometry("800x600")
        apply_styles(self.root)
        self.create_widgets()
        self.animate_intro()

    def create_widgets(self):
        self.intro_label = ttk.Label(self.root, text="🤖 Welcome to Aagni - Your AI-Powered Desktop Assistant! 🔥", font=("Helvetica", 16))
        self.intro_label.pack(pady=10)

        self.command_label = ttk.Label(self.root, text="Enter your command:", font=("Helvetica", 12))
        self.command_label.pack(pady=5)

        self.command_entry = ttk.Entry(self.root, width=50)
        self.command_entry.pack(pady=5)

        self.execute_button = ttk.Button(self.root, text="Execute", command=self.execute_command)
        self.execute_button.pack(pady=5)

        self.mic_button = ttk.Button(self.root, text="🎤 Speak", command=self.voice_command)
        self.mic_button.pack(pady=5)

        self.output_text = tk.Text(self.root, height=15, width=80, wrap=tk.WORD)
        self.output_text.pack(pady=10)

        self.image_label = ttk.Label(self.root)
        self.image_label.pack(pady=10)

    def animate_intro(self):
        self.intro_text = "🤖 Welcome to Aagni - Your AI-Powered Desktop Assistant! 🔥"
        self.intro_index = 0
        self.update_intro_text()

    def update_intro_text(self):
        if self.intro_index < len(self.intro_text):
            self.intro_label.config(text=self.intro_text[:self.intro_index + 1])
            self.intro_index += 1
            self.root.after(100, self.update_intro_text)

    def execute_command(self):
        command = self.command_entry.get().lower()
        self.output_text.delete(1.0, tk.END)
        self.interpret_and_execute(command)

        # Continuous conversation: Keep the input field ready for the next command
        self.command_entry.delete(0, tk.END)
        self.command_entry.focus()

    def voice_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.output_text.insert(tk.END, "Listening...\n")
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, f"You said: {command}\n")
                self.interpret_and_execute(command)
            except sr.UnknownValueError:
                self.output_text.insert(tk.END, "Sorry, could not understand the audio.\n")
            except sr.RequestError:
                self.output_text.insert(tk.END, "Could not request results. Check your internet connection.\n")

    def interpret_and_execute(self, command):
        if "weather" in command:
            city = self.prompt_user("Enter city name:")
            weather = get_weather(city)
            self.output_text.insert(tk.END, f"Weather in {city}: {weather}\n")
        elif "news" in command:
            query = self.prompt_user("What kind of news are you interested in?")
            category = categorize_news(query)
            news = get_news(category)
            self.output_text.insert(tk.END, f"Top {category.capitalize()} News:\n")
            for article in news:
                self.output_text.insert(tk.END, f"- {article['title']}\n")
                summary = summarize_text(article['description'])
                self.output_text.insert(tk.END, f"Summary: {summary}\n\n")
        elif "question" in command or "ai" in command:
            query = self.prompt_user("Enter your question:")
            answer = answer_question(query)
            self.output_text.insert(tk.END, f"Answer: {answer}\n")
        elif "open file" in command:
            file_path = self.prompt_user("Enter the full path of the file to open:")
            result = open_file(file_path)
            self.output_text.insert(tk.END, f"{result}\n")
        elif "search file" in command:
            directory = self.prompt_user("Enter directory to search:")
            filename = self.prompt_user("Enter the filename to search for:")
            result = search_files(directory, filename)
            self.output_text.insert(tk.END, f"{result}\n")
        elif "send a message" in command:
            phone_number = self.prompt_user("Please specify the phone number with country code:")
            message = self.prompt_user("What message would you like to send?")
            whatsapp_url = f"https://wa.me/{phone_number}?text={message}"
            self.output_text.insert(tk.END, "Opening WhatsApp to send your message.\n")
            webbrowser.open(whatsapp_url)
        elif "open youtube" in command:
            self.output_text.insert(tk.END, "Opening YouTube...\n")
            webbrowser.open("https://www.youtube.com")
        elif "exit" in command:
            self.root.quit()
        else:
            self.output_text.insert(tk.END, "Sorry, I didn't understand the command.\n")

        # Keep the conversation going
        self.command_entry.delete(0, tk.END)
        self.command_entry.focus()

    def prompt_user(self, prompt):
        return simpledialog.askstring("Input", prompt)

if __name__ == "__main__":
    root = tk.Tk()
    app = AagniApp(root)
    root.mainloop()
