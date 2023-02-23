import os

import interactions

guild_id = os.getenv("GUILD_ID")
client_secret = os.getenv("CLIENT_SECRET")

bot = interactions.Client(
    token=client_secret,
    default_scope=guild_id
)

@bot.command(
    name="get_user_connection",
    description="It will return 3rd party app connected to the users",
)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send(f"The user {ctx.user.username}")

bot.start()