spine = 1
leaf_zhuban = 1
guangmokuai = 1
jiedian=1
npu=1

leaf_zhuban_bushixiao = 1-leaf_zhuban
suoyou_leaf_bushixiao = leaf_zhuban_bushixiao*288
cunzai_yige_leaf_shixiao = 1-suoyou_leaf_bushixiao

jiedian_bushixiao = 1-jiedian
suoyou_jiedian_bushixiao = jiedian_bushixiao*288*4
cunzai_yige_jiedian_shixiao = 1-suoyou_jiedian_bushixiao

# 同一个leaf下，不同的节点
# 情况1 存在一个leaf坏了
p1 = cunzai_yige_leaf_shixiao
# 情况2 所以leaf交换机是好的
p2 = suoyou_leaf_bushixiao
# 2.1 存在2NPU失效
def leaf_haodeqiangkuangxia_2NPU_shixaiao_de_gailv():
    res= [0]
    temp=[]
    def huishu(temp, res):
        if len(temp)==8:
            print(temp)
            zuobian= temp[:4]
            youbian=temp[4:]
            if sum(zuobian)>1 and sum(youbian)>1:
                xxx=1
                gailvs=[guangmokuai, jiedian,guangmokuai, npu,guangmokuai,jiedian,guangmokuai,npu]
                for i in range(len(temp)):
                    if temp[i]==1:
                        xxx = xxx*gailvs[i]
                    else:
                        xxx=xxx*(1-gailvs[i])
                res[0]= res[0]+xxx
            return
        for i in range(2):
            temp.append(i)
            huishu(temp,res)
            temp.pop()
    huishu(temp, res)
    return res[0]

_2NPU_shixiao_gialv = leaf_haodeqiangkuangxia_2NPU_shixaiao_de_gailv()
_2NPU_bushixiao_ = 1-_2NPU_shixiao_gialv
all_2NPU_bushixiao = _2NPU_bushixiao_ * (9216/2)
cunzai_yige_2NPU_shixiao = 1-all_2NPU_bushixiao
p21 = cunzai_yige_2NPU_shixiao
jieguo = p1 + p2*p21


#  一个节点内
# 情况1 存在一个leaf交换机坏了
p1 = cunzai_yige_leaf_shixiao
# 情况2：leaf交换机都是好的
p2 = suoyou_leaf_bushixiao
    # 2.1 存在一个节点坏了
p21 = cunzai_yige_jiedian_shixiao
    # 2.2 节点都是好的
p22 = suoyou_jiedian_bushixiao
        # 2.2.1 2NPU失效
def leaf_haodeqiangkuangxia_2NPU_shixaiao_de_gailv1():
    res= [0]
    temp=[]
    def huishu(temp, res):
        if len(temp)==6:
            print(temp)
            zuobian= temp[:3]
            youbian=temp[3:]
            if sum(zuobian)>1 and sum(youbian)>1:
                xxx=1
                gailvs=[guangmokuai,guangmokuai, npu,guangmokuai,guangmokuai,npu]
                for i in range(len(temp)):
                    if temp[i]==1:
                        xxx = xxx*gailvs[i]
                    else:
                        xxx=xxx*(1-gailvs[i])
                res[0]= res[0]+xxx
            return
        for i in range(2):
            temp.append(i)
            huishu(temp,res)
            temp.pop()
    huishu(temp, res)
    return res[0]

_2NPU_shixiao_gialv = leaf_haodeqiangkuangxia_2NPU_shixaiao_de_gailv1()
_2NPU_bushixiao_ = 1-_2NPU_shixiao_gialv
all_2NPU_bushixiao = _2NPU_bushixiao_ * (9216/2)
cunzai_yige_2NPU_shixiao = 1-all_2NPU_bushixiao
p221 = cunzai_yige_2NPU_shixiao
jieguo = p1 + p2*p21 + p2*p22*p221


# 不同leaf交换机下
#1： spine交换机都失效
p1 =  spine*16
#2：存在一个spine交换机是好的 
p2 = 1-p1
    # 2.1 2NPU失效
def leaf_haodeqiangkuangxia_2NPU_shixaiao_de_gailv2():
    res= [0]
    temp=[]
    def huishu(temp, res):
        if len(temp)==12:
            print(temp)
            zuobian= temp[:6]
            youbian=temp[6:]
            if sum(zuobian)>1 and sum(youbian)>1:
                xxx=1
                gailvs=[guangmokuai,leaf_zhuban,guangmokuai, jiedian,guangmokuai, npu,guangmokuai,leaf_zhuban,guangmokuai,jiedian,guangmokuai,npu]
                for i in range(len(temp)):
                    if temp[i]==1:
                        xxx = xxx*gailvs[i]
                    else:
                        xxx=xxx*(1-gailvs[i])
                res[0]= res[0]+xxx
            return
        for i in range(2):
            temp.append(i)
            huishu(temp,res)
            temp.pop()
    huishu(temp, res)
    return res[0]
# p21 = leaf_haodeqiangkuangxia_2NPU_shixaiao_de_gailv2()
_2NPU_shixiao_gialv = leaf_haodeqiangkuangxia_2NPU_shixaiao_de_gailv2()
_2NPU_bushixiao_ = 1-_2NPU_shixiao_gialv
all_2NPU_bushixiao = _2NPU_bushixiao_ * (9216/2)
cunzai_yige_2NPU_shixiao = 1-all_2NPU_bushixiao
p21 = cunzai_yige_2NPU_shixiao
jieguo = p1 + p2*p21
