def calculate_fine(delay_days):
    if delay_days <= 0:
        return 0

    fine = 0
    remaining = delay_days

    week1 = min(remaining, 7)
    fine += week1 * 10
    remaining -= week1

    if remaining <= 0:
        return fine

    week2 = min(remaining, 7)
    fine += week2 * 20
    remaining -= week2

    if remaining <= 0:
        return fine

    week3 = min(remaining, 7)
    fine += week3 * 60
    remaining -= week3

    if remaining <= 0:
        return fine

    # after 3 weeks, keep doubling rate each week
    rate = 120
    while remaining > 0:
        chunk = min(remaining, 7)
        fine += chunk * rate
        remaining -= chunk
        rate *= 2

    return fine
