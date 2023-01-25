import interactions

bot = interactions.Client(token="MTA2NTY1ODMxNzQ4NzIxMDQ5Ng.G73OY0.8iahaQ0iU1Z-UeT-3i5hAFno_kZFcGoZ3yZtoE")

@bot.command(
    name="my_first_command",
    description="This is the first command I made!",
)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")

bot.start()