# 金融数值分析

[English](README.md) | [中文](README.zh-CN.md)

本课程是 [Programming Coursework Portfolio](../README.zh-CN.md) 的一部分，按每次作业组织。目前公开 100 个课程 Python 文件，不含检查工具。全部作业目录保留；部分来源待确认的参考实现暂不公开。

<!-- gallery:start -->
## 精选图表

以下为原作业目录中保存的历史 Matplotlib 输出，保留原图标签；本次未在代码审计后重新生成。图表对应代码见各图下方，验证范围见[质量说明](QUALITY.zh-CN.md)。

### Monte Carlo 价格路径

![Monte Carlo 价格路径](assets/figures/historical-monte-carlo-paths.jpg)

黑线为历史价格，五条彩线为原模拟练习生成的随机样本路径。

[作业05 · 模拟替代版本](assignment-05/extra/exercise-06_monte_carlo_alternative.py)

### 日内价格与成交量双面板

![日内价格与成交量双面板](assets/figures/intraday-price-volume.jpg)

价格与成交量双面板对齐时间轴，区分上午和下午交易，并标记前收盘价。p 为价格，v 为成交量，t 为时间。

[作业04 · 金融可视化](assignment-04/exercise-05.py)

### 三种差分方法的谱曲线对照

![三种差分方法的谱曲线对照](assets/figures/finite-difference-spectrum.jpg)

对给定的 q 与 τ(q) 表进行向前、向后和中心差分。横轴为 α = dτ(q)/dq，纵轴为 f(α) = qα − τ(q)。

[作业13 · 数值微分](assignment-13/exercise-01.py)

<!-- gallery:end -->


## 作业目录

| 作业 | 内容 |
| --- | --- |
| [01](assignment-01/README.zh-CN.md) | Python 数据类型 |
| [02](assignment-02/README.zh-CN.md) | 控制流程与函数 |
| [03](assignment-03/README.zh-CN.md) | NumPy 与金融数组 |
| [04](assignment-04/README.zh-CN.md) | Matplotlib 与金融图形 |
| [05](assignment-05/README.zh-CN.md) | Pandas 与几何布朗运动 |
| [06](assignment-06/README.zh-CN.md) | 数值求根与交易间隔 |
| [07](assignment-07/README.zh-CN.md) | 不动点与最小二乘 |
| [08](assignment-08/README.zh-CN.md) | 直接求解与金融模型拟合 |
| [09](assignment-09/README.zh-CN.md) | 迭代求解与三因子回归 |
| [10](assignment-10/README.zh-CN.md) | 多项式插值 |
| [11](assignment-11/README.zh-CN.md) | 幂法与金融网络 |
| [12](assignment-12/README.zh-CN.md) | 数值积分与分布 |
| [13](assignment-13/README.zh-CN.md) | 数值微分与随机模拟 |
| [14](assignment-14/README.zh-CN.md) | 常微分方程 |

## 环境与数据

在本课程目录安装依赖：

```bash
python -m pip install -r requirements.txt
```

再进入相应作业目录运行具体脚本。输入文件、字段、版本标记和原有问题见各作业说明。外部数据需另行获得授权；这里不分发数据库原表、教师课件、原题、答题模板、私人报告或来源未核实的课堂参考代码。

## 归属与验证

署名使用 Jason。课程指定任务、AI 辅助版本和已知限制按实际情况标注。后续定点修复及十组合成测试见[仓库审计记录](../AUDIT.zh-CN.md)。

Python 语法、双语文档配对和本地链接已检查；部分数值函数通过隔离合成测试，历史实证结果未全面复算。详见[质量说明](QUALITY.zh-CN.md)与[英文课程说明](README.md)。公开可见不等于授予第三方资料的再分发许可；本仓库尚未选择开源许可证。
