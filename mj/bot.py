#import random
#from datetime import datetime
import random
from datetime import datetime
from openai import OpenAI

client = OpenAI()


# =========================================================
#                    CHATBOT CLASS
# =========================================================

class MyChatBot:

    def __init__(self):
        self.user_name = None
        self.bot_name = "DjangoBot"
        self.conversation_count = 0

        self.jokes = [
            "Teacher: Homework kyu nahi kiya? Student: Sir, light nahi thi. Teacher: To candle jala lete. Student: Sir, matchbox nahi thi 😂",
            "Computer ko thand kyu lagti hai? Kyunki uske Windows khule rehte hain 😂",
            "Programmer ki favourite place? The coffee shop ☕😂",
            "Bug bola: Mujhe fix mat karo, main feature hoon 😂",
            "Ek programmer ne shaadi kyu nahi ki? Kyunki usko perfect match nahi mila 😆"
        ]

        self.facts = [
            "Python ko Guido van Rossum ne banaya tha.",
            "Django Python ka popular web framework hai.",
            "HTML website ka structure banata hai.",
            "CSS website ko design karta hai.",
            "JavaScript website me interaction add karta hai.",
            "MySQL ek popular relational database hai."
        ]

        self.friendly_replies = [
            "Bilkul bhai 😎",
            "Haan, batao kya hua?",
            "Main sun raha hoon 👂",
            "Achhaaa 😄 aur batao.",
            "Nice! Ye interesting hai.",
            "Haan bhai, bol.",
            "Samajh gaya 👍"
        ]


    # =====================================================
    #                    AI FUNCTION
    # =====================================================

    def ask_ai(self, message):
        response = client.responses.create(
            model="gpt-5.6-luna",
            input=message,
            max_output_tokens=300

        )

        return response.output_text


    # =====================================================
    #                    MAIN FUNCTION
    # =====================================================

    def get_response(self, message):

        self.conversation_count += 1

        message = message.strip()
        msg = message.lower()

        if not message:
            return "Kuch likho bhai 😄"


        # -------------------------------------------------
        # NAME
        # -------------------------------------------------

        if "my name is" in msg:
            name = message.lower().split("my name is", 1)[1].strip()

            if name:
                self.user_name = name.title()
                return f"Nice to meet you, {self.user_name}! 😄 Main tumhara naam yaad rakhunga."

        if msg.startswith("mera naam"):
            name = message[8:].strip()

            if name:
                self.user_name = name.title()
                return f"Okay {self.user_name} 😎 Ab mujhe tumhara naam yaad rahega."

        if "what is my name" in msg or "mera naam kya hai" in msg:

            if self.user_name:
                return f"Tumhara naam {self.user_name} hai 😎"

            return "Abhi tumne mujhe apna naam nahi bataya."


        # -------------------------------------------------
        # GREETINGS
        # -------------------------------------------------

        if msg in ["hi", "hello", "hey", "hii", "hlo", "namaste"]:

            if self.user_name:
                return f"Hello {self.user_name}! 👋 Kaise ho?"

            return random.choice([
                "Hello bhai 👋 Kaise ho?",
                "Hii 😄 Kya haal hai?",
                "Hey! 👋 Batao kya kar rahe ho?",
                "Namaste 🙏 Kaise help karun?"
            ])

        if "good morning" in msg:
            return "Good Morning 🌅 Bhai! Aaj ka din mast jaaye 😎"

        if "good afternoon" in msg:
            return "Good Afternoon ☀️ Bhai! Lunch hua?"

        if "good evening" in msg:
            return "Good Evening 🌆 Bhai! Kya chal raha hai?"

        if "good night" in msg:
            return "Good Night 🌙 Bhai! Achhe se sona 😴"


        # -------------------------------------------------
        # HOW ARE YOU
        # -------------------------------------------------

        if (
            "how are you" in msg
            or "kaise ho" in msg
            or "kesa hai" in msg
            or "kaisa hai" in msg
        ):
            return random.choice([
                "Main bilkul mast hoon 😎 Tum batao?",
                "Main badhiya hoon bhai! 🔥",
                "Ekdam fit 😄 Tum kaise ho?",
                "Main ready hoon tumse baat karne ke liye 🤖"
            ])


        # -------------------------------------------------
        # USER FEELING
        # -------------------------------------------------

        if "i am fine" in msg or "i'm fine" in msg or "mai thik hu" in msg:
            return "Ye sunkar achha laga 😄"

        if "i am sad" in msg or "mai sad hu" in msg or "main sad hu" in msg:
            return "To gaand mara nha"

        if "i am happy" in msg or "mai khush hu" in msg:
            return "Wah bhai! 😎🔥 Khush rehna sabse important hai."

        if "i am tired" in msg or "mai thak gaya" in msg:
            return "Thoda rest kar le bhai 😴 Paani bhi pee lena."


        # -------------------------------------------------
        # TIME
        # -------------------------------------------------

        if "time" in msg or "kitne baje" in msg:

            current_time = datetime.now().strftime("%I:%M %p")

            return f"Abhi time hai {current_time} ⏰"


        # -------------------------------------------------
        # DATE
        # -------------------------------------------------

        if "date" in msg or "aaj ki date" in msg:

            current_date = datetime.now().strftime("%d %B %Y")

            return f"Aaj ki date hai {current_date} 📅"


        # -------------------------------------------------
        # DAY
        # -------------------------------------------------

        if "which day" in msg or "kaunsa din" in msg or "aaj kya hai" in msg:

            today = datetime.now().strftime("%A")

            return f"Aaj {today} hai 📅"


        # -------------------------------------------------
        # BOT NAME
        # -------------------------------------------------

        if (
            "your name" in msg
            or "tumhara naam" in msg
            or "bot ka naam" in msg
        ):
            return f"Mera naam {self.bot_name} hai 🤖"


        # -------------------------------------------------
        # WHO ARE YOU
        # -------------------------------------------------

        if (
            "who are you" in msg
            or "tum kon ho" in msg
            or "tum kaun ho" in msg
        ):
            return (
                "Main DjangoBot hoon 🤖\n"
                "Mujhe Python se banaya gaya hai.\n"
                "Main normal conversation kar sakta hoon, "
                "naam yaad rakh sakta hoon aur basic questions ke answers de sakta hoon."
            )


        # -------------------------------------------------
        # CREATOR
        # -------------------------------------------------

        if (
            "who made you" in msg
            or "tumhe kisne banaya" in msg
            or "kisne banaya" in msg
        ):
            return "Mujhe Python aur Django project ke liye banaya gaya hai 😎"


        # -------------------------------------------------
        # PYTHON
        # -------------------------------------------------

        if "what is python" in msg or "python kya hai" in msg:

            return (
                "Python ek high-level programming language hai 🐍.\n"
                "Iska use web development, automation, AI, "
                "data science, games aur bahut saare kaam me hota hai."
            )


        # -------------------------------------------------
        # DJANGO
        # -------------------------------------------------

        if "what is django" in msg or "django kya hai" in msg:

            return (
                "Django Python ka web framework hai 🚀.\n"
                "Isse hum websites aur web applications bana sakte hain."
            )


        # -------------------------------------------------
        # HTML
        # -------------------------------------------------

        if "what is html" in msg or "html kya hai" in msg:

            return (
                "HTML ka full form HyperText Markup Language hai.\n"
                "Website ka basic structure HTML se banta hai 🌐."
            )


        # -------------------------------------------------
        # CSS
        # -------------------------------------------------

        if "what is css" in msg or "css kya hai" in msg:

            return (
                "CSS ka full form Cascading Style Sheets hai 🎨.\n"
                "CSS se website ka design, color, spacing, "
                "font aur layout control karte hain."
            )


        # -------------------------------------------------
        # MYSQL
        # -------------------------------------------------

        if "what is mysql" in msg or "mysql kya hai" in msg:

            return (
                "MySQL ek relational database management system hai 🗄️.\n"
                "Isme hum data ko tables ke form me store aur manage kar sakte hain."
            )


        # -------------------------------------------------
        # PROGRAMMING
        # -------------------------------------------------

        if "programming kya hai" in msg or "what is programming" in msg:

            return (
                "Programming ka matlab computer ko instructions dena hota hai 💻.\n"
                "Python, Java, C++, JavaScript etc. programming languages hain."
            )


        # -------------------------------------------------
        # JOKE
        # -------------------------------------------------

        if (
            "joke" in msg
            or "jokes" in msg
            or "joke sunao" in msg
            or "mazak" in msg
        ):
            return random.choice(self.jokes)


        # -------------------------------------------------
        # FACT
        # -------------------------------------------------

        if "fact" in msg or "interesting fact" in msg:

            return random.choice(self.facts)


        # -------------------------------------------------
        # HELP
        # -------------------------------------------------

        if msg == "help" or "what can you do" in msg:

            return (
                "Main ye kaam kar sakta hoon 🤖:\n\n"
                "• Normal conversation\n"
                "• Tumhara naam yaad rakhna\n"
                "• Time batana\n"
                "• Date batana\n"
                "• Day batana\n"
                "• Python ke basic questions\n"
                "• Django ke basic questions\n"
                "• HTML/CSS ke basic questions\n"
                "• MySQL ke basic questions\n"
                "• Jokes sunana\n"
                "• Random facts batana\n"
                "• Friendly conversation\n"
                "• AI se questions ka answer dena"
            )


        # -------------------------------------------------
        # THANK YOU
        # -------------------------------------------------

        if (
            "thank you" in msg
            or "thanks" in msg
            or "thank" in msg
            or "shukriya" in msg
        ):
            return random.choice([
                "You're welcome bhai 😎",
                "Koi baat nahi ❤️",
                "Anytime bhai!",
                "Arey thanks ki kya baat hai 😄"
            ])


        # -------------------------------------------------
        # SORRY
        # -------------------------------------------------

        if "sorry" in msg or "maaf" in msg:
            return "Koi baat nahi bhai 😄 Sab chill hai."


        # -------------------------------------------------
        # LOVE / FRIEND
        # -------------------------------------------------

        if "i love you" in msg or "love you" in msg:
            return "Aww 😄 Main bhi tumhara friendly chatbot hoon ❤️"

        if "are you my friend" in msg or "tum mere dost ho" in msg:
            return "Bilkul bhai 🤝 Main tumhara chatbot dost hoon."


        # -------------------------------------------------
        # BORED
        # -------------------------------------------------

        if "i am bored" in msg or "mai bore ho raha" in msg:

            return (
                "Bore ho rahe ho? 😄\n"
                "Joke sunu, Python sikhein, ya koi interesting fact bataun?"
            )


        # -------------------------------------------------
        # FOOD
        # -------------------------------------------------

        if "khana" in msg or "food" in msg or "kha liya" in msg:

            return random.choice([
                "Main digital hoon bhai, khana nahi kha sakta 😂",
                "Mera khana data aur Python hai 🤖😂",
                "Tumne khana kha liya? 🍕"
            ])


        # -------------------------------------------------
        # WEATHER BASIC
        # -------------------------------------------------

        if "weather" in msg or "mausam" in msg:

            return (
                "Main abhi internet weather service se connected nahi hoon 🌤️.\n"
                "Agar Django me weather API connect karoge to main "
                "live weather bhi dikha sakta hoon."
            )


        # -------------------------------------------------
        # AGE
        # -------------------------------------------------

        if "how old are you" in msg or "tumhari age" in msg:

            return "Meri age insaanon jaisi nahi hai 😄 Main ek Python chatbot hoon."


        # -------------------------------------------------
        # RANDOM FRIENDLY RESPONSE
        # -------------------------------------------------

        friendly_words = [
            "acha",
            "achha",
            "okay",
            "ok",
            "hmm",
            "haan",
            "yes",
            "nice",
            "cool"
        ]

        if msg in friendly_words:
            return random.choice(self.friendly_replies)


        # -------------------------------------------------
        # BYE
        # -------------------------------------------------

        if msg in [
            "bye",
            "goodbye",
            "see you",
            "see you later",
            "tata",
            "chal bye"
        ]:

            if self.user_name:
                return f"Bye {self.user_name}! 👋 Phir milte hain."

            return "Bye bhai 👋 Phir baat karenge."


        # -------------------------------------------------
        # EXIT
        # -------------------------------------------------

        if msg in ["exit", "quit", "close", "stop"]:

            return "Okay bhai 👋 Chatbot conversation end kar raha hoon."


        # -------------------------------------------------
        # DEFAULT RESPONSE + AI
        # -------------------------------------------------

        try:
            return self.ask_ai(message)

        except Exception:
            return random.choice([
                "Hmm 🤔 Iske baare me mujhe abhi pata nahi hai.",
                "Interesting question 😄 Lekin AI se answer lene me problem aa gayi.",
                "Abhi AI response nahi de pa raha 🤖.",
                "Thodi technical problem aa gayi bhai 😅.",
                "Dobara try karo bhai."
            ])


# =========================================================
#             CHATBOT OBJECT
# =========================================================

bot = MyChatBot()


# =========================================================
#        DJANGO KE LIYE SIMPLE FUNCTION
# =========================================================

def get_bot_response(message):
    return bot.get_response(message)