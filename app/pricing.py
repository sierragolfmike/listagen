import statistics

def calculate_fair_price(prices):
    if not prices:
        return 0.0

    # Remove obvious outliers
    q1 = statistics.quantiles(prices, n=4)[0]
    q3 = statistics.quantiles(prices, n=4)[2]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    filtered = [p for p in prices if lower_bound <= p <= upper_bound]

    if not filtered:
        return round(statistics.mean(prices), 2)

    return round(statistics.mean(filtered), 2)
