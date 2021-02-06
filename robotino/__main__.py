import os

import praw
import discord

from discord.ext import commands

REDDIT_ID = os.getenv("REDDIT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

REDDIT = praw.Reddit(client_id=REDDIT_ID,
                     client_secret=REDDIT_SECRET,
                     user_agent="bot v0.1.0 by /u/borax")

bot = commands.Bot(command_prefix='!')

print("Reddit Read-Only connected", REDDIT.read_only)


@bot.command(
    name="reddit",
    description="A simple reddit parser",
    pass_context=True
)
async def reddit_function(ctx, *args):
    options = list(filter(lambda x: x.startswith("--"), args))
    values = list(filter(lambda x: not x.startswith("--"), args))
    if len(values) == 2:
        sub, nb = values
    else:
        sub = values[0]
        nb = 5
    nb = int(nb) if nb < 20 else 20
    submitted = 0
    for e, i in enumerate(REDDIT.subreddit(sub).random_rising()):
        try:
            if submitted == nb:
                break
            embed = discord.Embed(
                author=e.author.name,
                title=e.title[0:256],
                url=e.shortlink,
            )
            if any([e.url.find(ext) >= 0 for ext in (".png", ".jpg", ".gif")]):
                embed.set_image(url=e.url)
            elif "--images" in options:
                continue
            await ctx.message.channel.send(embed=embed)
            submitted += 1
        except Exception as e:
            print("Error: ", e)


@bot.event
async def on_ready():
    print(
        'Bot is connected:\n'
    )


bot.run(DISCORD_TOKEN)
