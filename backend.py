import pandas as pd
import joblib

# =====================
# LOAD MODEL + COLUMNS
# =====================
rf = joblib.load("winner_model.pkl")
columns = joblib.load("columns.pkl")


# =====================
# WINNER PREDICTION
# =====================
def predict_match(team1, team2, toss_winner, toss_decision, venue):

    input_df = pd.DataFrame({
        "team1": [team1],
        "team2": [team2],
        "toss_winner": [toss_winner],
        "toss_decision": [toss_decision],
        "venue": [venue],
        "team1_form": [0.5],
        "team2_form": [0.5],
        "head_to_head": [0.5]
    })

    input_encoded = pd.get_dummies(input_df)

    input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

    pred = rf.predict(input_encoded)[0]

    return team1 if pred == 1 else team2


# =====================
# PLAYER OF MATCH LOGIC
# =====================
deliveries = pd.read_csv("data/deliveries.csv")

# Batting stats
batting_stats = deliveries.groupby(["match_id", "batsman"]).agg({
    "batsman_runs": "sum",
    "ball": "count"
}).reset_index()

batting_stats.rename(columns={
    "batsman": "player",
    "batsman_runs": "runs",
    "ball": "balls"
}, inplace=True)

batting_stats["strike_rate"] = (batting_stats["runs"] / batting_stats["balls"]) * 100

# Bowling stats
bowling_stats = deliveries[deliveries["player_dismissed"].notnull()]
bowling_stats = bowling_stats.groupby(["match_id", "bowler"]).agg({
    "player_dismissed": "count"
}).reset_index()

bowling_stats.rename(columns={
    "bowler": "player",
    "player_dismissed": "wickets"
}, inplace=True)

# Merge both
player_stats = pd.merge(
    batting_stats,
    bowling_stats,
    on=["match_id", "player"],
    how="left"
)

player_stats["wickets"] = player_stats["wickets"].fillna(0)

# Performance score
player_stats["performance_score"] = (
    player_stats["runs"] +
    (player_stats["wickets"] * 20) +
    (player_stats["strike_rate"] * 0.1)
)

# Best player per match
best_players = player_stats.loc[
    player_stats.groupby("match_id")["performance_score"].idxmax()
]


# =====================
# GET BEST PLAYER
# =====================
def get_best_player(match_id=1):

    player = best_players[best_players["match_id"] == match_id]

    if len(player) == 0:
        return "Unknown"

    return player.iloc[0]["player"]