from discord.ext import commands
from lavis import lavis

class updatetest1(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name=".uu")
    async def upload(self, ctx):
        await lavis(ctx, title="aloda", description="Update1 loaded")

async def setup(bot):
    await bot.add_cog(updatetest1(bot))