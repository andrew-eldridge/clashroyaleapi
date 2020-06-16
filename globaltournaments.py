from .cards import *
from .clans import *
from .locations import *
from .players import *
from .rankings import *
from .tournaments import *
from .format import *


def transform_ladder_tournament_list(x):
    ladder_tournament_list = LadderTournamentListStruct()
    ladder_tournament_list.items = []
    for item in x['items']:
        ladder_tournament_list.items.append(transform_ladder_tournament(item))
    return ladder_tournament_list


def transform_ladder_tournament(x):
    ladder_tournament = LadderTournamentStruct()
    ladder_tournament.game_mode = x['gameMode']
    ladder_tournament.max_losses = x['maxLosses']
    ladder_tournament.min_exp_level = x['minExpLevel']
    ladder_tournament.tournament_level = x['tournamentLevel']
    ladder_tournament.milestone_rewards = transform_survival_milestone_reward_list(x['milestoneRewards'])
    ladder_tournament.free_tier_rewards = transform_survival_milestone_reward_list(x['freeTierRewards'])
    ladder_tournament.tag = x['tag']
    ladder_tournament.title = x['title']
    ladder_tournament.start_time = x['startTime']
    ladder_tournament.end_time = x['endTime']
    ladder_tournament.top_rank_reward = transform_survival_milestone_reward_list(x['topRankReward'])
    ladder_tournament.max_top_reward_rank = x['maxTopRewardRank']
    return ladder_tournament


def transform_survival_milestone_reward_list(x):
    survival_milestone_reward_list = SurvivalMilestoneRewardListStruct()
    survival_milestone_reward_list.items = []
    for item in x:
        survival_milestone_reward_list.items.append(transform_survival_milestone_reward(item))
    return survival_milestone_reward_list


def transform_survival_milestone_reward(x):
    survival_milestone_reward = SurvivalMilestoneRewardStruct()
    survival_milestone_reward.chest = x['chest']
    survival_milestone_reward.rarity = x['rarity']
    survival_milestone_reward.resource = x['resource']
    survival_milestone_reward.type = x['type']
    survival_milestone_reward.amount = x['amount']
    survival_milestone_reward.card = transform_item(x['card'])
    survival_milestone_reward.wins = x['wins']
    return survival_milestone_reward

