import interactions

guild_id = 622450248362754050
client_secret = "F2oAt-VY-t8Ge8-fMFSeG6gVHCWDkKmw"

bot = interactions.Client(
    token=client_secret,
    default_scope=guild_id
)

@bot.command(
    name="get_user_connection",
    description="It will return 3rd party app connected to the users",
)
async def my_first_command(ctx: interactions.CommandContext , text:str):
    await ctx.send(f"The user {ctx.user.username} says {text}")

bot.start()