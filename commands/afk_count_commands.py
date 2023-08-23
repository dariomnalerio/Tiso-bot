"""
Module for afk_count commands.
"""
import discord
from api.afk_count import get_afk_count, add_to_afk_count
from database.database import get_session, create_tables


def afkCount(bot):
    @bot.command(name="afk-add")
    async def afk_add(ctx, member: discord.Member = None):
        """
        Add one to the AFK count of a member

        Example:
            $afk-add @member
        """

        if member is None:
            await ctx.send("Must mention user")
            return

        session = get_session()
        server_id = str(ctx.message.guild.id)
        afk_count = add_to_afk_count(session, str(member.id), server_id)

        if afk_count is None:
            await ctx.send("Error adding to AFK count")
        else:
            times_text = "time" if afk_count == 1 else "times"
            await ctx.send(f"{member.display_name} has gone afk {afk_count} {times_text}")

    @bot.command(name="afk-get")
    async def afk_get(ctx, member: discord.Member = None):
        """
        Get the AFK count of a member

        Example:
            $afk-get @member
        """

        if member is None:
            await ctx.send("Must mention user")
            return

        session = get_session()
        server_id = str(ctx.message.guild.id)
        afk_count = get_afk_count(session, str(member.id), server_id)

        if afk_count is None:
            await ctx.send("Error getting AFK count")
        if afk_count == 0:
            await ctx.send(f"{member.display_name} has not gone afk yet")
        else:
            times_text = "time" if afk_count == 1 else "times"
            await ctx.send(f"{member.display_name} has gone afk {afk_count} {times_text}")
