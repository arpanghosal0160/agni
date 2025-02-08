from core.weather import get_weather
from core.news import get_news
from core.ai_tasks import answer_question
from core.desktop_ops import open_file, search_files

def display_menu():
    print("\nMenu:")
    print("1. Get weather information")
    print("2. Get top news")
    print("3. Ask any question (AI)")
    print("4. Open a file")
    print("5. Search for files")
    print("6. Exit")
    print("\n")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            city = input("Enter city name: ")
            weather = get_weather(city)
            print(f"Weather in {city}: {weather}")
        elif choice == '2':
            news = get_news()
            print("Top News:")
            for article in news:
                print(f"- {article['title']}")
        elif choice == '3':
            query = input("Enter your question: ")
            print("Delegating task to AI model...")
            answer = answer_question(query)
            print(f"Answer: {answer}")
        elif choice == '4':
            file_path = input("Enter the full path of the file to open: ")
            result = open_file(file_path)
            print(result)
        elif choice == '5':
            directory = input("Enter directory to search: ")
            filename = input("Enter the filename to search for: ")
            result = search_files(directory, filename)
            print(result)
        elif choice == '6':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
