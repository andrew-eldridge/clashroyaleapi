from .cards import *
from .globaltournaments import *
from .locations import *
from .players import *
from .rankings import *
from .clans import *
from .format import *


def transform_tournament_header_list(x):
    tournament_header_list = TournamentHeaderListStruct()
    tournament_header_list.items = []
    for item in x['items']:
        tournament_header_list.items.append(transform_tournament_header(item))
    return tournament_header_list


def transform_tournament_header(x):
    tournament_header = TournamentHeaderStruct()
    tournament_header.status = x['status']
    tournament_header.preparation_duration = x['preparationDuration']
    tournament_header.created_time = x['createdTime']
    tournament_header.first_place_card_prize = x['firstPlaceCardPrize']
    tournament_header.game_mode = transform_game_mode(x['gameMode'])
    tournament_header.duration = x['duration']
    tournament_header.type = x['type']
    tournament_header.tag = x['tag']
    tournament_header.creator_tag = x['creatorTag']
    tournament_header.name = x['name']
    tournament_header.description = x['description']
    tournament_header.capacity = x['capacity']
    tournament_header.max_capacity = x['maxCapacity']
    tournament_header.level_cap = x['levelCap']
    return tournament_header


def transform_tournament(x):
    tournament = TournamentStruct()
    tournament.members_list = transform_tournament_member_list(x['mebmersList'])
    tournament.status = x['status']
    tournament.preparation_duration = x['preparationDuration']
    tournament.created_time = x['createdTime']
    tournament.started_time = x['startedTime']
    tournament.ended_time = x['endedTime']
    tournament.first_place_card_prize = x['firstPlaceCardPrize']
    tournament.game_mode = transform_game_mode(x['gameMode'])
    tournament.duration = x['duration']
    tournament.type = x['type']
    tournament.tag = x['tag']
    tournament.creator_tag = x['creatorTag']
    tournament.name = x['name']
    tournament.description = x['description']
    tournament.capacity = x['capacity']
    tournament.max_capacity = x['maxCapacity']
    tournament.level_cap = x['levelCap']
    return tournament


def transform_tournament_member_list(x):
    tournament_member_list = TournamentMemberListStruct()
    tournament_member_list.items = []
    for item in x['items']:
        tournament_member_list.items.append(transform_tournament_member(item))
    return tournament_member_list


def transform_tournament_member(x):
    tournament_member = TournamentMemberStruct()
    tournament_member.clan = transform_player_clan(x['clan'])
    tournament_member.rank = x['rank']
    tournament_member.previous_rank = x['previousRank']
    tournament_member.tag = x['tag']
    tournament_member.name = x['name']
    tournament_member.score = x['score']
    return tournament_member


def transform_ladder_tournament_ranking_list(x):
    ladder_tournament_ranking_list = LadderTournamentRankingListStruct()
    ladder_tournament_ranking_list.items = []
    for item in x['items']:
        ladder_tournament_ranking_list.items.append(transform_ladder_tournament_ranking(item))
    return ladder_tournament_ranking_list


def transform_ladder_tournament_ranking(x):
    ladder_tournament_ranking = LadderTournamentRanking()
    ladder_tournament_ranking.clan = transform_player_ranking_clan(x['clan'])
    ladder_tournament_ranking.wins = x['wins']
    ladder_tournament_ranking.losses = x['losses']
    ladder_tournament_ranking.tag = x['tag']
    ladder_tournament_ranking.name = x['name']
    ladder_tournament_ranking.rank = x['rank']
    ladder_tournament_ranking.previous_rank = x['previousRank']
    return ladder_tournament_ranking

