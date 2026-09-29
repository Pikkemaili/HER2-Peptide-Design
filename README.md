# HER2靶向多肽的计算设计与筛选

## 一、项目说明
本项目属于赛道一：AI大分子与多肽药物设计。
基于文献报道的 HER2 介导溶酶体降解策略，聚焦 HER2 靶向多肽 LTVSPWY 及其丙氨酸扫描变体。
使用 AlphaFold Server 预测多肽三维构象，并使用 HPEPDOCK 2.0 与 HER2 胞外域（PDB: 6BGT）进行分子对接，
筛选潜在订书肽修饰位点，为后续靶向降解分子设计提供依据。

## 二、使用工具
- AlphaFold Server：输入为单链7肽序列，MSA默认，Copies=1，输出为model_0.cif及summary_confidences.json。
- HPEPDOCK 2.0：受体为6BGT.pdb（未经去水/去配体处理，直接使用），肽段输入为FASTA序列，其余参数默认。
- PyMOL，版本：未使用

## 三、候选筛选与排序规则
1. 首先通过 AlphaFold 3 预测 8 条候选肽的结构，计算 pLDDT 局部置信度。
2. 使用 PyMOL 将 L1-L7 与原始 L 肽进行结构叠合，计算 RMSD，评估构象变化程度。
3. 由于 HPEPDOCK 计算资源有限，在初步结构筛选后，选取原始肽 L 以及构象变化最显著且 pLDDT 最高的 L5 进入 HPEPDOCK 分子对接复筛。
4. 其余候选（L1-L4, L6-L7）未进行对接，在结果表中记为“-”，不参与最终打分排序。
5. 最终排序以 HPEPDOCK 对接打分（负值越大结合越强）为准，L5（-198.400）优于 L（-185.682）。

## 四、运行环境
本项目核心计算使用在线平台，无需本地 GPU。
运行 `predict.py` 需要：
- Python 3.10 或以上
- pandas
- openpyxl

依赖文件见 `requirements.txt`。

## 五、运行命令
```bash
pip install -r requirements.txt
python predict.py
