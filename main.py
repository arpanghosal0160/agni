import speech_recognition as sr
from core.weather import get_weather
from core.news import get_news
from core.ai_tasks import answer_question
from core.desktop_ops import open_file, search_files

def app_intro():
    print("=" * 50)
    print("🤖 Welcome to Aagni - Your AI-Powered Desktop Assistant! 🔥")
    print("I can help you with the following tasks:")
    print("• Fetch weather information 🌦️")
    print("• Provide the latest news 🗞️")
    print("• Answer your AI-driven queries 🧠")
    print("• Open and search for files on your system 📂")
    print("• Understand your commands through voice 🎙️")
    print("=" * 50)

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Speech recognition service is unavailable."

def interpret_and_execute(command):
    if "weather" in command:
        city = input("Enter city name: ")
        weather = get_weather(city)
        print(f"Weather in {city}: {weather}")
    elif "news" in command:
        news = get_news()
        print("Top News:")
        for article in news:
            print(f"- {article['title']}")
    elif "question" in command or "ai" in command:
        query = input("Enter your question: ")
        print("Delegating task to AI model...")
        answer = answer_question(query)
        print(f"Answer: {answer}")
    elif "open file" in command:
        file_path = input("Enter the full path of the file to open: ")
        result = open_file(file_path)
        print(result)
    elif "search file" in command:
        directory = input("Enter directory to search: ")
        filename = input("Enter the filename to search for: ")
        result = search_files(directory, filename)
        print(result)
    elif "exit" in command:
        print("Exiting the application... Goodbye!")
        exit()
    else:
        print("Sorry, I didn't understand the command.")

def main():
    app_intro()
    while True:
        print("\nSpeak your command or type 'exit' to quit.")
        command = recognize_speech()
        interpret_and_execute(command)

if __name__ == "__main__":
    main()
