import numpy as np
import random
import os
import torch


class DIYAgent:
    """
    DIY智能体
    """

    def __init__(self, args):
        self.args = args

    # 必须完成：
    def choose_action(self):
        '''
        observation与info包含了环境的返回的即时观测与各种信息，你可以充分利用他们来设计你的决策方法；
        具体来说，observation和info是两个字典dict，你可以调用他们中的以下内容：
        :param observation:
        observation = {
            "local_view": np.array(shape=(5, 5), dtype=np.int32),
            # 以智能体为中心的5×5局部视野
            # 值域: 0=障碍物, 1=通路, 2=起点, 3=终点, 4=宝箱, 5=智能体

            "agent_pos": np.array(shape=(2,), dtype=np.int32),
            # 智能体当前位置 [x, y]

            "target_pos": np.array(shape=(2,), dtype=np.int32),
            # 终点位置 [x, y]

            "treasure_status": np.array(shape=(10,), dtype=np.int8),
            # 10个宝箱的状态，1=未收集，0=已收集

            "location_memory": np.array(shape=(64, 64), dtype=np.float32),
            # 位置访问记忆，每访问一次增加0.1，上限1.0，未访问过的位置均为0.0

            "map_visible": np.array(shape=(64, 64), dtype=np.int32),
            # 已探索区域的地图，探索过的区域显示地图元素，未探索为-1
            # 智能体当前位置标记为5
        }
        :param info:
        info = {
            "result_message": "Running" | "Success" | "Failure",  #正在运行 | 顺利抵达终点  |  失败

            "game_info": {
                "score": float,              # 本步即时得分
                "total_score": float,        # 当前总得分（在达到步数上线时会不断累计，但是在最后一步1200还没到达终点时会清零）
                "step_no": int,              # 当前已经走过的步数
                "pos_x": int,                # X坐标
                "pos_y": int,                # Y坐标
                "blocked": int               # 0或1：1表示前一步撞到墙上导致位置不改变，0则表示上一步顺利移动了一格
                "legal_act": [1,0,1,1],      # 当前状态下，4个动作的合法性（1=合法，0=非法）
                "treasure_count": int,       # 已收集宝箱数量
                "treasure_score": int,       # 通过宝箱获取的累计得分
                "treasure_status": [0,1,1,0,...],  # 宝箱状态列表
            },

            "score_info": {
                "score": float,             # 同game_info["score"]
                "total_score": float        # 同game_info["total_score"]
            }
        }
        :return: 动作，0，1，2，3中的某一个值
        0： 坐标 + [0,1]
        1： 坐标 + [0,-1]
        2： 坐标 + [-1,0]
        3： 坐标 + [1,0]
        '''
        pass

    # 不限制其他函数的自定义与使用，如:
    # 构建特征提取函数、网络权重保存与导入函数、构建强化学习训练函数、通过obs和info构建奖励函数等等
