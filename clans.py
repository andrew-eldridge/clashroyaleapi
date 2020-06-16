from .cards import *
from .rankings import *
from .format import *


def transform_clan_list(x):
    clan_list = ClanListStruct()
    clan_list.items = []
    for clan in x['items']:
        clan_list.items.append(transform_clan(clan))
    return clan_list


def transform_clan(x):
    clan = ClanStruct()
    clan.member_list = transform_clan_member_list(x['memberList'])
    clan.badge_id = x['badgeId']
    clan.tag = x['tag']
    clan.donations_per_week = x['donationsPerWeek']
    clan.clan_chest_status = x['clanChestStatus']
    clan.clan_chest_level = x['clanChestLevel']
    clan.clan_chest_max_level = x['clanChestMaxLevel']
    clan.clan_war_trophies = x['clanWarTrophies']
    clan.required_trophies = x['requiredTrophies']
    clan.clan_score = x['clanScore']
    clan.name = x['name']
    clan.location = transform_location(x['location'])
    clan.type = x['type']
    clan.members = x['members']
    clan.description = x['description']
    clan.clan_chest_points = x['clanChestPoints']
    clan.badge_urls = x['badgeUrls']
    return clan


def transform_clan_member_list(x):
    clan_member_list = ClanMemberListStruct()
    clan_member_list.items = []
    for member in x:
        clan_member_list.items.append(transform_clan_member(member))
    return clan_member_list


def transform_clan_member(x):
    member = ClanMemberStruct()
    member.arena = transform_arena(x['arena'])
    member.clan_chest_points = x['clanChestPoints']
    member.last_seen = x['lastSeen']
    member.tag = x['tag']
    member.name = x['name']
    member.role = x['role']
    member.exp_level = x['expLevel']
    member.trophies = x['trophies']
    member.clan_rank = x['clanRank']
    member.previous_clan_rank = x['previousClanRank']
    member.donations = x['donations']
    member.donations_received = x['donationsReceived']
    return member


def transform_clan_war_log(x):
    clan_war_log = ClanWarLogStruct()
    clan_war_log.items = []
    for log_entry in x['items']:
        clan_war_log.items.append(transform_clan_war_log_entry(log_entry))
    return clan_war_log


def transform_clan_war_log_entry(x):
    clan_war_log_entry = ClanWarLogEntryStruct()
    clan_war_log_entry.standings = x['standings']
    clan_war_log_entry.season_id = x['seasonId']
    clan_war_log_entry.participants = transform_clan_war_participant_list(x['participants'])
    clan_war_log_entry.created_date = x['createdDate']
    return clan_war_log_entry


def transform_clan_war_standing_list(x):
    clan_war_standing_list = ClanWarStandingListStruct()
    clan_war_standing_list.items = []
    for standing in x:
        clan_war_standing_list.items.append(transform_clan_war_standing(standing))
    return clan_war_standing_list


def transform_clan_war_participant_list(x):
    clan_war_participant_list = ClanWarParticipantListStruct()
    clan_war_participant_list.items = []
    for participant in x:
        clan_war_participant_list.items.append(transform_clan_war_participant(participant))
    return clan_war_participant_list


def transform_clan_war_standing(x):
    clan_war_standing = ClanWarStandingStruct()
    clan_war_standing.trophy_change = x['trophyChange']
    clan_war_standing.clan = transform_clan_war_clan(x['clan'])
    return clan_war_standing


def transform_clan_war_participant(x):
    clan_war_participant = ClanWarParticipantStruct()
    clan_war_participant.tag = x['tag']
    clan_war_participant.name = x['name']
    clan_war_participant.cards_earned = x['cardsEarned']
    clan_war_participant.battles_played = x['battlesPlayed']
    clan_war_participant.wins = x['wins']
    clan_war_participant.collection_day_battles_played = x['collectionDayBattlesPlayed']
    clan_war_participant.number_of__battles = x['numberOfBattles']
    return clan_war_participant


def transform_clan_war_clan(x):
    clan_war_clan = ClanWarClanStruct()
    clan_war_clan.tag = x['tag']
    clan_war_clan.clan_score = x['clanScore']
    clan_war_clan.crowns = x['crowns']
    clan_war_clan.badge_id = x['badgeId']
    clan_war_clan.name = x['name']
    clan_war_clan.participants = x['participants']
    clan_war_clan.battles_played = x['battlesPlayed']
    clan_war_clan.wins = x['wins']
    return clan_war_clan


def transform_current_clan_war(x):
    current_clan_war = CurrentClanWarStruct()
    current_clan_war.state = x['state']
    current_clan_war.clan = transform_clan_war_clan(x['clan'])
    current_clan_war.participants = transform_clan_war_participant_list(x['participants'])
    current_clan_war.clans = transform_clan_war_clan_list(x['clans'])
    current_clan_war.collection_end_time = x['collectionEndTime']
    current_clan_war.war_end_time = x['warEndTime']
    return current_clan_war


def transform_clan_war_clan_list(x):
    clan_war_clan_list = ClanWarClanListStruct()
    clan_war_clan_list.items = []
    for clan in x:
        clan_war_clan_list.items.append(transform_clan_war_clan(clan))
    return clan_war_clan_list

