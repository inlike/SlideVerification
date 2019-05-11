import numpy as np
import math


def ease_out_expo(x):
    """
    曲线函数
    :param x:
    :return:
    """
    if x == 1:
        return 1
    else:
        return 1 - pow(2, -10 * x)


def get_tracks(distance, seconds):
    """
    轨迹生成函数
    :param distance: 滑动总距离
    :param seconds: 滑动总时间
    :return:
    """
    tracks = [0]  # 存放轨迹的数组
    offsets = [0]  # 存放滑动总距离的记录数组
    for t in np.arange(0.0, seconds, 0.1):  # 产生一个数列如[0.0, 0.1, 0.2, 0.3]
        offset = round(ease_out_expo(t/seconds) * distance)  # 根据时间t计算在曲线上的滑动距离
        tracks.append(offset - offsets[-1])  # 本次计算的距离减去上一次移动的距离，得到本次的轨迹
        offsets.append(offset)  # 至本次滑动了的总距离
    return offsets, tracks


a, b = get_tracks(138, 3)
print(a, b)


def get_tracksb(distance):
    """
    根据物理的先加速再减速规律计算
    :param distance:
    :return:
    """
    distance += 20  # 加上20是为了滑动超过缺口再回滑
    v = 0  # 初速度
    t = 0.2  # 以0.2秒为一个计算周期
    forward_tracks = []  # 轨迹记录数组
    current = 0  # 初始移动距离
    mid = distance * 3 / 5  # 减速阀值即五分之三的距离加速剩下距离减速
    while current < distance:  # 总移动距离等于输入距离时结束
        if current < mid:  # 加速状态
            a = 2  # 加速度为+2
        else:  # 减速状态
            a = -3  # 加速度-3
            
        s = v * t + 0.5 * a * (t ** 2)  # 计算0.2秒周期内的位移
        v = v + a * t  # 计算本次周期后的速度
        current += s  # 将之前移动的总距离，加上本次0.2秒周期内移动的距离
        forward_tracks.append(round(s))  # 记录本次0.2秒周期内的移动距离为轨迹

    back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]  # 手动将开头加上的20，生成减去轨迹，即回滑轨迹
    return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}
