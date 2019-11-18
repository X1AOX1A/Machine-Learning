import sys
sys.path.append('/Users/apple/Documents/Jupyter/ML/RL_OpenAI_Gym')

from agent import Agent
from monitor import interact
import gym
import numpy as np

env = gym.make('Taxi-v2')
agent = Agent()
avg_rewards, best_avg_reward = interact(env, agent)
