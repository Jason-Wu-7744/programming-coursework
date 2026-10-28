# 金融工程导论

[English](README.md) | [中文](README.zh-CN.md)

四次作业、四份 Python 脚本均已收录，内容涵盖期货套保、期权定价与隐含波动率计算。

## 作业目录

| 作业 | 主题 | 代码 |
| --- | --- | --- |
| [01](assignment-01/README.zh-CN.md) | 股指期货套期保值 | [sample_01.py](assignment-01/sample_01.py) |
| [02](assignment-02/README.zh-CN.md) | 国债期货久期套保 | [sample_02.py](assignment-02/sample_02.py) |
| [03](assignment-03/README.zh-CN.md) | BSM 期权价格敏感性 | [sample_03.py](assignment-03/sample_03.py) |
| [04](assignment-04/README.zh-CN.md) | 隐含波动率微笑 | [sample_04.py](assignment-04/sample_04.py) |

## 图表成果

### 股票组合与股指期货

![股票组合及四类股指期货的累计对数收益](assets/figures/portfolio-cumulative-log-returns.jpg)

五条累计对数收益曲线对照股票组合与 IF、IH、IC、IM 股指期货。[对应代码](assignment-01/sample_01.py)

### 隐含波动率微笑

![不同行权价下的看涨与看跌期权隐含波动率](assets/figures/implied-volatility-smile-may-2026.jpg)

按行权价反解 BSM 定价公式，展示5月到期看涨与看跌期权的隐含波动率曲线。[对应代码](assignment-04/sample_04.py)

### 期权价格敏感性

![标的现价变化时的BSM看涨与看跌期权价格](assets/figures/bsm-option-price-vs-spot.jpg)

固定其他参数，比较看涨与看跌期权价格随标的现价的变化。[对应代码](assignment-03/sample_03.py)
