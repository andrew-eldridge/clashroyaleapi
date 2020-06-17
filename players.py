from .cards import *
from .globaltournaments import *
from .locations import *
from .clans import *
from .rankings import *
from .tournaments import *
from .format import *


def transform_arena(x):
    arena = ArenaStruct()
    arena.name = x['name']
    arena.id = x['id']
    try:
        x['iconUrls']
    except NameError:
        pass
    else:
        arena.icon_urls = x['iconUrls']
    return arena


def transform_player(x):
    player = PlayerStruct()
    player.clan = transform_player_clan(x['clan'])
    player.arena = transform_arena(x['arena'])
    player.role = x['role']
    player.wins = x['wins']
    player.losses = x['losses']
    player.total_donations = x['totalDonations']
    player.league_statistics = transform_player_league_statistics(x['leagueStatistics'])
    player.cards = transform_player_item_level_list(x['cards'])
    player.current_favourite_card = transform_item(x['currentFavouriteCard'])
    player.badges = transform_player_achievement_badge_list(x['badges'])
    player.tag = x['tag']
    player.name = x['name']
    player.exp_level = x['expLevel']
    player.trophies = x['trophies']
    player.best_trophies = x['bestTrophies']
    player.donations = x['donations']
    player.donations_received = x['donationsReceived']
    player.achievements = transform_player_achievement_progress_list(x['achievements'])
    player.battle_count = x['battleCount']
    player.three_crown_wins = x['threeCrownWins']
    player.challenge_cards_won = x['challengeCardsWon']
    player.challenge_max_wins = x['challengeMaxWins']
    player.tournament_cards_won = x['tournamentCardsWon']
    player.tournament_battle_count = x['tournamentBattleCount']
    player.current_deck = transform_player_item_level_list(x['currentDeck'])
    player.war_day_wins = x['warDayWins']
    player.clan_cards_collected = x['clanCardsCollected']
    player.star_points = x['starPoints']
    return player


def transform_player_clan(x):
    player_clan = PlayerClanStruct()
    player_clan.badge_id = x['badgeId']
    player_clan.tag = x['tag']
    player_clan.name = x['name']
    player_clan.badge_urls = x['badgeUrls']
    return player_clan


def transform_player_league_statistics(x):
    player_league_statistics = PlayerLeagueStatisticsStruct()
    player_league_statistics.previous_season = transform_league_season_result(x['previousSeason'])
    player_league_statistics.current_season = transform_league_season_result(x['currentSeason'])
    player_league_statistics.best_season = transform_league_season_result(x['bestSeason'])
    return player_league_statistics


def transform_player_item_level_list(x):
    player_item_level_list = PlayerItemLevelListStruct()
    player_item_level_list.items = []
    for item in x:
        player_item_level_list.items.append(transform_player_item_level(item))
    return player_item_level_list


def transform_player_achievement_badge_list(x):
    player_achievement_badge_list = PlayerAchievementBadgeListStruct()
    player_achievement_badge_list.items = []
    for item in x:
        player_achievement_badge_list.items.append(transform_player_achievement_badge(item))
    return player_achievement_badge_list


def transform_player_achievement_progress_list(x):
    player_achievement_progress_list = PlayerAchievementProgressListStruct()
    player_achievement_progress_list.items = []
    for item in x:
        player_achievement_progress_list.items.append(transform_player_achievement_progress(item))
    return player_achievement_progress_list


def transform_league_season_result(x):
    league_season_result = LeagueSeasonResultStruct()
    league_season_result.rank = x['rank']
    league_season_result.trophies = x['trophies']
    league_season_result.best_trophies = x['bestTrophies']
    league_season_result.id = x['id']
    return league_season_result


def transform_player_item_level(x):
    player_item_level = PlayerItemLevelStruct()
    player_item_level.id = x['id']
    player_item_level.count = x['count']
    player_item_level.level = x['level']
    player_item_level.star_level = x['starLevel']
    player_item_level.name = x['name']
    player_item_level.max_level = x['maxLevel']
    player_item_level.icon_urls = x['iconUrls']
    return player_item_level


def transform_player_achievement_badge(x):
    player_achievement_badge = PlayerAchievementBadgeStruct()
    player_achievement_badge.max_level = x['maxLevel']
    player_achievement_badge.progress = x['progress']
    player_achievement_badge.target = x['target']
    player_achievement_badge.level = x['level']
    player_achievement_badge.name = x['name']
    return player_achievement_badge


def transform_player_achievement_progress(x):
    player_achievement_progress = PlayerAchievementProgressStruct()
    player_achievement_progress.stars = x['stars']
    player_achievement_progress.value = x['value']
    player_achievement_progress.name = x['name']
    player_achievement_progress.target = x['target']
    player_achievement_progress.info = x['info']
    player_achievement_progress.completion_info = x['completionInfo']
    return player_achievement_progress


def transform_upcoming_chests(x):
    upcoming_chests = UpcomingChestsStruct()
    upcoming_chests.items = transform_chest_list(x['items'])
    return upcoming_chests


def transform_chest_list(x):
    chest_list = ChestListStruct()
    chest_list.items = []
    for item in x:
        chest_list.items.append(transform_chest(item))
    return chest_list


def transform_chest(x):
    chest = ChestStruct()
    chest.name = x['name']
    chest.index = x['index']
    chest.icon_urls = x['iconUrls']
    return chest


def transform_battle_list(x):
    battle_list = BattleListStruct()
    battle_list.items = []
    for item in x:
        battle_list.items.append(transform_battle(item))
    return battle_list


def transform_battle(x):
    battle = BattleStruct()
    battle.game_mode = transform_game_mode(x['gameMode'])
    battle.arena = transform_arena(x['arena'])
    battle.type = x['type']
    battle.deck_selection = x['deckSelection']
    battle.team = transform_player_battle_data_list(x['team'])
    battle.opponent = transform_player_battle_data_list(x['opponent'])
    battle.challenge_win_count_before = x['challengeWinCountBefore']
    battle.battle_time = x['battleTime']
    battle.challenge_id = x['challengeId']
    battle.tournament_tag = x['tournamentTag']
    battle.challenge_title = x['challengeTitle']
    battle.replay_tag = x['replayTag']
    battle.is_ladder_tournament = x['isLadderTournament']
    return battle


def transform_game_mode(x):
    game_mode = GameModeStruct()
    game_mode.id = x['id']
    game_mode.name = x['name']
    return game_mode


def transform_player_battle_data_list(x):
    player_battle_data_list = PlayerBattleDataListStruct()
    player_battle_data_list.items = []
    for item in x:
        player_battle_data_list.items.append(transform_player_battle_data(item))
    return player_battle_data_list


def transform_player_battle_data(x):
    player_battle_data = PlayerBattleDataStruct()
    player_battle_data.clan = transform_player_clan(x['clan'])
    player_battle_data.cards = transform_player_item_level_list(x['cards'])
    player_battle_data.tag = x['tag']
    player_battle_data.name = x['name']
    player_battle_data.starting_trophies = x['startingTrophies']
    player_battle_data.trophy_change = x['trophyChange']
    player_battle_data.crowns = x['crowns']
    player_battle_data.king_tower_hit_points = x['kingTowerHitPoints']
    player_battle_data.princess_towers_hit_points = x['princessTowerHitPoints']
    return player_battle_data

