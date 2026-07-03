import os
from dotenv import load_dotenv
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# 1. Initialize environment settings before importing Cognee
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Force-inject correct Google API configurations
os.environ["LLM_PROVIDER"] = "gemini"
os.environ["LLM_MODEL"] = "gemini/gemini-2.5-flash"
os.environ["LLM_API_KEY"] = os.getenv("LLM_API_KEY", "")

os.environ["EMBEDDING_PROVIDER"] = "gemini"
os.environ["EMBEDDING_MODEL"] = "gemini/gemini-embedding-001"
os.environ["EMBEDDING_DIMENSIONS"] = "768"
os.environ["EMBEDDING_API_KEY"] = os.getenv("EMBEDDING_API_KEY", "")
os.environ["COGNEE_SKIP_CONNECTION_TEST"] = "true"

# 2. Invisible Web Server to keep the bot alive 24/7 on free cloud hosting
class HealthCheckServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"ContextClip Gateway Online 24/7")
    def log_message(self, format, *args):
        return  # Keep terminal logs clean

def run_health_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), HealthCheckServer)
    print(f"📡 Stealth Web Server Listening on port {port}")
    server.serve_forever()

# Safely import remaining dependencies
import discord
from discord.ext import commands
import cognee
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("=========================================")
    print(f"🔥 ContextClip Gateway Active!")
    print(f"Logged in safely as: {bot.user}")
    print("=========================================")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)
    if message.content.startswith("!"):
        return

    # ROUTE A: Querying System Memory
    if message.content.startswith("?"):
        query_string = message.content[1:].strip()
        if not query_string:
            await message.reply("⚠️ Please provide a clear question or query after the '?' symbol.")
            return

        status_msg = await message.reply("🔍 Traversing AI Knowledge Graph index vectors...")
        try:
            results = await cognee.recall(query_string)
            if not results:
                await status_msg.edit(content="❌ No matching clipboard context located in memory graph.")
                return

            response_text = "**Found Vector & Graph Matches:**\n"
            for node in results:
                # Extract only the clean human text property from the database object
                text_content = ""
                if hasattr(node, "text") and node.text:
                    text_content = node.text
                elif isinstance(node, dict) and "text" in node:
                    text_content = node["text"]
                elif hasattr(node, "raw") and isinstance(node.raw, dict) and "value" in node.raw:
                    text_content = node.raw["value"]
                else:
                    text_content = str(node)
                
                response_text += f"• {text_content}\n"

            if len(response_text) > 2000:
                response_text = response_text[:1990] + "..."
            await status_msg.edit(content=response_text)
        except Exception as error:
            await status_msg.edit(content=f"⚠️ System Error during memory traversal: {str(error)}")

    # ROUTE B: Storing New Clipboard Data
    else:
        clip_data = message.content.strip()
        if not clip_data:
            return

        status_msg = await message.reply("🧠 Mapping content context and anchoring to knowledge graph...")
        try:
            await cognee.remember(clip_data)
            await status_msg.edit(content="✅ Clip successfully conceptualized into your long-term memory graph!")
        except Exception as error:
            await status_msg.edit(content=f"⚠️ System Error during graph chunk ingestion: {str(error)}")

if __name__ == "__main__":
    if not DISCORD_TOKEN:
        print("❌ Runtime Aborted: DISCORD_TOKEN missing from environment structures.")
    else:
        # Start the background server thread before launching the Discord bot
        threading.Thread(target=run_health_server, daemon=True).start()
        bot.run(DISCORD_TOKEN)
