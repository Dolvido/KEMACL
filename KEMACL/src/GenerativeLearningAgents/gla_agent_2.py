"""
GLA (Generative Learning Agent)
---------------------------

This module defines a Generative Learning Agent (GLA) that can learn from its interactions with the environment
and other agents.

"""

import random
import numpy as np
from typing import List, Dict

class GLAgent:
    def __init__(self, name: str):
        self.name = name
        self.memory = []  # list to store past experiences
        self.model = None  # model for making predictions
        self.reward = 0  # initial reward