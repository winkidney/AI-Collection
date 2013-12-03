#!/usr/bin/python
#coding:utf-8
#仅供测试用，为了省去每次打字的力气
import AIs  

#第一个简单反射智能体
W = AIs.VacuumCleanerWorld(AIs.VacuumCleanerRobot,1,2)

def run(total_times, eva_time, dist_generation_rate):

    W.run_ai(total_times, eva_time, dist_generation_rate)
