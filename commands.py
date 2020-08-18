import discord

class AddReaction:
    def __init__(self, message):
        self.message = message
        self.content = message.content[5:]

    async def run(self): ## maybe can reformat error raises in try/except if can obtain right error raises
        if self.message.guild is not None:
            args = self.content.split(" ")
            if (len(args) < 1):
                #DM User Error for Incorrect /add Command
                print("1")
                return
            emoji_str = self.content[0]

            # Check Message ID is Valid
            try:
                if (len(args) > 1):
                    msg_id = int(args[1])
                    message = await self.message.channel.fetch_message(msg_id)
                else:
                    message = await self.message.channel.history(limit=2).flatten()
                    message = message[1]
            except:
                #DM User Error for Incorrect /add Command
                # Invalid Message ID
                print("2")
                return

            # Add Reaction
            if (len(message.reactions) >= 20):
                #Discord MAX Reactions Limit of 20 Reached
                # Send Message @author ^ in Channel
                # Delete Message After 5 Seconds
                print("3")
                return
            try:
                await message.add_reaction(emoji_str)
            except:
                #DM User Error for Incorrect /add Command
                # Invalid Emoji ID or
                # Not Perms to Add Reacts
                print("4")
                return

            # Delete Emoji Command ## maybe make a separate function for this?
            try:
                await self.message.delete()
            except:
                print("5")
                pass

            # log_command