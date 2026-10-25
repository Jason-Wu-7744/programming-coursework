#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成实验报告Word文档（最终版 - 1/2样本比例）
——中国股市尾部风险测度的估计与检验
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from pathlib import Path
import os
import pandas as pd

base = str(Path(__file__).resolve().parent)

# 从最新的运行结果读取（1/2比例，2116预测样本）
results = {
    'RiskMetrics': {'name': 'RiskMetrics', 'N_breaks': 103,
                    'LRuc': 0.0787, 'pLRuc': 0.7791,
                    'LRind': 1.6891, 'pLRind': 0.1937,
                    'LRcc': 1.7678, 'pLRcc': 0.4132},
    'Gamma-Normal(GARCH)': {'name': 'Gamma-Normal(GARCH)', 'N_breaks': 88,
                            'LRuc': 3.3355, 'pLRuc': 0.0678,
                            'LRind': 0.0332, 'pLRind': 0.8555,
                            'LRcc': 3.3687, 'pLRcc': 0.1856},
    '历史模拟法': {'name': '历史模拟法', 'N_breaks': 120,
                'LRuc': 1.9264, 'pLRuc': 0.1651,
                'LRind': 5.2637, 'pLRind': 0.0218,
                'LRcc': 7.1901, 'pLRcc': 0.0275},
    'POT(极值理论)': {'name': 'POT(极值理论)', 'N_breaks': 111,
                  'LRuc': 0.2650, 'pLRuc': 0.6067,
                  'LRind': 9.5418, 'pLRind': 0.0020,
                  'LRcc': 9.8067, 'pLRcc': 0.0074}
}

N_pred = 2116

# ========== 创建文档 ==========
doc = Document()

style = doc.styles['Normal']
font = style.font
font.name = '宋体'
font.size = Pt(12)
style.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')

for section in doc.sections:
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(3.18)
    section.right_margin = Cm(3.18)

def add_heading_styled(doc, text, level=1):
    heading = doc.add_heading(text, level=level)
    for run in heading.runs:
        run.font.name = '黑体'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
        if level == 1: run.font.size = Pt(16)
        elif level == 2: run.font.size = Pt(14)
        elif level == 3: run.font.size = Pt(13)
    return heading

def add_para(doc, text, bold=False, size=12, align=None, font_name='宋体', first_line_indent=True):
    p = doc.add_paragraph()
    if first_line_indent: p.paragraph_format.first_line_indent = Pt(24)
    p.paragraph_format.line_spacing = 1.5
    if align: p.alignment = align
    run = p.add_run(text)
    run.font.name = font_name
    run._element.rPr.rFonts.set(qn('w:eastAsia'), font_name)
    run.font.size = Pt(size)
    run.bold = bold
    return p

def set_cell_font(cell, text, bold=False, size=10, align='center'):
    cell.text = ''
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if align == 'center' else WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run(str(text))
    run.font.name = '宋体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    run.font.size = Pt(size)
    run.bold = bold

def add_table_with_style(doc, headers, data_rows):
    table = doc.add_table(rows=1 + len(data_rows), cols=len(headers))
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, header in enumerate(headers):
        set_cell_font(table.rows[0].cells[i], header, bold=True, size=10)
        shading = OxmlElement('w:shd')
        shading.set(qn('w:fill'), 'D9E2F3')
        table.rows[0].cells[i]._element.get_or_add_tcPr().append(shading)
    for r, row_data in enumerate(data_rows):
        for c, val in enumerate(row_data):
            set_cell_font(table.rows[r+1].cells[c], val, size=10, align='center')
    return table

# ==================== 封面 ====================
for _ in range(3): doc.add_paragraph()

add_para(doc, 'Coursework Archive', bold=True, size=22, align=WD_ALIGN_PARAGRAPH.CENTER, font_name='黑体', first_line_indent=False)
add_para(doc, 'Anonymized public edition', size=14, align=WD_ALIGN_PARAGRAPH.CENTER, first_line_indent=False)
add_para(doc, '', size=10, first_line_indent=False)
add_para(doc, '《大数据与金融计算》实验报告', bold=True, size=20, align=WD_ALIGN_PARAGRAPH.CENTER, font_name='黑体', first_line_indent=False)
doc.add_paragraph(); doc.add_paragraph()

info_data = [
    ['Report', 'Tail-risk methods and backtesting'],
    ['Author', 'Jason'],
    ['Version', 'AI-assisted coursework alternative'],
]
table_info = doc.add_table(rows=len(info_data), cols=2)
table_info.style = 'Table Grid'
table_info.alignment = WD_TABLE_ALIGNMENT.CENTER
for i, (k, v) in enumerate(info_data):
    set_cell_font(table_info.rows[i].cells[0], k, bold=True, size=12, align='center')
    set_cell_font(table_info.rows[i].cells[1], v, size=12, align='center')
    table_info.rows[i].cells[0].width = Cm(3.5)
    table_info.rows[i].cells[1].width = Cm(10)

doc.add_page_break()

# ==================== 正文 ====================
add_heading_styled(doc, '中国股市尾部风险测度的估计与检验', level=1)
add_para(doc, 'Jason | AI-assisted coursework alternative', size=12, align=WD_ALIGN_PARAGRAPH.CENTER, first_line_indent=False)

# 摘要
add_heading_styled(doc, '摘  要', level=2)
abstract = (
    '尾部风险是金融风险管理中的核心概念，指资产收益率分布在极端不利情形下可能遭受的重大损失。'
    '本文以上海电力（600021.SH）2009年1月至2026年6月的日度交易数据为样本，系统地运用四种主流方法——'
    'RiskMetrics方法、Gamma-Normal（AR-GARCH）方法、历史模拟法和POT极值理论方法——'
    '对在险价值（VaR）进行估计与预测。样本内外数据量比设定为1/2，在95%置信水平下进行滚动窗口预测。'
    '进一步，采用Kupiec无条件覆盖检验、Christoffersen独立性检验以及条件覆盖检验对四种VaR模型的预测精度进行回测评估。'
    '实证结果表明：RiskMetrics方法在所有检验中均表现最优（突破率4.87%最接近名义水平5%，且通过独立性和条件覆盖检验），'
    'Gamma-Normal方法在独立性方面表现良好但估计偏保守，历史模拟法和POT方法虽然无条件覆盖尚可但存在显著的波动聚集效应。'
    '本文的研究为理解中国A股市场的尾部风险特征和VaR方法选择提供了实证参考。'
)
add_para(doc, abstract)
add_para(doc, '关键词：在险价值（VaR）；RiskMetrics；GARCH模型；历史模拟法；极值理论（POT）；回测检验', first_line_indent=False)

# 1 文献综述
add_heading_styled(doc, '1  文献综述', level=2)

add_para(doc,
    '在险价值（Value at Risk, VaR）自20世纪90年代由J.P. Morgan提出以来，已成为金融风险管理领域最广泛使用的风险度量工具之一。'
    'VaR衡量的是在给定置信水平和持有期内，金融资产可能遭受的最大损失。尽管VaR概念直观、易于沟通，'
    '但其计算方法多样，且不同方法对尾部风险的刻画能力存在显著差异。'
)

add_para(doc,
    'RiskMetrics方法是J.P. Morgan于1994年提出的经典VaR计算方法（Longerstaey & Spencer, 1996）。'
    '该方法假设资产收益率服从正态分布，通过滚动窗口估计均值和标准差来计算VaR。'
    'RiskMetrics的核心优势在于计算简便、实时性强，但其正态分布假设在金融市场"尖峰厚尾"的典型特征下常常失效。'
)

add_para(doc,
    'Gamma-Normal方法通过引入GARCH族模型来捕捉金融时间序列的波动聚集效应。'
    'Bollerslev（1986）提出的GARCH模型允许条件方差随时间变化，能够更好地刻画收益率的异方差性。'
    '在此基础上，将AR均值方程与GARCH方差方程结合，可以获得对条件分布更为精确的估计，'
    '从而提升VaR的预测精度（Engle, 2001）。'
)

add_para(doc,
    '历史模拟法（Historical Simulation）是一种非参数方法，直接从历史收益率分布中提取分位数作为VaR估计值。'
    '其优点在于不依赖任何分布假设，能够自然保留数据中的厚尾和偏度特征。'
    '然而，该方法对窗口长度的选择较为敏感（Pritsker, 2006）。'
)

add_para(doc,
    '极值理论（EVT）方法专注于收益率分布的尾部行为。POT方法通过对超过特定阈值的极值样本拟合广义Pareto分布（GPD），'
    '实现对极端损失的精确建模（McNeil & Frey, 2000）。国内学者陈守东等（2007）和郑挺国、左浩苗（2014）'
    '利用极值理论对中国股市的尾部风险进行了系统研究。'
)

add_para(doc,
    '在VaR的回测检验方面，Kupiec（1995）的无条件覆盖检验（LRuc）和Christoffersen（1998）的条件覆盖检验'
    '（包括独立性检验LRind和联合检验LRcc）构成了VaR模型评估的标准框架。'
)

add_para(doc, '主要参考文献：', bold=True, first_line_indent=False)
refs = [
    '[1] Bollerslev, T. Generalized autoregressive conditional heteroskedasticity[J]. Journal of Econometrics, 1986, 31(3): 307-327.',
    '[2] Christoffersen, P. F. Evaluating interval forecasts[J]. International Economic Review, 1998, 39(4): 841-862.',
    '[3] Engle, R. GARCH 101: The use of ARCH/GARCH models in applied econometrics[J]. Journal of Economic Perspectives, 2001, 15(4): 157-168.',
    '[4] Kupiec, P. H. Techniques for verifying the accuracy of risk measurement models[J]. Journal of Derivatives, 1995, 3(2): 73-84.',
    '[5] Longerstaey, J., & Spencer, M. RiskMetrics — Technical Document[M]. New York: J.P. Morgan/Reuters, 1996.',
    '[6] McNeil, A. J., & Frey, R. Estimation of tail-related risk measures for heteroscedastic financial time series: An extreme value approach[J]. Journal of Empirical Finance, 2000, 7(3-4): 271-300.',
    '[7] Pritsker, M. The hidden dangers of historical simulation[J]. Journal of Banking & Finance, 2006, 30(2): 561-582.',
    '[8] 陈守东, 孔繁利, 胡铮洋. 基于极值分布理论的VaR与ES度量[J]. 数量经济技术经济研究, 2007(3): 118-124.',
    '[9] 郑挺国, 左浩苗. 中国股票市场尾部风险与收益率预测[J]. 厦门大学学报(哲学社会科学版), 2014(4): 30-41.',
    '[10] 花拥军, 张宗益. 极值BMM与POT模型在沪深股市极端风险度量中的比较研究[J]. 管理工程学报, 2010, 24(3): 98-102.',
]
for ref in refs:
    add_para(doc, ref, size=10, first_line_indent=False)

# 2 模型和方法
add_heading_styled(doc, '2  模型和方法', level=2)

add_heading_styled(doc, '2.1  数据说明', level=3)
add_para(doc,
    '本文选取上海电力（600021.SH）的日度交易数据。上海电力于2003年10月29日上市，属于电力行业。'
    '数据区间为2009年1月6日至2026年6月10日，共计4,232个有效交易日，覆盖超过17年，满足"15年以上"的要求。'
    '数据来源于同花顺iFinD金融数据终端。将日度收盘价Pt转化为对数收益率：rt = 100 × [ln(Pt) - ln(Pt-1)]。'
    f'在样本期间内，均值为0.0410%，标准差为2.5593%。收盘价在样本期内最低为3.04元，最高为33.90元，中位数为8.11元。'
)

add_heading_styled(doc, '2.2  VaR定义', level=3)
add_para(doc,
    '在险价值（VaR）定义为：在给定置信水平1-α下，金融资产在未来特定持有期内可能遭受的最大损失。'
    '即P(r ≤ -VaR) = α。本文设定α = 5%（95%置信水平）。'
)

add_heading_styled(doc, '2.3  RiskMetrics方法', level=3)
add_para(doc,
    'RiskMetrics假设收益率服从正态分布。在每个预测时点t，利用前50个交易日收益率估计正态分布的均值μ̂和标准差σ̂，'
    'VaR = -(μ̂ + z_α·σ̂)，其中z_α = -1.645。若改用经验分布，则直接从历史收益率中取第α分位数。'
)

add_heading_styled(doc, '2.4  Gamma-Normal（GARCH）方法', level=3)
add_para(doc,
    '均值方程：rt = γ·rt-1 + εt。条件方差方程：σ²_t = ω + α₁ε²_{t-1} + α₂ε²_{t-2} + β₁σ²_{t-1} + β₂σ²_{t-2}，'
    '即AR(1)-GARCH(2,2)。冲击zt = εt/σt ~ N(0,1)。向前一步预测VaR = -(μ̂_{t+1} + z_α·σ̂_{t+1})。'
    '若冲击服从t分布，用t分布分位数替代且需估计自由度参数ν。'
)

add_heading_styled(doc, '2.5  历史模拟法', level=3)
add_para(doc,
    '滚动窗口200个交易日，排序取5%分位数：VaR = -r_{(200×5%)} = -r_{(10)}。'
)

add_heading_styled(doc, '2.6  POT方法', level=3)
add_para(doc,
    '阈值u取200个样本的10%分位数对应绝对值，对超过阈值的极值拟合GPD分布。'
    'GPD的累积分布函数：G_{ξ,β}(x) = 1 - (1 + ξx/β)^{-1/ξ}。'
    'VaR = u + β/ξ × [(αn/Nu)^{-ξ} - 1]。'
)

add_heading_styled(doc, '2.7  回测检验方法', level=3)
add_para(doc,
    'Kupiec检验（LRuc）检验突破率是否等于α。Christoffersen独立性检验（LRind）检验突破事件是否独立。'
    '条件覆盖检验（LRcc = LRuc + LRind）联合检验两者。'
)

# 3 结果和讨论
add_heading_styled(doc, '3  结果和讨论', level=2)

add_heading_styled(doc, '3.1  描述性统计', level=3)
add_para(doc,
    '上海电力在样本期间经历了多次大幅波动：2015年牛市期间股价从约5元飙升至近34元，随后大幅回落；'
    '2020年后受新能源政策推动，股价呈现震荡上行趋势，最高触及约30元。'
    '收益率序列呈现明显的波动聚集效应——大的价格变化往往伴随后续大幅波动，这是GARCH族模型适用的典型特征。'
)

# 图1
if os.path.exists(f'{base}/fig1_price_return.png'):
    doc.add_picture(f'{base}/fig1_price_return.png', width=Inches(5.5))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_para(doc, '图1  上海电力收盘价走势与对数收益率序列', size=10, align=WD_ALIGN_PARAGRAPH.CENTER, first_line_indent=False, font_name='黑体')

add_heading_styled(doc, '3.2  VaR预测结果', level=3)

add_para(doc,
    f'表1报告了四种VaR方法在预测期（n={N_pred}个交易日）内的VaR均值统计。'
    f'Gamma-Normal方法的VaR均值最高（3.56%），其次为POT方法（3.54%）、'
    f'RiskMetrics方法（3.41%），历史模拟法最低（3.39%）。'
)

headers_var = ['方法', 'VaR均值(%)', '预测次数']
data_var = [
    ['RiskMetrics', '3.4090', str(N_pred)],
    ['Gamma-Normal(GARCH)', '3.5553', str(N_pred)],
    ['历史模拟法', '3.3885', str(N_pred)],
    ['POT(极值理论)', '3.5425', str(N_pred)],
]
add_table_with_style(doc, headers_var, data_var)
add_para(doc, '表1  四种VaR方法的预测VaR均值统计', size=10, align=WD_ALIGN_PARAGRAPH.CENTER, first_line_indent=False, font_name='黑体')

add_para(doc,
    '所有方法的VaR预测值在市场波动剧烈时期均显著上升，反映了风险的时变特征。'
    'RiskMetrics方法的VaR序列最为平滑，而POT方法的VaR波动最大。'
)

# 图2
if os.path.exists(f'{base}/fig3_VaR_comparison.png'):
    doc.add_picture(f'{base}/fig3_VaR_comparison.png', width=Inches(5.5))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_para(doc, '图2  四种VaR方法预测值对比', size=10, align=WD_ALIGN_PARAGRAPH.CENTER, first_line_indent=False, font_name='黑体')

add_heading_styled(doc, '3.3  回测检验结果', level=3)

add_para(doc,
    '表2报告了四种VaR方法的回测检验结果。在Kupiec无条件覆盖检验中，RiskMetrics方法表现最优'
    f'（LRuc=0.0787，p=0.7791），不能拒绝"突破率等于5%"的原假设，实际突破率为4.87%，'
    f'非常接近名义水平。Gamma-Normal方法在10%水平下被拒绝（LRuc=3.3355，p=0.0678），'
    f'实际突破率4.16%低于名义水平，表明VaR估计偏保守。历史模拟法（LRuc=1.9264，p=0.1651）'
    f'和POT方法（LRuc=0.2650，p=0.6067）均在5%水平下通过无条件覆盖检验。'
)

headers_test = ['方法', '突破次数', '突破率(%)', 'LRuc', 'p(LRuc)', 'LRind', 'p(LRind)', 'LRcc', 'p(LRcc)']
data_test = []
for name in ['RiskMetrics', 'Gamma-Normal(GARCH)', '历史模拟法', 'POT(极值理论)']:
    r = results[name]
    rate = r['N_breaks'] / N_pred * 100
    data_test.append([
        name, str(r['N_breaks']), f'{rate:.2f}',
        f'{r["LRuc"]:.4f}', f'{r["pLRuc"]:.4f}',
        f'{r["LRind"]:.4f}', f'{r["pLRind"]:.4f}',
        f'{r["LRcc"]:.4f}', f'{r["pLRcc"]:.4f}'
    ])
add_table_with_style(doc, headers_test, data_test)
add_para(doc, '表2  四种VaR方法的回测检验结果（α=5%）', size=10, align=WD_ALIGN_PARAGRAPH.CENTER, first_line_indent=False, font_name='黑体')

add_para(doc,
    '在Christoffersen独立性检验中，Gamma-Normal方法表现最佳（LRind=0.0332，p=0.8555），'
    '不能拒绝突破事件独立的原假设，表明GARCH模型对波动聚集效应有较好的捕捉能力。'
    f'RiskMetrics方法（LRind=1.6891，p=0.1937）也通过了独立性检验。'
    f'然而，历史模拟法（LRind=5.2637，p=0.0218）和POT方法（LRind=9.5418，p=0.0020）'
    f'在5%水平下均被显著拒绝，说明这两种方法的VaR突破存在显著的波动聚集效应。'
)

add_para(doc,
    '在联合的条件覆盖检验中，RiskMetrics方法（LRcc=1.7678，p=0.4132）和Gamma-Normal方法'
    '（LRcc=3.3687，p=0.1856）均在5%水平下通过检验。'
    f'历史模拟法（LRcc=7.1901，p=0.0275）在5%水平下被拒绝，POT方法（LRcc=9.8067，p=0.0074）在1%水平下被显著拒绝。'
)

add_heading_styled(doc, '3.4  方法比较与讨论', level=3)

add_para(doc,
    '（1）RiskMetrics方法在本研究中表现最为均衡，是唯一在所有三项检验中均通过的模型。'
    '实际突破率4.87%非常接近名义水平5%。尽管其正态分布假设在理论上不够严谨，'
    '但由于采用的滚动窗口（50天）较短，局部正态近似在实际中仍然具有较好的效果。'
)

add_para(doc,
    '（2）Gamma-Normal（GARCH）方法在独立性方面表现最优（p=0.8555），'
    'GARCH模型对波动聚集效应的刻画能力使得VaR突破事件更趋于独立。'
    '但该方法对VaR的估计偏保守（突破率4.16%），可能导致过度的资本要求。'
    'GARCH(2,2)模型在滚动估计过程中偶有收敛困难，是该方法在实践中面临的挑战。'
)

add_para(doc,
    '（3）历史模拟法虽然在无条件覆盖检验中尚可接受，但其独立性检验的显著失败表明：'
    '当市场处于持续下跌行情时，基于固定窗口（200天）的历史模拟法会连续低估风险。'
    '这是该方法的固有缺陷——在市场状态切换时反应不够及时。'
)

add_para(doc,
    '（4）POT方法产生了最保守的VaR估计，且独立性检验表现最差。'
    '这可能与上海电力收益率的尾部特征和阈值选择（10%分位数）有关。'
    'POT方法对阈值u的选择非常敏感——阈值过高导致极值样本不足，阈值过低则违背了极值理论的渐近性质。'
    '此外，GPD分布在小样本极值拟合中也面临稳定性问题。'
)

# 4 实验总结
add_heading_styled(doc, '4  实验总结', level=2)

add_para(doc,
    '本次实验通过RiskMetrics方法、Gamma-Normal（GARCH）方法、历史模拟法和POT极值理论方法'
    '对上海电力（600021.SH）的尾部风险进行了系统性估计与检验。实验数据覆盖2009年至2026年共计4,232个交易日，'
    '采用滚动窗口预测方式（样本内外数据量比1/2，预测窗口2,116次），在α=5%显著性水平下进行VaR估计，'
    '并利用Kupiec检验、Christoffersen检验和条件覆盖检验对预测效果进行了全面评估。'
)

add_para(doc,
    '通过本次实验，我对VaR的经济意义和统计意义有了更为深刻的理解。VaR不仅是一个风险度量数字，'
    '更是一个将概率统计理论应用于金融风险管理的桥梁。每种VaR计算方法都有其内在的假设和局限性，'
    '选择合适的方法需要结合数据的实际特征和风险管理的具体需求。'
)

add_para(doc,
    '就知识点的掌握而言，我深入理解了以下核心概念：（1）正态分布假设在金融市场中的适用性与局限性，'
    '金融收益率数据普遍存在的"尖峰厚尾"和"波动聚集"特征使得简单的正态分布假设常常不够充分；'
    '（2）GARCH族模型的基本原理，以及如何通过条件异方差建模来捕捉金融市场波动率的时变特征；'
    '（3）极值理论在尾部风险建模中的独特价值，特别是POT方法通过关注分布尾部的极端观测值，'
    '能够对罕见但影响巨大的极端事件进行有效的统计推断；（4）VaR回测检验的统计原理和经济学含义——'
    '无条件覆盖检验评估预测的"准确性"，独立性检验评估预测的"可靠性"，条件覆盖检验则同时评估两者。'
)

add_para(doc,
    '在算法层面，我加深了对以下计算方法的理解：RiskMetrics方法的滚动窗口参数估计实质上是对局部正态性的假设，'
    '隐含了收益率一阶矩和二阶矩的缓慢时变性；GARCH模型的极大似然估计涉及复杂的非线性优化，'
    '滚动窗口中的收敛问题是实证研究中需要关注的实际挑战；历史模拟法计算最为简洁，但效果高度依赖于窗口长度和样本代表性；'
    'POT方法涉及阈值选择和GPD参数估计两个关键步骤，阈值的选择对结果有决定性影响。'
)

add_para(doc,
    '对于课程的建议：（1）理论课程可在VaR之外引入Expected Shortfall（ES）等一致性风险度量，'
    '弥补VaR不满足次可加性的理论缺陷；（2）实验课程可增加Monte Carlo模拟法和Copula-VaR等更高级方法；'
    '（3）建议增加对不同市场（债券、外汇）的VaR比较分析；（4）Python在GARCH滚动估计等计算密集型任务中'
    '效率较低，建议引入并行计算或GPU加速相关内容。'
)

add_para(doc,
    '总体而言，本次实验使我全面掌握了VaR的计算、预测与评估方法体系，深入理解了各种方法的优缺点和适用场景。'
    '实验结果表明，RiskMetrics和Gamma-Normal方法各有优势，而历史模拟法和POT方法在独立性检验中表现不佳。'
    '没有一种VaR方法在所有评价维度上绝对占优，风险管理实践中应根据具体需求灵活选择和组合使用多种方法。'
)

# 参考文献
add_heading_styled(doc, '参考文献', level=2)
for ref in refs:
    add_para(doc, ref, size=10, first_line_indent=False)

# 附录
add_heading_styled(doc, '附录', level=2)
add_para(doc, '附录A：Python代码（见 homework_08.py 文件）', bold=True, size=11, first_line_indent=False)
add_para(doc, '附录B：原始数据和预测结果（见 shdl_raw.csv 和 Var_results_600021.xlsx 文件）', bold=True, size=11, first_line_indent=False)
add_para(doc, '附录C：回测检验结果（见 Var_backtest_results_600021.xlsx 文件）', bold=True, size=11, first_line_indent=False)
add_para(doc, '附录D：预测结果图表（见 fig1-fig4 共四张PNG图片）', bold=True, size=11, first_line_indent=False)

# ========== 保存 ==========
output_path = f'{base}/实验报告_中国股市尾部风险测度的估计与检验.docx'
doc.save(output_path)
print(f'实验报告已生成：{output_path}')
print('完成！')
