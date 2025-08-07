import datetime
import webbrowser

def Action(message: str) -> str:
    msg = message.lower().strip()

    # === Greetings & Basic Interactions ===
    greetings = ["hello", "hi", "hey", "hi there", "hello eva", "hey eva"]
    if any(greet in msg for greet in greetings):
        return "Hello! I'm Eva, your assistant. How can I help you today?"

    if "your name" in msg or "who are you" in msg:
        return "I'm Eva, your personal assistant!"

    if "how are you" in msg:
        return "I'm great, thanks for asking! How about you?"

    if "thank you" in msg or "thanks" in msg:
        return "You're welcome! 😊"

    if "good morning" in msg:
        return "Good morning! I hope your day starts well."

    if "good night" in msg:
        return "Good night! Sweet dreams. 🌙"

    if "good evening" in msg:
        return "Good evening! What can I do for you tonight?"

    # === Date & Time ===
    if "time" in msg:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M')}."

    if "date" in msg:
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%d %B %Y')}."

    # === Open Websites ===
    if "open google" in msg:
        webbrowser.open("https://www.google.com")
        return "Opening Google..."

    if "open youtube" in msg:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."

    if "open github" in msg:
        webbrowser.open("https://www.github.com")
        return "Opening GitHub..."

    if "open chatgpt" in msg:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT..."

    if "open stackoverflow" in msg:
        webbrowser.open("https://stackoverflow.com")
        return "Opening Stack Overflow..."

    if "open linkedin" in msg:
        webbrowser.open("https://www.linkedin.com")
        return "Opening LinkedIn..."

    # === Weather & Location ===
    if "weather" in msg or "forecast" in msg:
        webbrowser.open("https://www.google.com/search?q=weather")
        return "Here is the latest weather report."

    if "find hospital" in msg:
        webbrowser.open("https://www.google.com/maps/search/nearest+hospital")
        return "Showing hospitals near you."

    if "nearest atm" in msg or "find atm" in msg:
        webbrowser.open("https://www.google.com/maps/search/nearest+atm")
        return "Here are some nearby ATMs."

    if "airport directions" in msg or "how to get to airport" in msg:
        webbrowser.open("https://www.google.com/maps/search/nearest+airport")
        return "Here’s how to get to the nearest airport."

    # === General Knowledge ===
    if "capital of india" in msg:
        return "The capital of India is New Delhi."

    if "national animal of india" in msg:
        return "The Bengal tiger is the national animal of India."

    if "largest ocean" in msg:
        return "The Pacific Ocean is the largest ocean on Earth."

    if "longest river" in msg:
        return "The Nile is considered the longest river in the world."

    if "tallest mountain" in msg:
        return "Mount Everest is the tallest mountain above sea level."

    if "fastest land animal" in msg:
        return "The cheetah is the fastest land animal."

    if "largest desert" in msg:
        return "The Antarctic Desert is the largest desert in the world."

    if "deepest ocean" in msg:
        return "The Mariana Trench in the Pacific Ocean is the deepest."

    # === Math & Conversions ===
    if "square root of 144" in msg:
        return "The square root of 144 is 12."

    if "is 17 a prime" in msg:
        return "Yes, 17 is a prime number."

    if "what is pi" in msg:
        return "Pi is approximately 3.14159."

    if "days in a leap year" in msg:
        return "A leap year has 366 days."

    if "convert 5 km to miles" in msg:
        return "5 kilometers is approximately 3.11 miles."

    if "25% of 200" in msg:
        return "25% of 200 is 50."

    if "convert 100 dollars" in msg:
        return "100 USD is approximately 8300 INR (check current rates)."

    # === Science & Tech ===
    if "who discovered gravity" in msg:
        return "Sir Isaac Newton discovered gravity."

    if "who invented electricity" in msg:
        return "Electricity wasn't 'invented', but Benjamin Franklin made landmark contributions."

    if "first man on moon" in msg:
        return "Neil Armstrong walked on the moon first in 1969."

    if "what is a black hole" in msg:
        return "A black hole is a region of space where gravity is so strong that nothing can escape."

    if "machine learning" in msg:
        return "Machine learning is a branch of AI where algorithms learn from data."

    if "cloud computing" in msg:
        return "Cloud computing lets you use computing services over the internet."

    if "what is ai" in msg:
        return "AI stands for Artificial Intelligence, and it enables machines to mimic human intelligence."

    if "what is python" in msg:
        return "Python is a high-level, widely-used programming language."

    # === People & Personalities ===
    if "who is bill gates" in msg:
        return "Bill Gates co‑founded Microsoft and is a philanthropist."

    if "who is elon musk" in msg:
        return "Elon Musk leads Tesla and SpaceX."

    if "who is the prime minister" in msg:
        return "The Prime Minister of India is Narendra Modi."

    if "who is president of usa" in msg or "who is president of the usa" in msg:
        return "As of today, the President of the USA is Joe Biden."

    # === Productivity & Study Help ===
    if "study tips" in msg:
        return "Use active recall, spaced repetition, stay hydrated, and avoid multitasking."

    if "how to focus" in msg:
        return "Try the Pomodoro technique, block distractions, and set clear goals."

    if "career advice" in msg:
        return "Pursue your passion, keep learning, and network with others."

    if "improve vocabulary" in msg:
        return "Read widely, use vocabulary tools, and learn a few new words daily."

    if "learn coding" in msg:
        return "Start with Python or JavaScript; use platforms like freeCodeCamp or LeetCode."

    if "how to get better at math" in msg:
        return "Practice consistently, understand core concepts, and apply to real-world problems."

    # === Entertainment & Fun ===
    if "tell me a joke" in msg:
        return "Why did the scarecrow win an award? Because he was outstanding in his field!"

    if "motivate me" in msg or "inspire me" in msg:
        return "Believe in yourself—every day is a new chance to grow stronger!"

    if "fun fact" in msg:
        return "Did you know? Octopuses have three hearts and blue blood."

    if "word of the day" in msg:
        return "Word of the day: Ephemeral – lasting for a very short time."

    if "suggest a movie" in msg:
        return "Try watching 'Inception', 'The Shawshank Redemption', or 'Interstellar'."

    # === Utilities & Entertainment ===
    if "play music" in msg:
        webbrowser.open("https://www.youtube.com/results?search_query=relaxing+music")
        return "Playing relaxing music on YouTube."

    if "latest news" in msg or "headlines" in msg:
        webbrowser.open("https://news.google.com")
        return "Here are today’s top news headlines."

    if "cricket score" in msg:
        webbrowser.open("https://www.google.com/search?q=live+cricket+score")
        return "Here’s the latest cricket score."

    if "set a timer" in msg or "remind me" in msg:
        return "I'd recommend using your device’s timer or reminder app."

    if "battery percentage" in msg:
        return "Please check your device screen or settings for your battery status."

    if "where is my phone" in msg:
        return "Try 'Find My Device' on Google or iCloud, depending on your device."

    if "calendar" in msg or "what's on my calendar" in msg:
        return "Open your calendar app to check today's events."

    if "symptoms of cold" in msg:
        return "Common cold symptoms include sneezing, sore throat, and a runny nose."

    if "covid symptoms" in msg:
        return "COVID‑19 symptoms often include fever, dry cough, and fatigue."

    # === Default Catch-All ===
    return "I'm not sure how to help with that. Try asking in a different way 😊"

# Example interactive loop
if __name__ == "_main_":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Eva: Goodbye! Have a great day 😊")
            break
        print("Eva:", Action(user_input))
        
        