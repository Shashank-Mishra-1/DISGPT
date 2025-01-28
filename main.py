import discord
import os
import openai

# Initialize OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

chat_history = ""

token = os.getenv("SECRET_KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        global chat_history

        try:
            chat_history += f"{message.author}: {message.content}\n"
            print(f'Message from {message.author}: {message.content}')

            if self.user != message.author and self.user in message.mentions:
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": chat_history}
                        ],
                        temperature=1,
                        max_tokens=256,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )

                    message_to_send = response["choices"][0]["message"]["content"]
                    await message.channel.send(message_to_send)

                except openai.error.RateLimitError:
                    await message.channel.send("Sorry, I've exceeded my usage quota. Please try again later!")
                except Exception as api_error:
                    await message.channel.send("Sorry, there was an issue with my AI service. Please try again later!")
                    print(f"OpenAI API error: {api_error}")

        except Exception as e:
            print(f"Error: {e}")
            chat_history = ""

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
