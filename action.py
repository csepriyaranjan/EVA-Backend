import datetime

def Action(message: str):
    msg = message.lower().strip()

    # === Greetings & Basic Interactions ===
    greetings = ["hello", "hi", "hey", "hi there", "hello eva", "hey eva"]
    if any(greet in msg for greet in greetings):
        return {"message": "Hello! I'm Eva, your assistant. How can I help you today?"}

    if "your name" in msg or "who are you" in msg:
        return {"message": "I'm Eva, your personal assistant!"}

    if "how are you" in msg:
        return {"message": "I'm great, thanks for asking! How about you?"}

    if "thank you" in msg or "thanks" in msg:
        return {"message": "You're welcome! 😊"}

    if "good morning" in msg:
        return {"message": "Good morning! I hope your day starts well."}

    if "good night" in msg:
        return {"message": "Good night! Sweet dreams. 🌙"}

    if "good evening" in msg:
        return {"message": "Good evening! What can I do for you tonight?"}

    # === Date & Time ===
    if "time" in msg:
        now = datetime.datetime.now()
        return {"message": f"The current time is {now.strftime('%H:%M')}."}

    if "date" in msg:
        today = datetime.date.today()
        return {"message": f"Today's date is {today.strftime('%d %B %Y')}."}

    # === Open Websites (send to frontend to open) ===
    if "open google" in msg:
        return {"action": "open_url", "url": "https://www.google.com", "message": "Opening Google..."}

    if "open youtube" in msg:
        return {"action": "open_url", "url": "https://www.youtube.com", "message": "Opening YouTube..."}

    if "open github" in msg:
        return {"action": "open_url", "url": "https://www.github.com", "message": "Opening GitHub..."}

    if "open chatgpt" in msg:
        return {"action": "open_url", "url": "https://chat.openai.com", "message": "Opening ChatGPT..."}

    if "open stackoverflow" in msg:
        return {"action": "open_url", "url": "https://stackoverflow.com", "message": "Opening Stack Overflow..."}

    if "open linkedin" in msg:
        return {"action": "open_url", "url": "https://www.linkedin.com", "message": "Opening LinkedIn..."}

    # === Weather & Location ===
    if "weather" in msg or "forecast" in msg:
        return {"action": "open_url", "url": "https://www.google.com/search?q=weather", "message": "Here is the latest weather report."}

    if "find hospital" in msg:
        return {"action": "open_url", "url": "https://www.google.com/maps/search/nearest+hospital", "message": "Showing hospitals near you."}

    if "nearest atm" in msg or "find atm" in msg:
        return {"action": "open_url", "url": "https://www.google.com/maps/search/nearest+atm", "message": "Here are some nearby ATMs."}

    if "airport directions" in msg or "how to get to airport" in msg:
        return {"action": "open_url", "url": "https://www.google.com/maps/search/nearest+airport", "message": "Here’s how to get to the nearest airport."}

    # === General Knowledge ===
    facts = {
        "capital of india": "The capital of India is New Delhi.",
        "national animal of india": "The Bengal tiger is the national animal of India.",
        "largest ocean": "The Pacific Ocean is the largest ocean on Earth.",
        "longest river": "The Nile is considered the longest river in the world.",
        "tallest mountain": "Mount Everest is the tallest mountain above sea level.",
        "fastest land animal": "The cheetah is the fastest land animal.",
        "largest desert": "The Antarctic Desert is the largest desert in the world.",
        "deepest ocean": "The Mariana Trench in the Pacific Ocean is the deepest."
    }
    for key, val in facts.items():
        if key in msg:
            return {"message": val}

    # === Math & Conversions ===
    math_answers = {
        "square root of 144": "The square root of 144 is 12.",
        "is 17 a prime": "Yes, 17 is a prime number.",
        "what is pi": "Pi is approximately 3.14159.",
        "days in a leap year": "A leap year has 366 days.",
        "convert 5 km to miles": "5 kilometers is approximately 3.11 miles.",
        "25% of 200": "25% of 200 is 50.",
        "convert 100 dollars": "100 USD is approximately 8300 INR (check current rates)."
    }
    for key, val in math_answers.items():
        if key in msg:
            return {"message": val}

    # === Science & Tech ===
    science_answers = {
        "who discovered gravity": "Sir Isaac Newton discovered gravity.",
        "who invented electricity": "Electricity wasn't 'invented', but Benjamin Franklin made landmark contributions.",
        "first man on moon": "Neil Armstrong walked on the moon first in 1969.",
        "what is a black hole": "A black hole is a region of space where gravity is so strong that nothing can escape.",
        "machine learning": "Machine learning is a branch of AI where algorithms learn from data.",
        "cloud computing": "Cloud computing lets you use computing services over the internet.",
        "what is ai": "AI stands for Artificial Intelligence, and it enables machines to mimic human intelligence.",
        "what is python": "Python is a high-level, widely-used programming language."
    }
    for key, val in science_answers.items():
        if key in msg:
            return {"message": val}

    # === People & Personalities ===
    people_answers = {
        "who is bill gates": "Bill Gates co-founded Microsoft and is a philanthropist.",
        "who is elon musk": "Elon Musk leads Tesla and SpaceX.",
        "who is the prime minister": "The Prime Minister of India is Narendra Modi.",
        "who is president of usa": "As of today, the President of the USA is Joe Biden.",
        "who is president of the usa": "As of today, the President of the USA is Joe Biden."
    }
    for key, val in people_answers.items():
        if key in msg:
            return {"message": val}

    # === Productivity & Study Help ===
    productivity_answers = {
        "study tips": "Use active recall, spaced repetition, stay hydrated, and avoid multitasking.",
        "how to focus": "Try the Pomodoro technique, block distractions, and set clear goals.",
        "career advice": "Pursue your passion, keep learning, and network with others.",
        "improve vocabulary": "Read widely, use vocabulary tools, and learn a few new words daily.",
        "learn coding": "Start with Python or JavaScript; use platforms like freeCodeCamp or LeetCode.",
        "how to get better at math": "Practice consistently, understand core concepts, and apply to real-world problems."
    }
    for key, val in productivity_answers.items():
        if key in msg:
            return {"message": val}

    # === Entertainment & Fun ===
    entertainment_answers = {
        "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "motivate me": "Believe in yourself—every day is a new chance to grow stronger!",
        "inspire me": "Believe in yourself—every day is a new chance to grow stronger!",
        "fun fact": "Did you know? Octopuses have three hearts and blue blood.",
        "word of the day": "Word of the day: Ephemeral – lasting for a very short time.",
        "suggest a movie": "Try watching 'Inception', 'The Shawshank Redemption', or 'Interstellar'."
    }
    for key, val in entertainment_answers.items():
        if key in msg:
            return {"message": val}

    # === Utilities ===
    if "play music" in msg:
        return {"action": "open_url", "url": "https://www.youtube.com/results?search_query=relaxing+music", "message": "Playing relaxing music on YouTube."}

    if "latest news" in msg or "headlines" in msg:
        return {"action": "open_url", "url": "https://news.google.com", "message": "Here are today’s top news headlines."}

    if "cricket score" in msg:
        return {"action": "open_url", "url": "https://www.google.com/search?q=live+cricket+score", "message": "Here’s the latest cricket score."}

    if "set a timer" in msg or "remind me" in msg:
        return {"message": "I'd recommend using your device’s timer or reminder app."}

    if "battery percentage" in msg:
        return {"message": "Please check your device screen or settings for your battery status."}

    if "where is my phone" in msg:
        return {"message": "Try 'Find My Device' on Google or iCloud, depending on your device."}

    if "calendar" in msg or "what's on my calendar" in msg:
        return {"message": "Open your calendar app to check today's events."}

    if "symptoms of cold" in msg:
        return {"message": "Common cold symptoms include sneezing, sore throat, and a runny nose."}

    if "covid symptoms" in msg:
        return {"message": "COVID-19 symptoms often include fever, dry cough, and fatigue."}

    # === Default Catch-All ===
    return {"message": "I'm not sure how to help with that. Try asking in a different way 😊"}


# Example interactive loop (local testing)
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Eva: Goodbye! Have a great day 😊")
            break
        print("Eva:", Action(user_input))
