from format import *
from locations import *


def transform_clan_list(x):
    clan_list = ClanListStruct()
    clan_list.items = []
    for c in x["items"]:
        clan_list.items.append(transform_clan(c))
    return clan_list


def transform_clan(x):
    clan = ClanStruct()
    member_list = ClanMemberListStruct()
    clan.badge_id = x["badgeId"]
    clan.tag = x["tag"]
    clan.donations_per_week = x["donationsPerWeek"]
    clan.clan_chest_status = x["clanChestStatus"]
    clan.clan_chest_level = x["clanChestLevel"]
    clan.clan_chest_max_level = x["clanChestMaxLevel"]
    clan.clan_war_trophies = x["clanWarTrophies"]
    clan.required_trophies = x["requiredTrophies"]
    clan.clan_score = x["clanScore"]
    clan.name = x["name"]
    clan.location = transform_location(x["location"])
    clan.type = x["type"]
    clan.members = x["members"]
    clan.description = x["description"]
    clan.clan_chest_points = x["clanChestPoints"]
    clan.badge_urls = x["badgeUrls"]

    member_list.items = []
    for m in x["memberList"]:
        member_list.items.append(transform_clan_member(m))
    clan.member_list = member_list


def transform_clan_member_list(x):
    pass


def transform_clan_member(x):
    member = ClanMemberStruct()
    arena = ArenaStruct()
    member.clan_chest_points = x["clanChestPoints"]
    member.last_seen = x["lastSeen"]
    member.tag = x["tag"]
    member.name = x["name"]
    member.role = x["role"]
    member.exp_level = x["expLevel"]
    member.trophies = x["trophies"]
    member.clan_rank = x["clanRank"]
    member.previous_clan_rank = x["previousClanRank"]
    member.donations = x["donations"]
    member.donations_received = x["donationsReceived"]

    arena.name = x["arena"]["name"]
    arena.id = x["arena"]["id"]
    arena.icon_urls = x["arena"]["iconUrls"]
    member.arena = arena
    return member


def transform_clan_war_log(x):
    pass


def transform_clan_war_log_entry(x):
    pass


def transform_clan_war_standing_list(x):
    pass


def transform_clan_war_participant_list(x):
    pass


def transform_clan_war_standing(x):
    pass


def transform_clan_war_participant(x):
    pass


def transform_clan_war_clan(x):
    pass


def transform_current_clan_war(x):
    pass


def transform_clan_war_clan_list(x):
    pass


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