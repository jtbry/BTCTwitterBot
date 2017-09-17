import datetime
import random
from collections import namedtuple

Prices = namedtuple('prices', ['usd', 'gbp', 'eur'])

def _generate_prices(update_chance = 0.35, max_change=0.08):
    """ A generator that will return and endless stream of price tuples, updating
        the price by +- 8% 35% of the time. """

    # initial prices
    prices = Prices(usd=3776.8525, gbp=2778.4227, eur=3161.7354)
    updated = datetime.datetime.utcnow().strftime("%b %d, %Y %H:%M:%S UTC")

    while True:
        # nicely format our output
        formatted_out = Prices(*(format(x, ',.4f') for x in prices))

        yield formatted_out.usd, formatted_out.eur, formatted_out.gbp, updated

        # every so often, update the prices
        if random.random() < update_chance:

            # random price change of maximum +- 8%
            multiplier = random.uniform(1 - max_change, 1 + max_change)

            # update the prices (creating a new namedtuple with updated prices)
            prices = Prices(*(multiplier * x for x in prices))

            # Update the time of this price
            updated = datetime.datetime.utcnow().strftime("%b %d, %Y %H:%M:%S UTC")


_g = _generate_prices()

def retrieveprice():
    """Retrieve some fake data, for testing purposes."""
    return list(next(_g))


# if run as a script, print out some tests
if __name__ == "__main__":
    for _ in range(10):
        results = retrieveprice()
        print(results)
