import datetime

# Bride and Groom Details
bride = {
    "name": "Priya Sharma",
    "age": 24,
    "family": "Sharma Family"
}

groom = {
    "name": "Rahul Verma",
    "age": 26,
    "family": "Verma Family"
}

# Wedding Event Details
events = {
    "marriage": {
        "title": "Marriage Ceremony",
        "date": "12-April-2025",
        "time": "7:00 PM",
        "venue": "Royal Palace, Delhi"
    },
    "haldi": {
        "title": "Haldi Function",
        "date": "10-April-2025",
        "time": "10:00 AM",
        "venue": "Bride's Residence"
    },
    "mehendi": {
        "title": "Mehendi Function",
        "date": "11-April-2025",
        "time": "3:00 PM",
        "venue": "Groom's Residence"
    },
    "ring ceremony": {
        "title": "Ring Ceremony",
        "date": "09-April-2025",
        "time": "6:00 PM",
        "venue": "Taj Banquet Hall"
    }
}

# History of Searches
search_log = {}

# Function to simulate chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "bride":
        return f"👰 Bride: {bride['name']}, Age: {bride['age']}, Family: {bride['family']}"

    elif user_input == "groom":
        return f"🤵 Groom: {groom['name']}, Age: {groom['age']}, Family: {groom['family']}"

    elif user_input in events:
        now = datetime.datetime.now()
        event = events[user_input]
        
        # Update history
        if user_input not in search_log:
            search_log[user_input] = []
        search_log[user_input].append(now)
        
        response = f"""
📅 {event['title']} Details:
📍 Venue : {event['venue']}
📆 Date  : {event['date']}
🕓 Time  : {event['time']}

📘 Search History:
🔁 Searched {len(search_log[user_input])} time(s)
🕒 Last searched: {now.strftime('%d-%b-%Y %I:%M:%S %p')}
"""
        return response.strip()
    
    elif user_input == "help":
        return "🔎 You can ask about: bride, groom, marriage, haldi, mehendi, ring ceremony.\nType 'exit' to quit."

    elif user_input == "history":
        if not search_log:
            return "📘 No events have been searched yet."
        history_text = "📘 Search History:\n"
        for event, times in search_log.items():
            last_time = times[-1].strftime('%d-%b-%Y %I:%M:%S %p')
            history_text += f"🔸 {event.title()}: {len(times)} times, last on {last_time}\n"
        return history_text.strip()

    elif user_input == "exit":
        return None  # To end the loop

    else:
        return "❌ Sorry, I didn't understand that. Type 'help' to see options."

# Chatbot Welcome Message
print("💬 Welcome to the Wedding Chatbot!")
print("Type 'help' to see available commands.\n")

# Chatbot Main Loop
while True:
    user_input = input("You: ")
    reply = chatbot_response(user_input)
    if reply is None:
        print("🤖 Chatbot: Goodbye! Have a beautiful celebration! 🎉")
        break
    print(f"🤖 Chatbot: {reply}\n")
