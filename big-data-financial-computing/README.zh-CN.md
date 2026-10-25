# 大数据与金融计算

[English](README.md) | [中文](README.zh-CN.md)

本课程是 [Programming Coursework Portfolio](../README.zh-CN.md) 的一部分，按每次作业组织。目前公开 29 个课程 Python 文件，不含检查工具。全部作业目录保留；部分来源待确认的参考实现暂不公开。

<!-- gallery:start -->
## 精选图表

以下为原作业目录中保存的历史 Matplotlib 输出，保留原图标签；本次未在代码审计后重新生成。图表对应代码见各图下方，验证范围见[质量说明](QUALITY.zh-CN.md)。

### 七种采样尺度下的收益率经验分布

![七种采样尺度下的收益率经验分布](assets/figures/multiscale-return-density.jpg)

在对数密度坐标上，以不同线型和标记对照1分钟至240分钟共七种采样尺度的收益率经验分布。

[作业01 · 收益率分布](assignment-01/homework_01.py)

### 因子模型下的行业多空权重

![因子模型下的行业多空权重](assets/figures/factor-model-industry-weights.jpg)

展示2018—2021年因子协方差估计下的行业配置变化；负权重为空头敞口，属于未施加做空约束的配置练习。图例依次为信息、公用、医药、可选、工业、材料、消费、能源、通信和金融。

[作业05 · 协方差与组合配置](assignment-05/homework_05.py)

### GARCH(1,1) 模拟与条件波动率

![GARCH(1,1) 模拟与条件波动率](assets/figures/garch-simulation-comparison.jpg)

按观测序号对照模拟收益率（绿）、条件波动率（橙）和历史指数收益率（蓝）；绿线为随机模拟路径。

[作业07 · 条件波动率](assignment-07/homework_07_01.py)

<!-- gallery:end -->


## 作业目录

| 作业 | 内容 |
| --- | --- |
| [01](assignment-01/README.zh-CN.md) | 收益率分布 |
| [02](assignment-02/README.zh-CN.md) | CAPM 与收益率规律 |
| [03](assignment-03/README.zh-CN.md) | 三因子与横截面检验 |
| [04](assignment-04/README.zh-CN.md) | 收益率可预测性 |
| [05](assignment-05/README.zh-CN.md) | 协方差估计与组合配置 |
| [06](assignment-06/README.zh-CN.md) | 金融网络数据采集 |
| [07](assignment-07/README.zh-CN.md) | 条件波动率 |
| [08](assignment-08/README.zh-CN.md) | VaR 与回测 |

## 环境与数据

在本课程目录安装依赖：

```bash
python -m pip install -r requirements.txt
```

再进入相应作业目录运行具体脚本。输入文件、字段、版本标记和原有问题见各作业说明。外部数据需另行获得授权；这里不分发数据库原表、教师课件、原题、答题模板、私人报告或来源未核实的课堂参考代码。

## 归属与验证

署名使用 Jason。课程指定任务、AI 辅助版本和已知限制按实际情况标注。后续定点修复及十组合成测试见[仓库审计记录](../AUDIT.zh-CN.md)。

Python 语法、双语文档配对和本地链接已检查；部分数值函数通过隔离合成测试，历史实证结果未全面复算。详见[质量说明](QUALITY.zh-CN.md)与[英文课程说明](README.md)。公开可见不等于授予第三方资料的再分发许可；本仓库尚未选择开源许可证。
