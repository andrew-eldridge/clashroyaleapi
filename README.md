<header>
Clash Royale API<br>
JSON->Python Object Transformer<br>
Written by Andrew Eldridge<br>
https://andrewcentral.com<br>
6/7/2020
</header>

<ul>
    <li><h6>clashroyaleapi</h6>
        <ul>
            <li><b>format</b>: struct dictionary for JSON responses</li>
            <li><b>clans</b>: transform /v1/clans dict objects<ul>
                <li>ClanListStruct</li>
                <li>ClanStruct</li>
                <li>ClanMemberListStruct</li>
                <li>ClanMemberStruct</li>
                <li>ClanWarLogStruct</li>
                <li>ClanWarLogEntryStruct</li>
                <li>ClanWarStandingListStruct</li>
                <li>ClanWarParticipantListStruct</li>
                <li>ClanWarStandingStruct</li>
                <li>ClanWarParticipantStruct</li>
                <li>ClanWarClanStruct</li>
                <li>CurrentClanWarStruct</li>
                <li>ClanWarClanListStruct</li>
            </ul></li>
            <li><b>players</b>: transform /v1/players dict objects<ul>
                <li>ArenaStruct</li>
                <li>PlayerStruct</li>
                <li>PlayerClanStruct</li>
                <li>PlayerLeagueStatisticsStruct</li>
                <li>PlayerItemLevelListStruct</li>
                <li>PlayerAchievementBadgeListStruct</li>
                <li>PlayerAchievementProgressListStruct</li>
                <li>LeagueSeasonResultStruct</li>
                <li>PlayerItemLevelStruct</li>
                <li>PlayerAchievementBadgeStruct</li>
                <li>PlayerAchievementProgressStruct</li>
                <li>UpcomingChestsStruct</li>
                <li>ChestListStruct</li>
                <li>ChestStruct</li>
                <li>BattleListStruct</li>
                <li>BattleStruct</li>
                <li>GameModeStruct</li>
                <li>PlayerBattleDataListStruct</li>
                <li>PlayerBattleDataStruct</li>
            </ul></li>
            <li><b>cards</b>: transform /v1/cards dict objects<ul>
                <li>ItemStruct</li>
                <li>ItemListStruct</li>
            </ul></li>
            <li><b>tournaments</b>: transform /v1/tournaments dict objects<ul>
                <li>TournamentHeaderListStruct</li>
                <li>TournamentHeaderStruct</li>
                <li>TournamentStruct</li>
                <li>TournamentMemberListStruct</li>
                <li>TournamentMemberStruct</li>
                <li>LadderTournamentRankingListStruct</li>
                <li>LadderTournamentRankingStruct</li>
            </ul></li>
            <li><b>locations</b>: transform /v1/locations dict objects<ul>
                <li>LocationStruct</li>
                <li>LocationListStruct</li>
            </ul></li>
            <li><b>globaltournaments</b>: transform /v1/globaltournaments dict objects<ul>
                <li>LadderTournamentListStruct</li>
                <li>LadderTournamentStruct</li>
                <li>SurvivalMilestoneRewardListStruct</li>
                <li>SurvivalMilestoneRewardStruct</li>
            </ul></li>
            <li><b>rankings</b>: transform abstract ranking dict objects<ul>
                <li>ClanRankingListStruct</li>
                <li>ClanRankingStruct</li>
                <li>PlayerRankingListStruct</li>
                <li>PlayerRankingStruct</li>
                <li>PlayerRankingClanStruct</li>
            </ul></li>
        </ul>
    </li>
</ul>