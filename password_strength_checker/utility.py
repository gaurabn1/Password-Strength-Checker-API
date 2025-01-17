from zxcvbn import zxcvbn


def evaluate_password_strength(password):
    analysis = zxcvbn(password)
    return {
        "score" : analysis["score"],
        "feedback" : analysis["feedback"],
        "crack_time" : analysis["crack_times_display"]["offline_slow_hashing_1e4_per_second"]

    }
