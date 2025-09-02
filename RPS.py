def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    guess = "R"
    counter = {"R": "P", "P": "S", "S": "R"}

    if "models" not in player.__dict__:
        player.models = {2: {}, 3: {}, 4: {}, 5: {},6:{},7:{},8:{}}

    predictions = []

    for n in [2, 3, 4, 5,6,7,8]:
        if len(opponent_history) >= n:
            prev_key = "".join(opponent_history[-n:-1])
            nxt = opponent_history[-1]

            # Update model
            if prev_key not in player.models[n]:
                player.models[n][prev_key] = {}
            player.models[n][prev_key][nxt] = player.models[n][prev_key].get(nxt, 0) + 1

            # Predict
            last_pattern = "".join(opponent_history[-(n-1):])
            if last_pattern in player.models[n]:
                prediction = max(
                    player.models[n][last_pattern],
                    key=player.models[n][last_pattern].get
                )
                predictions.append(prediction)

    if predictions:
        # Majority vote
        final_prediction = max(set(predictions), key=predictions.count)
        guess = counter[final_prediction]

    return guess
