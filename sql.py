import enum

async def get_user(pool, uid):
    """Return user data from rotmg.users table"""
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * from rotmg.users WHERE id = {}".format(uid))
            data = await cursor.fetchone()
            await conn.commit()
            return data

async def get_num_verified(pool):
    """Count number of verified raiders"""
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT COUNT(*) FROM rotmg.users where status = 'verified'")
            data = await cursor.fetchone()
            await conn.commit()
            return data

async def get_guild(pool, uid):
    """Return guild data from rotmg.guilds"""
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * from rotmg.guilds WHERE id = {}".format(uid))
            data = await cursor.fetchone()
            await conn.commit()
            return data

async def ign_exists(pool, ign, id):
    """Check if an IGN has been entered into the user table already"""
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * from rotmg.users WHERE ign = '{}' AND status = 'verified'".format(ign))
            user = await cursor.fetchone()
            await conn.commit()
            if not user or user[0] == id:
                return False
            return True

# async def user_exists(uid):
#     if await get_user(uid) is None:
#         return False
#     return True


async def add_new_user(pool, user_id, guild_id, verify_id):
    """Create record of user data in rotmg.users"""
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            sql = "INSERT INTO rotmg.users (id, status, verifyguild, verifyid) VALUES (%s, 'stp_1', %s, %s)"
            data = (user_id, guild_id, verify_id)
            await cursor.execute(sql, data)
            await conn.commit()


async def update_user(pool, id, column, change):
    """Update user data entry in rotmg.users"""
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            sql = "UPDATE rotmg.users SET {} = %s WHERE id = {}".format(column, id)
            await cursor.execute(sql, (change,))
            await conn.commit()


async def add_new_guild(pool, guild_id, guild_name):
    """Add new guild to rotmg.guilds"""
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            sql = ("INSERT INTO rotmg.guilds (id, name, verificationid, nmaxed, nfame,"
                   "nstars, reqall, privateloc, reqsmsg, manualverifychannel, verifiedroleid,"
                   "verifylogchannel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            data = (guild_id, guild_name, 0, 0, 0, 0, False, True, "", 0, 0, 0)
            await cursor.execute(sql, data)
            await conn.commit()


async def update_guild(pool, id, column, change):
    """Update guild data in rotmg.guilds"""
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            sql = "UPDATE rotmg.guilds SET {} = %s WHERE id = {}".format(column, id)
            await cursor.execute(sql, (change,))
            await conn.commit()
            

class casino_cols(enum.IntEnum):
    id = 0
    balance = 1
    dailycooldown = 2
    workcooldown = 3
    searchcooldown = 4
    

class usr_cols(enum.IntEnum):
    """Contains References to rotmg.users table for easy access"""
    id = 0  # Int
    ign = 1  # String
    status = 2  # String
    verifyguild = 3  # Int
    verifykey = 4  # String
    verifyid = 5  # Int
    verifiedguilds = 6  # String (CSV)


class gld_cols(enum.IntEnum):
    """Contains References to rotmg.guilds table for easy access"""
    id = 0  # Int
    name = 1  # String
    verificationid = 2  # Int
    nmaxed = 3  # Int
    nfame = 4  # Int
    nstars = 5  # Int
    reqall = 6  # Boolean
    privateloc = 7  # Boolean
    reqsmsg = 8  # String (formatted)
    manualverifychannel = 9  # Int
    verifiedroleid = 10  # Int
    verifylogchannel = 11  # Int
    supportchannelname = 12  # String
    raidhc1 = 13  # Int
    raidvc1 = 14  # Int
    raidhc2 = 15
    raidhc3 = 16
    raidvc2 = 17
    raidvc3 = 18
    rlroleid = 19
    vethcid = 20
    vetvcid = 21
    vetroleid = 22
    vetrlroleid = 23
    creationmonths = 24
    subverify1id = 25
    subverify1name = 26
    subverify1roleid = 27
    subverifylogchannel = 28
    subverify2id = 29
    subverify2name = 30
    subverify2roleid = 31
    mmroleid = 32
