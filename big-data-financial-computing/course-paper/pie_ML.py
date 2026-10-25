import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 设置中文字体（Windows常用 SimHei / Microsoft YaHei；Mac可用 Arial Unicode MS）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 数据：来自你的表6
labels = ['换手率对数', '英伟达PE变化率', 'CAPM_Beta', 'PE对数']
sizes = [0.4732, 0.4012, 0.0874, 0.0383]

# 配色方案（学术/商务风格，可替换）
colors = ['#4472C4', '#ED7D31', '#A5A5A5', '#FFC000']

# 突出显示前两大权重
explode = (0.03, 0.03, 0, 0)

fig, ax = plt.subplots(figsize=(8, 6))

wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    autopct='%1.1f%%',
    colors=colors,
    startangle=90,
    pctdistance=0.6,
    textprops={'fontsize': 20}
)

# 美化百分比文字
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_weight('bold')

# 标题
ax.set_title('随机森林特征重要性（全样本）', fontsize=24, pad=20)

# 添加图例（可选）
ax.legend(wedges, [f'{l}: {s:.4f}' for l, s in zip(labels, sizes)],
          title="重要性",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()

# 如需保存，取消下面注释：
fig.savefig('rf_feature_importance.png', dpi=300, bbox_inches='tight')

import matplotlib.pyplot as plt
import numpy as np

# ==================== 设置中文字体 ====================
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# ==================== 数据（表7） ====================
labels = ['CAPM_Beta', 'PE对数', '换手率对数', '英伟达PE\n变化率']

upstream = [0.0043, 0.0984, 0.6520, 0.2453]  # 上游
midstream = [0.0713, 0.0977, 0.3425, 0.4885]  # 中游
downstream = [0.0274, 0.0659, 0.5938, 0.3129]  # 下游

# ==================== 统一配色 ====================
colors = ['#4472C4', '#A5A5A5', '#ED7D31', '#70AD47']

# ==================== 创建画布 ====================
fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))

categories = ['上游', '中游', '下游']
datasets = [upstream, midstream, downstream]

# ==================== 绘制三个饼图 ====================
for idx, (ax, data, title) in enumerate(zip(axes, datasets, categories)):
    # 突出显示当前产业链中权重最大的特征
    max_idx = np.argmax(data)
    explode = [0.05 if i == max_idx else 0 for i in range(len(data))]

    wedges, texts, autotexts = ax.pie(
        data,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        startangle=90,
        pctdistance=0.6,
        textprops={'fontsize': 14}
    )

    # 百分比文字样式：白色、粗体
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(9)
        autotext.set_weight('bold')

    ax.set_title(title, fontsize=14, pad=15)

# ==================== 总标题与图例 ====================
fig.suptitle('随机森林特征重要性的产业链异质性', fontsize=24, y=1.02)

fig.legend(
    wedges, labels,
    title="特征变量",
    loc="lower center",
    ncol=4,
    bbox_to_anchor=(0.5, -0.05),
    fontsize=10
)

# ==================== 保存与显示 ====================
plt.tight_layout()
plt.savefig('rf_importance_pie.png', dpi=300, bbox_inches='tight')
plt.show()