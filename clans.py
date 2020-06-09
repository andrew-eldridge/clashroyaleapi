# Royale API Transformer
# Written by Andrew Eldridge
# 6/7/2020
# clans.py: parses res data from /v1/clan api reqs into usable structures

import json
from format import *
from collections import namedtuple

# obj = json.loads(data, object_hook=lambda d: namedtuple("X", d.keys())(*d.values()))

# /v1/clans
def transform_clans(data):
    decoded = json.loads(data)
    clan_list = ClanListStruct()
    for c in decoded["items"]:
        clan = ClanStruct()
        clan.member_list = ClanMemberListStruct()
        clan.badge_id = c["badgeId"]
        clan.tag = c["tag"]
        clan.donations_per_week = c["donationsPerWeek"]
        clan.clan_chest_status = c["clanChestStatus"]
        clan.clan_chest_level = c["clanChestLevel"]
        clan.clan_chest_max_level = c["clanChestMaxLevel"]
        clan.clan_war_trophies = c["clanWarTrophies"]
        clan.required_trophies = c["requiredTrophies"]
        clan.clan_score = c["clanScore"]
        clan.name = c["name"]
        clan.location = LocationStruct()
        clan.type = c["type"]
        clan.members = c["members"]
        clan.description = c["description"]
        clan.clan_chest_points = c["clanChestPoints"]
        clan.badge_urls = c["badgeUrls"]

        clan.member_list.items = []
        for m in c["memberList"]:
            member = ClanMemberStruct()
            member.arena = ArenaStruct()
            member.clan_chest_points = m["clanChestPoints"]
            member.last_seen = m["lastSeen"]
            member.tag = m["tag"]
            member.name = m["name"]
            member.role = m["role"]
            member.exp_level = m["expLevel"]
            member.trophies = m["trophies"]
            member.clan_rank = m["clanRank"]
            member.previous_clan_rank = m["previousClanRank"]
            member.donations = m["donations"]
            member.donations_received = m["donationsReceived"]
            clan.member_list.items.append(member)


# /v1/clans/{clanTag}/warlog
"""
def transform_war_log(data):
    # Convert war log data to internal structure
    war_log = WarLogStruct()
    for war in data["items"]:
        # Construct war objects, append to war log
        curr_war = WarStruct()
        curr_war.seasonId = war["seasonId"]
        curr_war.createdDate = war["createdDate"]

        # Construct participant objects, append to war's participants list
        for participant in war["participants"]:
            curr_participant = ParticipantStruct()
            curr_participant.tag = participant["tag"]
            curr_participant.name = participant["name"]
            curr_participant.cardsEarned = participant["cardsEarned"]
            curr_participant.battlesPlayed = participant["battlesPlayed"]
            curr_participant.wins = participant["wins"]
            curr_participant.collectionDayBattlesPlayed = participant["collectionDayBattlesPlayed"]
            curr_participant.numberOfBattles = participant["numberOfBattles"]
            curr_war.participants.append(curr_participant)

        # Construct standing objects, append to war's standings list
        for standing in war["standings"]:
            curr_standing = StandingStruct()
            curr_clan = ClanStruct()
            clan = standing["clan"]
            # Child attributes
            curr_clan.tag = clan["tag"]
            curr_clan.name = clan["name"]
            curr_clan.badgeId = clan["badgeId"]
            curr_clan.clanScore = clan["clanScore"]
            curr_clan.participants = clan["participants"]
            curr_clan.battlesPlayed = clan["battlesPlayed"]
            curr_clan.wins = clan["wins"]
            curr_clan.crowns = clan["crowns"]
            # Parent attributes
            curr_standing.clan = curr_clan
            curr_standing.trophyChange = standing["trophyChange"]
            curr_war.standings.append(curr_standing)

        # Append current war item to log
        war_log.items.append(curr_war)

    # Return reformatted war log
    return war_log
"""