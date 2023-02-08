import interactions

bot = interactions.Client(
    token="MTA2NTY1ODMxNzQ4NzIxMDQ5Ng.GYi6X4.i4UDls7mgQwPgCbYXyqtsofFClrMr3-Or9u9zw",
    default_scope=622450248362754050
)

@bot.command(
    name="my_first_command",
    description="This is the first command I made!",
    options = [
        interactions.Option(
            name="text",
            description="What you want to say",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def my_first_command(ctx: interactions.CommandContext , text:str):
    #await test(ctx)
    await ctx.send(f"The user {ctx.user.username} says {text}")

"""
@bot.command(
    type=interactions.ApplicationCommandType.USER,
    name="User Command",
)
async def test(ctx):
    await ctx.send(f"You have applied a command onto user {ctx.target.user.username}!")
"""

bot.start()