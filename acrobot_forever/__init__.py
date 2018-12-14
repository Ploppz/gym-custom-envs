import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='AcrobotForever-v1',
    entry_point='acrobot_forever.envs:AcrobotForeverEnv',
)
