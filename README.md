# 🤖 DISGPT: The AI-Powered Discord Bot  

DISGPT is a powerful and fun Discord bot that brings the magic of OpenAI's GPT-3.5-Turbo to your server! Whether you need quick answers, assistance with brainstorming, or just someone to chat with, DISGPT has got your back. 🎉  

---

## ✨ Features  

- 🔥 **AI-Powered Chat** – Get instant and intelligent responses with OpenAI's GPT-3.5-Turbo.  
- 💬 **Real-Time Interaction** – DISGPT responds to mentions, so just tag it and chat away!  
- 🧠 **Engaging Conversations** – It learns from the ongoing chat to make replies context-aware.  
- 🛡️ **Error Handling** – Graceful handling of API rate limits and errors, so your bot doesn’t break under pressure.  

---

## 🚀 Getting Started

Follow these steps to set up DISGPT on your server:  

### 1️⃣ Prerequisites
- 🐍 **Python 3.8+**  
- 🤖 **A Discord Bot Token** (Get it from the [Discord Developer Portal](https://discord.com/developers/applications))  
- 🔑 **An OpenAI API Key** ([Sign up here](https://platform.openai.com/signup/))  

---

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/Shashank-Mishra-1/DISGPT.git
cd DISGPT
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables  
Create a `.env` file and add your API keys:
```env
OPENAI_API_KEY=your_openai_api_key
SECRET_KEY=your_discord_bot_token
```

### 5️⃣ Run the Bot
```bash
python main.py
```  

---

## 🎉 How to Use

1️⃣ **Add the bot to your server** using its invite link.  
2️⃣ **Mention DISGPT in any channel** to get a reply! Example:  
   ```@DISGPT, what's the weather like?```  
3️⃣ **Watch it respond with intelligence, wit, and charm!** 🤩  

---

## 🛠️ Customization

Want to tweak the bot’s behavior? Modify the `messages` parameter in `bot.py`:  
```python
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": chat_history}
]
```
Change the `system` message to customize the bot’s personality. Make it a sarcastic friend, a professional assistant, or even a pirate! 🏴‍☠️  

---

## 🐛 Troubleshooting

🐞 **Bot not responding?** Double-check your bot token and API key in `.env`.  
⏳ **Rate Limit Errors?** OpenAI's API has usage limits. Consider upgrading your plan if needed.  
🤔 **Need help?** Open an issue on GitHub or DM me on Discord!  

---

## 🤝 Contributing

Got ideas or improvements? Contributions are welcome! Just fork the repo, make your changes, and submit a pull request. Let’s make DISGPT even better together! 🌟  

---

## 📜 License

📜 This project is licensed under the MIT License. See `LICENSE` for details.  

---

