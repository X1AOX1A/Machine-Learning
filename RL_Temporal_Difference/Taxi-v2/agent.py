import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        

    def select_action(self, i_episode, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        
        self 
        Q_next_step = self.Q[state]
        epsilon = 1.0 / i_episode
        policy_s = np.ones(self.nA) * epsilon / self.nA # 初始化为上方括号第二行
        policy_s[np.argmax(Q_next_step)] = 1 - epsilon + (epsilon / self.nA) # 计算括号第一行 
        next_action = np.random.choice(np.arange(self.nA), p=policy_s)
        return next_action

    def step(self, state, action, reward, next_state, next_action, done, i_episode, alpha=.01, gamma=1.0):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        # Sarsa || Best average reward 9.2884
        self.Q[state][action] = self.Q[state][action]  + (alpha * (reward + (gamma * self.Q[next_state][next_action] ) - self.Q[state][action] )) 
        
        # Q-Learning || Best average reward 9.1166
        # self.Q[state][action] = self.Q[state][action]  + (alpha * (reward + (gamma * np.max(self.Q[next_state]) ) - self.Q[state][action] )) 
        