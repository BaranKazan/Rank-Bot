from config import *
import interactions
from discord_oauth2_api import get_user_data

bot = interactions.Client(
    token=TOKEN,
    default_scope=GUILD_ID
)
@bot.command(
    name="get_user_connection",
    description="It will return 3rd party app connected to the users",
)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send(f"The user {ctx.user.email}")

bot.start()