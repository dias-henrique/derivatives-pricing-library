from geometric_brownian_motion import geometric_brownian_motion
from simulation_class import simulation_class
from market_environment import market_environment
from constant_short_rate import constant_short_rate
from get_year_deltas import get_year_deltas
from sn_random_numbers import sn_random_numbers
import datetime as dt

me_gbm = market_environment('me_gbm', dt.datetime(2020, 1, 1))

me_gbm.add_constant('initial_value', 36.)
me_gbm.add_constant('volatility', 0.2)
me_gbm.add_constant('final_date', dt.datetime(2020, 12, 31))
me_gbm.add_constant('currency', 'EUR')
me_gbm.add_constant('frequency', 'M')
me_gbm.add_constant('paths', 10000)

csr = constant_short_rate('csr', 0.06)
me_gbm.add_curve('discount_curve', csr)
