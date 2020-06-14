from .cards import *
from .globaltournaments import *
from .locations import *
from .players import *
from .clans import *
from .tournaments import *
from .format import *


def transform_clan_ranking_list(x):
    clan_ranking_list = ClanRankingListStruct()
    clan_ranking_list.items = []
    for item in x['items']:
        clan_ranking_list.items.append(transform_clan_ranking(item))
    return clan_ranking_list


def transform_clan_ranking(x):
    clan_ranking = ClanRankingStruct()
    clan_ranking.clan_score = x['clanScore']
    clan_ranking.badge_id = x['badgeId']
    clan_ranking.location = transform_location(x['location'])
    clan_ranking.members = x['members']
    clan_ranking.tag = x['tag']
    clan_ranking.name = x['name']
    clan_ranking.rank = x['rank']
    clan_ranking.previous_rank = x['previousRank']
    clan_ranking.badge_urls = x['badgeUrls']
    return clan_ranking


def transform_player_ranking_list(x):
    player_ranking_list = PlayerRankingListStruct()
    player_ranking_list.items = []
    for item in x['items']:
        player_ranking_list.items.append(transform_player_ranking(item))
    return player_ranking_list


def transform_player_ranking(x):
    player_ranking = PlayerRankingStruct()
    player_ranking.clan = transform_player_ranking_clan(x['clan'])
    player_ranking.arena = transform_arena(x['arena'])
    player_ranking.tag = x['tag']
    player_ranking.name= x['name']
    player_ranking.exp_level = x['expLevel']
    player_ranking.rank = x['rank']
    player_ranking.previous_rank = x['previousRank']
    player_ranking.trophies = x['trophies']
    return player_ranking


def transform_player_ranking_clan(x):
    player_ranking_clan = PlayerRankingClanStruct()
    player_ranking_clan.badge_id = x['badgeId']
    player_ranking_clan.tag = x['tag']
    player_ranking_clan.name = x['name']
    player_ranking_clan.badge_urls = x['badgeUrls']
    return player_ranking_clan

