# programming作业成果展示

[English](README.md) | 中文

**Jason 的 Python 课程作业归档**，涵盖「金融数值分析」「金融工程导论」「大数据与金融计算」。按课程和作业次序保留全部 **26 次作业目录**，展示学习内容、代码实现和不同版本，不再精选少数作业。

*A Python coursework archive by Jason, covering numerical analysis, financial engineering, and financial computing. All assignment folders are retained, with documented versions, input requirements, and limitations. External datasets and teaching materials are excluded.*

## 课程总览

| 课程 | 作业目录 | 当前公开 Python 作业文件 | 学习内容 |
| --- | ---: | ---: | --- |
| [金融数值分析](financial-numerical-analysis/README.md) | 14 | 100 | Python 与科学计算基础、数值方法及金融计算练习 |
| [金融工程导论](financial-engineering/README.md) | 4 | 4 | 股指与国债期货套保、BSM 定价及隐含波动率 |
| [大数据与金融计算](big-data-financial-computing/README.md) | 8 | 29 | 收益分布、资产定价检验、组合配置、波动率和风险分析 |
| 合计 | 26 | 133 | 文件数不包含各课程的归档检查脚本 |

每次作业的 README 说明公开脚本、所需数据、运行目录和已知问题。下表概述课程作业主题；具体可用实现及暂未公开的条目，以各作业说明为准。

## 金融数值分析

从 Python 数据结构、NumPy、Pandas 和绘图练习，逐步进入求根、回归、线性方程组、插值、特征值、积分、微分和常微分方程。金融应用包括收益与波动率估计、股票价格模拟、因子回归及金融网络计算。

| 作业 | 主题 | 内容概览 |
| --- | --- | --- |
| [01](financial-numerical-analysis/assignment-01/README.md) | Python 数据类型 | 字符串与容器、金融算术、比较和序列化 |
| [02](financial-numerical-analysis/assignment-02/README.md) | 控制流程与函数 | 条件、循环、枚举和蒙特卡洛期望计算 |
| [03](financial-numerical-analysis/assignment-03/README.md) | NumPy 与金融数组 | 数组操作、矩阵代数、统计量和概率分布 |
| [04](financial-numerical-analysis/assignment-04/README.md) | Matplotlib 与金融图表 | 双坐标轴、极坐标、逐笔交易和基金再投资图表 |
| [05](financial-numerical-analysis/assignment-05/README.md) | Pandas 与几何布朗运动 | 表格查询、缺失值、收益与波动率估计、价格模拟 |
| [06](financial-numerical-analysis/assignment-06/README.md) | 求根与交易间隔 | 二分、牛顿与割线方法，交易间隔分布估计 |
| [07](financial-numerical-analysis/assignment-07/README.md) | 不动点与最小二乘 | 迭代收敛、线性及多元回归、收益尾部拟合 |
| [08](financial-numerical-analysis/assignment-08/README.md) | 直接解法与金融模型拟合 | 高斯消元、LU 分解、三因子回归与 LPPLS 线性部分拟合 |
| [09](financial-numerical-analysis/assignment-09/README.md) | 迭代解法与三因子回归 | Jacobi、Gauss–Seidel 及行业指数因子估计 |
| [10](financial-numerical-analysis/assignment-10/README.md) | 多项式插值 | Lagrange 插值、Newton 差商和分期利率计算 |
| [11](financial-numerical-analysis/assignment-11/README.md) | 幂法与金融网络 | 主特征值与特征向量、收益相关性和行业中心性排序 |
| [12](financial-numerical-analysis/assignment-12/README.md) | 数值积分与分布 | 复化梯形、Simpson 方法、正态及对数正态概率计算 |
| [13](financial-numerical-analysis/assignment-13/README.md) | 数值微分与随机模拟 | 前向、后向及中心差分，几何布朗运动参数估计与模拟 |
| [14](financial-numerical-analysis/assignment-14/README.md) | 常微分方程 | Euler、梯形和二阶 Runge–Kutta 方法及应用练习 |

另见[补充练习](financial-numerical-analysis/supplementary/README.md)与[共享参考代码的公开范围说明](financial-numerical-analysis/shared/README.md)。

## 金融工程导论

围绕衍生品定价和套期保值完成四次实验，主要使用对数收益率、OLS 回归、债券现金流与久期、BSM 公式及数值求根。代码保留课程实现；作业一的回归方向问题已在对应 README 中明确记录。

| 作业 | 主题 | 内容概览 |
| --- | --- | --- |
| [01](financial-engineering/assignment-01/README.md) | 股指期货套期保值 | 比较四类股指期货、回归拟合和套保头寸计算 |
| [02](financial-engineering/assignment-02/README.md) | 国债期货久期套保 | 应计利息、全价、到期收益率、组合久期和 CTD 近似 |
| [03](financial-engineering/assignment-03/README.md) | BSM 期权价格敏感性 | 分析现价、行权价、波动率、利率和到期期限的影响 |
| [04](financial-engineering/assignment-04/README.md) | 隐含波动率微笑 | 按到期月份反解看涨与看跌期权波动率并作图 |

## 大数据与金融计算

从收益分布和资产定价回归，扩展到预测检验、协方差估计、组合配置、网络数据采集、条件波动率和尾部风险分析。主要方法包括 CAPM、Fama–French、Fama–MacBeth、ARCH/GARCH/EGARCH、VaR 及回测检验。

| 作业 | 主题 | 内容概览 |
| --- | --- | --- |
| [01](big-data-financial-computing/assignment-01/README.md) | 收益分布 | 不同采样间隔、经验分布、正态拟合与尾部特征 |
| [02](big-data-financial-computing/assignment-02/README.md) | CAPM 与收益规律 | 单资产回归、联合检验及反转与动量补充计算 |
| [03](big-data-financial-computing/assignment-03/README.md) | Fama–French 与截面检验 | 行业时序回归、规模与价值分组、Fama–MacBeth 回归 |
| [04](big-data-financial-computing/assignment-04/README.md) | 收益可预测性 | 样本内拟合、样本外预测和预测设定评估 |
| [05](big-data-financial-computing/assignment-05/README.md) | 协方差估计与组合配置 | 样本、常数、因子、收缩及 EWMA 协方差估计与权重计算 |
| [06](big-data-financial-computing/assignment-06/README.md) | 网络数据采集 | 金融网页与接口数据、文本情绪及收益关系探索 |
| [07](big-data-financial-computing/assignment-07/README.md) | 条件波动率 | ARCH、GARCH、EGARCH 估计及分布诊断 |
| [08](big-data-financial-computing/assignment-08/README.md) | VaR 与回测 | 正态、GARCH、历史及 POT 尾部风险估计与覆盖、独立性检验 |

另见[课程论文代码](big-data-financial-computing/course-paper/README.md)、[课堂练习的公开范围说明](big-data-financial-computing/classroom-exercises/README.md)和[数据访问补充练习](big-data-financial-computing/supplementary/README.md)。课程论文包含资产定价和随机森林的探索性分析，相关限制在目录内说明。

## 源代码与版本范围

保留全部作业目录及可公开的不同实现版本。内容完全相同的副本只保留一份，必要时在作业说明中交叉引用。`extra/` 保存补充或替代实现，`legacy/` 保存已识别的历史版本，`ai-assisted/` 标记已知的 AI 辅助版本；具体文件用途见各作业 README。版本标记仅反映已知信息，不能据此推断其他文件均为独立原创。

这里记录的是课程学习与作业实现。指定金融方法、模型和任务不作为原创研究成果宣称。原算法及其限制保留在档案中，整理时主要处理目录、隐私和连接配置，未将金融计算问题悄悄改写为新的答案。

教师课件、讲义、作业原题全文、教师参考或答案代码、原始报告、考试材料、IDE 缓存和压缩包均不发布。与课堂示例重合或来源尚未确认的参考代码暂不公开，对应目录保留说明；这项处理不构成对原作者身份或权属的判断。各作业的简短主题介绍为本次归档重新整理，未粘贴教师材料的大段内容。

## Python 环境与运行

整理时使用 **Python 3.12** 进行语法检查。建议使用虚拟环境，并根据所读课程安装对应依赖；历史依赖版本未完整重建，运行兼容性仍需自行验证。

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

以下路径均从仓库根目录出发。选择需要运行的课程安装依赖：

| 课程 | 依赖文件 | 安装命令 |
| --- | --- | --- |
| 金融数值分析 | [requirements.txt](financial-numerical-analysis/requirements.txt) | `python -m pip install -r "financial-numerical-analysis/requirements.txt"` |
| 金融工程导论 | [requirements.txt](financial-engineering/requirements.txt) | `python -m pip install -r "financial-engineering/requirements.txt"` |
| 大数据与金融计算 | [requirements.txt](big-data-financial-computing/requirements.txt) | `python -m pip install -r "big-data-financial-computing/requirements.txt"` |

依赖清单依据实际代码使用的库，以及数据库、Excel 读取所需的后端整理；未任意补写版本号。部分脚本需要中文字体、图形界面、可用的数据接口或额外的本地输入。

**工作目录会影响数据读取。** 金融数值分析按各作业 README，从所属 `assignment-XX/` 目录运行，即使脚本位于子目录也先查看该作业约定；金融工程导论从各自作业目录运行；大数据与金融计算通常从脚本所在目录运行，嵌套版本以其说明为准。

例如，从仓库根目录运行无需外部工作簿的期权敏感性作业：

```powershell
Set-Location "financial-engineering/assignment-03"
python sample_03.py
```

该示例只说明启动方式，不代表已完成运行验证。其他作业可能需要先准备数据，脚本也可能在工作目录生成图片或结果文件。

## 外部数据与本地配置

原始金融数据、RESSET 等数据库导出、课程数据表和研究来源的网络数据不随仓库分发。请按各作业 README 所列文件名、字段、日期、编码、单位和表结构，通过有权使用的来源自行准备。外部来源链接仅作获取与核对线索，不能保证重建原始课程快照；小型内嵌数值与课堂参数的保留情况见具体代码。

数据库访问需要私下配置。金融数值分析相关脚本使用 `FNA_DB_HOST`、`FNA_DB_PORT`、`FNA_DB_USER`、`FNA_DB_PASSWORD`、`FNA_DB_NAME` 环境变量；[配置样例](financial-numerical-analysis/.env.example)只列变量名，不包含原值，也不会自动加载。API 凭据与个人连接信息同样只在本地配置，勿提交填有真实值的环境文件或私有数据。

## 验证范围与已知限制

当前 **133 个 Python 作业文件通过语法检查**，文档相对链接也已检查。检查结果不代表端到端运行成功：未全面执行依赖导入、数据库访问、网络请求、模型估计、随机模拟或绘图，也未全面复算或独立验证金融结果、统计结论及预测表现。

各课程的具体检查与限制见：

- [金融数值分析 QUALITY.md](financial-numerical-analysis/QUALITY.md)
- [金融工程导论 QUALITY.md](financial-engineering/QUALITY.md)
- [大数据与金融计算 QUALITY.md](big-data-financial-computing/QUALITY.md)

已知问题包括部分数值算法的收敛与停止条件、数据对齐和缺失值处理、指定参数与图表口径，以及金融工程作业一的回归方向。解释结果前应先阅读对应说明，再准备数据并复核计算。源码公开本身不代表授予未声明的开源许可或外部数据再分发许可。

维护者：**Jason**。财报分析系统作为独立项目另行维护。
