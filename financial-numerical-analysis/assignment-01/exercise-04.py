# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
#第一小题：
set1_A = {"神州长城", "中集集团", "晨鸣纸业", "古井贡酒", "招商港口", "百联股份", "浙江医药", "江西铜业", "中金黄金", "国泰君安", "掌阅科技"}
set2_B = {"神州长城", "中集集团", "晨鸣纸业", "古井贡酒", "招商港口", "百联股份"}
set3_H = {"中集集团", "晨鸣纸业", "江西铜业", "国泰君安", "小米集团", "阿里影业", "平安好医生"}

#第二小题：
set4_intersection = set1_A & set2_B & set3_H
print(set4_intersection)
set5_union = set1_A | set2_B | set3_H
print(set5_union)
set6 = set1_A - set2_B
set7 = set3_H - set1_A
print(set6, "\n", set7)

#第三小题：
set1_A.add("光大证券")
set3_H.add("光大证券")
print(set1_A, set3_H)

#第锶小题：
set1_A.remove("神州长城")
# print(set1_A)
set2_B.remove("神州长城")
set3_H.remove("小米集团")
set3_H.remove("阿里影业")
print(set2_B, set3_H)