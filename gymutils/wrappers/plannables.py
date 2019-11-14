import gym
import numpy as np


class SavableEnv(gym.Wrapper):
	def __init__(self, env):
		super().__init__(env)
	def reset(self, **kwargs):
		return self.env.reset(**kwargs)
	def step(self, action):
		return self.env.step(action)
	def save(self):
		self._checkpoint = self.env.unwrapped.clone_state()
		return self._checkpoint
	def load(self, checkpoint=None):
		if checkpoint:
			self._checkpoint = checkpoint
		self.env.unwrapped.restore_state(self._checkpoint)


class ObsTreeNode:
	def __init__(self, env, height=0, parent=None,
				 action=0, reward=0, terminal=False, info=None,
				 total_reward=0, tree_height=-1):
		if not isinstance(env, gym.envs.atari.atari_env.AtariEnv):
			env = env.unwrapped

		self.height = height
		if tree_height < 0:
			self.tree_height = self.height
		else:
			self.tree_height = tree_height

		self.parent = parent
		self.is_root = parent is None
		self.is_child = not self.is_root

		self.n_children = env.action_space.n
		self.id = 0
		if self.is_child:
			self.id += self.parent.id * self.n_children + 1 + action

		self.action = action  # edge connected from parent
		self.reward = reward
		self.total_reward = total_reward + reward
		self.terminal = terminal
		self.state = None
		self.obs = None
		if not terminal:
			self.state = env.clone_state()
			self.obs = env._get_obs()
		self.info = info

		self.children = None
		if not terminal and height > 0:
			self._extends(env)
		self.is_leaf = self.children is None

		env.restore_state(self.state)

	def _extends(self, env):
		self.children = []
		for a in range(self.n_children):
			env.restore_state(self.state)
			_, reward, terminal, info = env.step(a)
			child = ObsTreeNode(env, self.height - 1, self,
								a, reward, terminal, info,
								self.total_reward, self.tree_height)
			self.children.append(child)


class ObsTreeEnv(gym.Wrapper):
	def __init__(self, env, depth=0):
		super().__init__(env)
		self.depth = depth
	def reset(self, **kwargs):
		_ = self.env.reset(**kwargs)
		return self._get_tree()
	def step(self, action):
		_, reward, terminal, info = self.env.step(action)
		return self._get_tree(), reward, terminal, info
	def _get_tree(self):
		return ObsTreeNode(env, self.depth)
