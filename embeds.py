import discord


# Verification

def verification_check_msg(reqs):
    embed = discord.Embed(
        title='Verification Steps',
        description="__If you meet the requirements of this server, follow these steps to be verified:__\n1. Enable "
                    "DM's from server members\n2. Set **everything** on Realmeye to public except last known "
                    "location\n3. React to the ✅ below\n4. Follow all the directions the bot DM's you.",
        color=discord.Color.green()
    )
    embed.add_field(name="Server Requirements", value=f"```yaml\n{reqs}```")
    embed.add_field(name="Troubleshooting", value="If you're having trouble verifying, post in #support!",
                    inline=False)
    return embed


def verification_dm_start():
    embed = discord.Embed(
        title="Verification Status",
        color=discord.Color.teal()
    )
    embed.description = "__You are not yet verified. Follow the steps below to gain access to the " \
                        "server.__ "
    embed.add_field(name="\a", value="**Please provide your IGN** as it is spelled in-game.\nOnly "
                                     "send your IGN, ex: `Darkmattr`\n\nCapitalization does not "
                                     "matter.")
    embed.set_footer(text="React to the 'X' to cancel verification.")
    return embed


def verification_step_1(ign):
    embed = discord.Embed(
        title="Verification Status",
        description="Is `{}` the correct username?".format(ign),
        color=discord.Color.teal()
    )
    embed.add_field(name='https://www.realmeye.com/player/{}'.format(ign),
                    value="React with the check if so, if you entered the wrong username - click the x to cancel verification then dm the bot your correct username.")
    return embed


def verification_step_2(ign, key):
    embed = discord.Embed(
        title="You're almost done!",
        description="You have chosen `{}` to be your IGN.".format(ign),
        color=discord.Color.teal()
    )
    embed.add_field(name="\a",
                    value="Please paste the code below into any line of your [realmeye]("
                          "https://www.realmeye.com/player/{}) description.\n```{}```\n\nOnce you are done, "
                          "un-react to the check emoji and re-react to finish!".format(
                        ign, key))
    return embed


def verification_success(guild_name, mention):
    embed = discord.Embed(
        title="Success!",
        description="{} is now a verified member of __{}__!".format(mention, guild_name),
        color=discord.Color.green()
    )
    return embed


def verification_already_verified():
    embed = discord.Embed(
        title="Verification Status",
        color=discord.Color.teal()
    )
    embed.description = "__You are already verified!__"
    embed.add_field(name="Troubleshooting",
                    value="If there are still missing channels, please contact a "
                          "moderator+!")
    return embed


def verification_already_verified_complete(verified_servers, ign):
    embed = discord.Embed(
        title="Verification Status",
        color=discord.Color.teal()
    )
    embed.description = "__You have been verified in another server__"
    if verified_servers is not None:
        embed.add_field(name="Verified Servers:", value='`{}`'.format(verified_servers))
    embed.add_field(name="\a",
                    value="React with a thumbs up if you would like to verify for this server with the IGN: `{}`.".format(
                        ign), inline=False)
    return embed


def verification_checking_realmeye():
    embed = discord.Embed(
        title="Retrieving data from Realmeye...",
        color=discord.Color.green()
    )
    return embed


def verification_manual_verify(ign, uid):
    embed = discord.Embed(
        title="Manual Verification",
        description=f"[{ign}](https://www.realmeye.com/player/{ign}) failed to meet the requirements and would like "
        f"to be manually verified.\nTo manually verify them use the following command below: \n```!manual_verify {uid}```"
    )
    return embed


# Verification Errors

def verification_missing_code():
    embed = discord.Embed(
        title="Error!",
        description="You do not appear to have the code in your description.",
        color=discord.Color.red()
    )
    embed.add_field(name="\a",
                    value="If you have already placed the code in your description, wait a minute for the servers to "
                          "catch up and re-react to the check above.")
    return embed


def verification_public_location():
    embed = discord.Embed(
        title="Error!",
        description="Your location has not been set to private.",
        color=discord.Color.red()
    )
    embed.add_field(name="\a",
                    value="Once you've set your location to private, wait a minute for the servers to catch up and "
                          "re-react to the check above.")
    return embed


def verification_bad_reqs(requirements):
    embed = discord.Embed(
        title="Error!",
        description="You do not meet the requirements for this server!",
        color=discord.Color.red()
    )
    embed.add_field(name='Requirements:',
                    value="```yaml\n{}```\nIf you would like to appeal the verification to a mod, re-react to the "
                          "check emoji.".format(
                        requirements))
    embed.set_footer(text="React to the 'X' to cancel verification.")
    return embed


def verification_bad_username():
    embed = discord.Embed(
        title="Error!",
        description="The username you provided is invalid. Please re-submit your username __as it is spelled in-game.__",
        color=discord.Color.red()
    )
    return embed


def verification_cancelled():
    embed = discord.Embed(
        title="Verification Cancelled.",
        description="You have cancelled the verification process.\nIf you would like to restart, re-react to the "
                    "verification message in the server.",
        color=discord.Color.red()
    )
    return embed


# Misc
def poll(title, options):
    numbers = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']
    embed=discord.Embed(
        title=f"🗳️ Poll: {title.capitalize()}",
        color=discord.Color.dark_red()
    )
    desc = ""
    for i, o in enumerate(options):
        desc += numbers[i] + ": " + options[i] + "\n"
    embed.description = desc
    return embed
