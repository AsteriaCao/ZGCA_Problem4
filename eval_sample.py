import numpy as np
from environment import GorgeWalkEnv
# 从environment.so中调用迷宫环境GorgeWalkEnv
from agent_sample import SampleAgent


def make_env():
    '''
    环境的使用方法为：在一个回合（episode）内，环境首先重置（reset）并获取初始观测，
    智能体根据观测决策、选择动作并与环境交互，环境随后根据智能体的行为更新一次并返回新的观测。
    智能体继续根据观测决策，并以此循环到一个周期结束（智能体抵达终点或达到1200步）
    如果你要使用强化学习，环境通过openai gym接口封装，支持gym环境的功能，但是需要你根据obs和info自行构建奖励函数
    '''
    return GorgeWalkEnv()


def evaluate_one_episode(agent, env):
    obs, info = env.reset()
    done = False

    while not done:
        action = agent.choose_action(obs, info)
        obs, _, terminated, truncated, info = env.step(action)
        '''
        环境返回值：
        obs: 直接观测
        terminated: 抵达终点
        truncated: 超出步数上限
        info: 环境信息
        详细内容可以参考agent_diy或agent_sample中注释
        '''
        done = terminated or truncated

    return info['game_info']['total_score']


if __name__ == "__main__":
    env = make_env()
    agent = SampleAgent()

    score = evaluate_one_episode(agent, env)
    print(f"评估完成， Episode 总得分: {score}")

    env.close()
