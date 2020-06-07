# Clans
class ClanStruct:
    def __init__(self):
        self.tag = ""
        self.name = ""
        self.type = ""
        self.description = ""
        self.badge_id = 0
        self.clan_score = 0
        self.clan_war_trophies = 0
        self.location = LocationStruct()
        self.required_trophies = 0
        self.donations_per_week = 0
        self.clan_chest_status = ""
        self.clan_chest_level = 0
        self.clan_chest_max_level = 0
        self.members = 0
        self.member_list = []


class GenericClanStruct:
    def __init__(self):
        self.tag = ""
        self.name = ""
        self.badge_id = 0


class MemberStruct:
    def __init__(self):
        self.tag = ""
        self.name = ""
        self.role = ""
        self.last_seen = ""
        self.exp_level = 0
        self.trophies = 0
        self.arena = ArenaStruct()
        self.clan_rank = 0
        self.previous_clan_rank = 0
        self.donations = 0
        self.donations_received = 0
        self.clan_chest_points = 0


class LocationStruct:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.is_country = False
        self.country_code = ""


class ArenaStruct:
    def __init__(self):
        self.id = ""
        self.name = ""


# Clans -> Wars
class WarLogStruct:
    def __init__(self):
        self.items = []


class WarStruct:
    def __init__(self):
        self.season_id = 0
        self.created_date = ""
        self.participants = []
        self.standings = []


class ParticipantStruct:
    def __init__(self):
        self.tag = ""
        self.name = ""
        self.cards_earned = 0
        self.battles_played = 0
        self.wins = 0
        self.collection_day_battles_played = 0
        self.number_of_battles = 0


class StandingStruct:
    def __init__(self):
        self.clan = ClanStruct()
        self.trophy_change = 0


class StandingClanStruct:
    def __init__(self):
        self.tag = ""
        self.name = ""
        self.badge_id = 0
        self.clan_score = 0
        self.participants = 0
        self.battles_played = 0
        self.wins = 0
        self.crowns = 0


class CurrentWarStruct:
    def __init__(self):
        self.state = ""
        self.war_end_time = ""
        self.clan = StandingClanStruct()
        self.participants = []
        self.clans = []


# Players
class PlayerStruct:
    def __init__(self):
        self.tag = ""
        self.name = ""
        self.exp_level = 0
        self.trophies = 0
        self.best_trophies = 0
        self.wins = 0
        self.losses = 0
        self.battle_count = 0
        self.three_crown_wins = 0
        self.challenge_cards_won = 0
        self.challenge_max_wins = 0
        self.tournament_cards_won = 0
        self.tournament_battle_count = 0
        self.role = ""
        self.donations = 0
        self.donations_received = 0
        self.total_donations = 0
        self.war_day_wins = 0
        self.clan_cards_collected = 0
        self.clan = GenericClanStruct()
        self.arena = ArenaStruct()
        self.league_statistics = LeagueStatsStruct()
        self.badges = []
        self.achievements = []
        self.cards = []
        self.current_deck = []
        self.current_favorite_card = CardStruct()


class LeagueStatsStruct:
    def __init__(self):
        self.current_season = CurrentSeasonStatsStruct()
        self.previous_season = PreviousSeasonStatsStruct()
        self.best_season = BestSeasonStatsStruct()


class CurrentSeasonStatsStruct:
    def __init__(self):
        self.trophies = 0
        self.best_trophies = 0


class PreviousSeasonStatsStruct:
    def __init__(self):
        self.id = ""
        self.trophies = 0
        self.best_trophies = 0


class BestSeasonStatsStruct:
    def __init__(self):
        self.id = ""
        self.trophies = 0


class BadgeStruct:
    def __init__(self):
        self.name = ""
        self.progress = 0


class LevelEnabledBadgeStruct:
    def __init__(self):
        self.name = ""
        self.level = 0
        self.max_level = 0
        self.progress = 0
        self.target = 0


class AchievementStruct:
    def __init__(self):
        self.name = ""
        self.stars = 0
        self.value = 0
        self.target = 0
        self.info = ""
        self.completion_info = {}


class LeveledCardStruct:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.level = 0
        self.max_level = 0
        self.count = 0
        self.icon_urls = IconUrlsStruct()


class CardStruct:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.max_level = 0
        self.icon_urls = IconUrlsStruct()


class IconUrlsStruct:
    def __init__(self):
        self.medium = ""


# Players -> Chests
class UpcomingChestsStruct:
    def __init__(self):
        self.items = []


class ChestStruct:
    def __init__(self):
        self.index = 0
        self.name = ""


# Players -> Battle log
class BattleLogStruct:
    def __init__(self):
        self.items = []


class BattleStruct:
    def __init__(self):
        self.type = ""
        self.battle_time = ""
        self.is_ladder_tournament = False
        self.arena = ArenaStruct()
        self.game_mode = GameModeStruct()
        self.deck_selection = ""
        self.team = []
        self.opponent = []


class GameModeStruct:
    def __init__(self):
        self.id = 0
        self.name = ""


class ContenderStruct:
    def __init__(self):
        self.tag = ""
        self.name = ""
        self.starting_trophies = 0
        self.crowns = 0
        self.king_tower_hit_points = 0
        self.clan = GenericClanStruct()
        self.cards = []


class CountlessLeveledCardStruct:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.level = 0
        self.max_level = 0
        self.icon_urls = IconUrlsStruct()

