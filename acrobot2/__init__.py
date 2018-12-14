import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Acrobot-v2',
    entry_point='acrobot2.envs:Acrobot2Env',
)
