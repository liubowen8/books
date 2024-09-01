"""
每组有8个交换机，每一个交换机有失效率，计算每组失效不同交换机数量的概率
计算每组，失效的交换机的数量小于等于x的概率
计算各组中交换机失效个数最大为y的概率
"""
import numpy as np
from scipy.stats import binom

# 参数定义
n = 8  # 每组交换机的数量
x = 0.1  # 交换机失效率（即坏的概率）

# 计算每个可能坏的交换机数目的概率
def compute_probabilities(n, x):
    probabilities = {}
    for k in range(n + 1):
        probability = binom.pmf(k, n, x)
        probabilities[k] = probability
    return probabilities

# 计算并打印结果
probabilities = compute_probabilities(n, x)

for k, prob in probabilities.items():
    print(f"坏的交换机数为 {k} 的概率为: {prob:.4f}")
    

print(probabilities)

xiaoyudengyu_xs = []
for i in list(probabilities.keys()):
    print(i)
    xiaoyudengyu_x = sum(list(probabilities.values())[:i+1])
    xiaoyudengyu_xs.append(xiaoyudengyu_x)

K = 10

gezu_zuida_guzhang_geshu_x = []
for i in range(len(xiaoyudengyu_xs)):
    if i==0:
        gezu_zuida_guzhang_geshu_x.append(xiaoyudengyu_xs[i]**K)
        pass
    else:
        gezu_zuida_guzhang_geshu_x.append(xiaoyudengyu_xs[i]**K - xiaoyudengyu_xs[i-1]**K)
        pass
print(gezu_zuida_guzhang_geshu_x)
print(sum(gezu_zuida_guzhang_geshu_x))
