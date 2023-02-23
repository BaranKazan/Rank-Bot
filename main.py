import os

import interactions

guild_id = os.getenv("GUILD_ID")
token = os.getenv("TOKEN")

bot = interactions.Client(
    token=token,
    default_scope=guild_id
)

@bot.command(
    name="get_user_connection",
    description="It will return 3rd party app connected to the users",
)
async def my_first_command(ctx: interactions.CommandContext):
    user_json = get
    await ctx.send(f"The user {ctx.user.username}")

bot.start()