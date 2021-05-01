import command
import discord


def test_monster_id():
    results = command.monster("34")
    assert(isinstance(results, discord.Embed))


def test_monster_name():
    results = command.monster("Aptonoth")
    assert (isinstance(results, discord.Embed))


def test_monster_not_found():
    results = command.monster("zzz")
    assert (results == "No monsters matched your search.")