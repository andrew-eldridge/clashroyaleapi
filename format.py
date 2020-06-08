class ClanListStruct:
    def __init__(self):
        self.items = None


class ClanStruct:
    def __init__(self):
        self.member_list = ClanMemberListStruct()
        self.badge_id = None
        self.tag = None
        self.donations_per_week = None
        self.clan_chest_status = None
        self.clan_chest_level = None
        self.clan_chest_max_level = None
        self.clan_war_trophies = None
        self.required_trophies = None
        self.clan_score = None
        self.name = None
        self.location = LocationStruct()
        self.type = None
        self.members = None
        self.description = None
        self.clan_chest_points = None
        self.badge_urls = None


class ClanMemberListStruct:
    def __init__(self):
        self.items = None


class LocationStruct:
    def __init__(self):
        self.localized_name = None
        self.id = None
        self.name = None
        self.is_country = None
        self.country_code = None


class ClanMemberStruct:
    def __init__(self):
        self.arena = ArenaStruct()
        self.clan_chest_points = None
        self.last_seen = None
        self.tag = None
        self.name = None
        self.role = None
        self.exp_level = None
        self.trophies = None
        self.clan_rank = None
        self.previous_clan_rank = None
        self.donations = None
        self.donations_received = None


class ArenaStruct:
    def __init__(self):
        self.name = None
        self.id = None
        self.icon_urls = None


class ClanWarLogStruct:
    def __init__(self):
        self.items = None


class ClanWarLogEntryStruct:
    def __init__(self):
        self.standings = ClanWarStandingListStruct()
        self.season_id = None
        self.participants = ClanWarParticipantListStruct()
        self.created_date = None


class ClanWarStandingListStruct:
    def __init__(self):
        self.items = None


class ClanWarParticipantListStruct:
    def __init__(self):
        self.items = None


class ClanWarStandingStruct:
    def __init__(self):
        self.trophy_change = None
        self.clan = ClanWarClanStruct()


class ClanWarParticipantStruct:
    def __init__(self):
        self.tag = None
        self.name = None
        self.cards_earned = None
        self.battles_played = None
        self.wins = None
        self.collection_day_battles_played = None
        self.number_of__battles = None


class ClanWarClanStruct:
    def __init__(self):
        self.tag = None
        self.clan_score = None
        self.crowns = None
        self.badge_id = None
        self.name = None
        self.participants = None
        self.battles_played = None
        self.wins = None


class CurrentClanWarStruct:
    def __init__(self):
        self.state = None
        self.clan = ClanWarClanStruct()
        self.participants = ClanWarParticipantListStruct()
        self.clans = ClanWarClanListStruct()
        self.collection_end_time = None
        self.war_end_time = None


class ClanWarClanListStruct:
    def __init__(self):
        self.items = None


class PlayerStruct:
    def __init__(self):
        self.clan = PlayerClanStruct()
        self.arena = ArenaStruct()
        self.role = None
        self.wins = None
        self.losses = None
        self.total_donations = None
        self.league_statistics = PlayerLeagueStatisticsStruct()
        self.cards = PlayerItemLevelListStruct()
        self.current_favourite_card = ItemStruct()
        self.badges = PlayerAchievementBadgeListStruct()
        self.tag = None
        self.name = None
        self.exp_level = None
        self.trophies = None
        self.best_trophies = None
        self.donations = None
        self.donations_received = None
        self.achievements = PlayerAchievementProgressListStruct()
        self.battle_count = None
        self.three_crown_wins = None
        self.challenge_cards_won = None
        self.challenge_max_wins = None
        self.tournament_cards_won = None
        self.tournament_battle_count = None
        self.current_deck = PlayerItemLevelListStruct()
        self.war_day_wins = None
        self.clan_cards_collected = None
        self.star_points = None


class PlayerClanStruct:
    def __init__(self):
        self.badge_id = None
        self.tag = None
        self.name = None
        self.badge_urls = None


class PlayerLeagueStatisticsStruct:
    def __init__(self):
        self.previous_season = LeagueSeasonResultStruct()
        self.current_season = LeagueSeasonResultStruct()
        self.best_season = LeagueSeasonResultStruct()


class PlayerItemLevelListStruct:
    def __init__(self):
        self.items = None


class ItemStruct:
    def __init__(self):
        self.icon_urls = None
        self.name = None
        self.id = None
        self.max_level = None


class PlayerAchievementBadgeListStruct:
    def __init__(self):
        self.items = None


class PlayerAchievementProgressListStruct:
    def __init__(self):
        self.items = None


class LeagueSeasonResultStruct:
    def __init__(self):
        self.rank = None
        self.trophies = None
        self.best_trophies = None
        self.id = None


class PlayerItemLevelStruct:
    def __init__(self):
        self.id = None
        self.count = None
        self.level = None
        self.star_level = None
        self.name = None
        self.max_level = None
        self.icon_urls = None


class PlayerAchievementBadgeStruct:
    def __init__(self):
        self.max_level = None
        self.progress = None
        self.target = None
        self.level = None
        self.name = None


class PlayerAchievementProgressStruct:
    def __init__(self):
        self.stars = None
        self.value = None
        self.name = None
        self.target = None
        self.info = None
        self.completion_info = None


class UpcomingChestsStruct:
    def __init__(self):
        self.items = ChestListStruct()


class ChestListStruct:
    def __init__(self):
        self.items = None


class ChestStruct:
    def __init__(self):
        self.name = None
        self.index = None
        self.icon_urls = None


class BattleListStruct:
    def __init__(self):
        self.items = None


class BattleStruct:
    def __init__(self):
        self.game_mode = GameModeStruct()
        self.arena = ArenaStruct()
        self.type = None
        self.deck_selection = None
        self.team = PlayerBattleDataListStruct()
        self.opponent = PlayerBattleDataListStruct()
        self.challenge_win_count_before = None
        self.battle_time = None
        self.challenge_id = None
        self.tournament_tag = None
        self.challenge_title = None
        self.replay_tag = None
        self.is_ladder_tournament = None


class GameModeStruct:
    def __init__(self):
        self.id = None
        self.name = None


class PlayerBattleDataListStruct:
    def __init__(self):
        self.items = None


class PlayerBattleDataStruct:
    def __init__(self):
        self.clan = PlayerClanStruct()
        self.cards = PlayerItemLevelListStruct()
        self.tag = None
        self.name = None
        self.starting_trophies = None
        self.trophy_change = None
        self.crowns = None
        self.king_tower_hit_points = None
        self.princess_towers_hit_points = None


class ItemListStruct:
    def __init__(self):
        self.items = None


class TournamentHeaderListStruct:
    def __init__(self):
        self.items = None


class TournamentHeaderStruct:
    def __init__(self):
        self.status = None
        self.preparation_duration = None
        self.created_time = None
        self.first_place_card_prize = None
        self.game_mode = GameModeStruct()
        self.duration = None
        self.type = None
        self.tag = None
        self.creator_tag = None
        self.name = None
        self.description = None
        self.capacity = None
        self.max_capacity = None
        self.level_cap = None


class TournamentStruct:
    def __init__(self):
        self.members_list = TournamentMemberListStruct()
        self.status = None
        self.preparation_duration = None
        self.created_time = None
        self.started_time = None
        self.ended_time = None
        self.first_place_card_prize = None
        self.game_mode = GameModeStruct()
        self.duration = None
        self.type = None
        self.tag = None
        self.creator_tag = None
        self.name = None
        self.description = None
        self.capacity = None
        self.max_capacity = None
        self.level_cap = None


class TournamentMemberListStruct:
    def __init__(self):
        self.items = None


class TournamentMemberStruct:
    def __init__(self):
        self.clan = PlayerClanStruct()
        self.rank = None
        self.previous_rank = None
        self.tag = None
        self.name = None
        self.score = None


class LocationListStruct:
    def __init__(self):
        self.items = None


class ClanRankingListStruct:
    def __init__(self):
        self.items = None


class ClanRankingStruct:
    def __init__(self):
        self.clan_score = None
        self.badge_id = None
        self.location = LocationStruct()
        self.members = None
        self.tag = None
        self.name = None
        self.rank = None
        self.previous_rank = None
        self.badge_urls = None


class PlayerRankingListStruct:
    def __init__(self):
        self.items = None


class PlayerRankingStruct:
    def __init__(self):
        self.clan = PlayerRankingClanStruct()
        self.arena = ArenaStruct()
        self.tag = None
        self.name = None
        self.exp_level = None
        self.rank = None
        self.previous_rank = None
        self.trophies = None


class PlayerRankingClanStruct:
    def __init__(self):
        self.badge_id = None
        self.tag = None
        self.name = None
        self.badge_urls = None


class LadderTournamentRankingListStruct:
    def __init__(self):
        self.items = None


class LadderTournamentRanking:
    def __init__(self):
        self.clan = PlayerRankingClanStruct()
        self.wins = None
        self.losses = None
        self.tag = None
        self.name = None
        self.rank = None
        self.previous_rank = None


class LadderTournamentListStruct:
    def __init__(self):
        self.items = None


class LadderTournamentStruct:
    def __init__(self):
        self.game_mode = GameModeStruct()
        self.max_losses = None
        self.min_exp_level = None
        self.tournament_level = None
        self.milestone_rewards = SurvivalMilestoneRewardListStruct()
        self.free_tier_rewards = SurvivalMilestoneRewardListStruct()
        self.tag = None
        self.title = None
        self.start_time = None
        self.end_time = None
        self.top_rank_reward = SurvivalMilestoneRewardListStruct()
        self.max_top_reward_rank = None


class SurvivalMilestoneRewardListStruct:
    def __init__(self):
        self.items = None


class SurvivalMilestoneRewardStruct:
    def __init__(self):
        self.chest = None
        self.rarity = None
        self.resource = None
        self.type = None
        self.amount = None
        self.card = ItemStruct()
        self.wins = None

