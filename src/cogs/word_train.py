from discord.ext import commands
from constants import ERROR_STRINGS, ErrorCode, WORDTRAIN_STRINGS
from models.GamePlay import GamePlay


class WordTrain(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_games = {}  # Tracks game state per channel

    @commands.command()
    async def starttrain(self, ctx):
        self.channel_games[ctx.channel.id] = GamePlay()
        await ctx.send(WORDTRAIN_STRINGS["start"])

    @commands.command()
    async def stoptrain(self, ctx):
        if ctx.channel.id in self.channel_games:
            del self.channel_games[ctx.channel.id]
            await ctx.send(WORDTRAIN_STRINGS["stop"])
        else:
            await ctx.send(WORDTRAIN_STRINGS["no_train"])

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content.strip().startswith("/"):
            return
        if len(message.content.split()) != 2:
            return
        
        game = self.channel_games.get(message.channel.id)
        if not game:
            return  # No active game

        words = message.content.strip().lower()
        if game.is_game_end(words.split()[-1]):
            await message.channel.send(WORDTRAIN_STRINGS["game_end"].format(words.split()[-1]))
            game.reset()
            return
        
        add_word_result = game.add_word(words, message.author.name)
        if add_word_result is True:
            await message.add_reaction("✅")
            return
        elif add_word_result is ErrorCode.USED_WORD:
            await message.add_reaction("❌")
            await message.channel.send(ERROR_STRINGS[ErrorCode.USED_WORD])
        elif add_word_result is ErrorCode.INVALID_WORD:
            await message.add_reaction("❌")
            await message.channel.send(ERROR_STRINGS[ErrorCode.INVALID_WORD].format(game.last_word))
        elif add_word_result is ErrorCode.NON_EXISTENT_WORD:
            await message.add_reaction("❌")
            await message.channel.send(ERROR_STRINGS[ErrorCode.NON_EXISTENT_WORD].format(words))
        elif add_word_result is ErrorCode.LAST_USER:
            await message.add_reaction("❌")
            await message.channel.send(ERROR_STRINGS[ErrorCode.LAST_USER].format(game.last_user))
        else:
            await message.channel.send(WORDTRAIN_STRINGS["unknown_error"])

        # Required to keep bot commands working
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(WordTrain(bot))