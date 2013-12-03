#!/usr/bin/python
#coding:utf-8
import random
#例一 2个方格的吸尘器世界


class VacuumCleanerRobot(object):

    """简单反射智能体"""
    env = None
    step_count = 0
    current_location = None

    def __init__(self, env):

        self.env = env
        self.current_location = [0,0]

    def move_left(self):

        self.current_location = [0,0]

    def move_right(self):

        self.current_location = [0,1]

    def suck(self,x,y):

        """清理区域"""
        self.env.world[x][y] = 'clean'

    def work(self):

        """检查状态并执行相应动作"""
        self.step_count += 1
        current_x,current_y = self.current_location[0],self.current_location[1]
        current = self.env.world[current_x][current_y]
        if current == 'dirty' :
            self.suck(current_x,current_y)
        else:
            if current_y == 0:
                self.move_right()
            else:
                self.move_left()


class VacuumCleanerWorld(object):

    world = []
    ai = None

    def __init__(self, ai_class, rows, columns):

        self.dist_generation_rate = 0.1  # max 1
        self.performance = 0
        self.ai = ai_class(self)
        self.generate_world(rows, columns)

    def generate_world(self, rows, columns):

        """生成世界，根据输入的行列参数"""
        for row in range(rows):
            world = []
            per_column = []
            for column in range(columns):
                per_column.append('clean')
            world.append(per_column)
        self.world = world

    def evaluate_performance(self):

        """度量性能，通过读取ai环境的清洁情况"""
        for row in self.world:
            for column in row:
                if column == 'clean':
                    self.performance += 1

    def add_dist(self, dist_generation_rate):

        """添加灰尘，根据默认的灰尘生成概率"""
        for i in range(len(self.world)):
            for j in range(len(self.world[i])):
                randnum = random.randint(1, 10)
                if  randnum <= dist_generation_rate*10:
                    self.world[i][j] = "dirty"

    def run_ai(self, tatal_times, eva_time, dist_generation_rate):

        self.dist_generation_rate = dist_generation_rate
        self.performance = 0
        for i in range(tatal_times):
            self.add_dist(self.dist_generation_rate)
            self.ai.work()
            if i % eva_time == 0:
                self.evaluate_performance()
        print "preformance: %s" % self.performance

def console():

    """j仅仅复制粘贴用，没有别的用处，请勿乱用=/="""
    W = VacuumCleanerWorld(VacuumCleanerRobot,1,2)

def main():

    W = VacuumCleanerWorld(VacuumCleanerRobot,1,2)
    W.add_dist(1)
    W.ai.work()
    print 1

if __name__ == "__main__":
    main()
