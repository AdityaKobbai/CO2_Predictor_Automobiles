def determine_rating(predictions):
    ratings = {
        1: (381, 608),
        2: (336, 408),
        3: (284, 356),
        4: (234, 316),
        5: (202, 270),
        6: (165, 226),
        7: (133, 201),
        8: (104, 175),
        9: (99, 147),
        10: (94, 124)
    }

    possible_ratings = []
    for rating, (min_val, max_val) in ratings.items():
        if min_val <= predictions <= max_val:
            possible_ratings.append(rating)

    return possible_ratings if possible_ratings else None
