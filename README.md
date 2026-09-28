# HER2靶向多肽的计算设计与筛选

## 一、项目说明
本项目属于赛道一：AI大分子与多肽药物设计。
基于文献报道的 HER2 介导溶酶体降解策略，聚焦 HER2 靶向多肽 LTVSPWY 及其丙氨酸扫描变体。
使用 AlphaFold Server 预测多肽三维构象，并使用 HPEPDOCK 2.0 与 HER2 胞外域（PDB: 6BGT）进行分子对接，
筛选潜在订书肽修饰位点，为后续靶向降解分子设计提供依据。

## 二、使用工具
- AlphaFold Server（AlphaFold 3），在线版，访问日期：2026-09-28
- HPEPDOCK 2.0，在线版，访问日期：2026-09-28
- PyMOL，版本：未使用

## 三、运行环境
本项目核心计算使用在线平台，无需本地 GPU。
运行 `predict.py` 需要：
- Python 3.10 或以上
- pandas
- openpyxl

依赖文件见 `requirements.txt`。

## 四、运行命令
```bash
pip install -r requirements.txt
python predict.py
