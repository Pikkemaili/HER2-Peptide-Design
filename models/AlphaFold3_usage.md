# AlphaFold2 模型调用说明

## 模型信息
- 名称：AlphaFold2 (Colab网页端)
- 版本：Colab Notebook (AlphaFold2.ipynb)
- 来源：DeepMind / ColabFold
- 访问日期：2026-09-09

## 调用方式
通过 Google Colab 网页界面在线调用，未部署本地权重，未进行训练或微调。

## 输入输出
- 输入：单字母氨基酸序列（7肽）。
- 输出：`.pdb` 结构文件、pLDDT 图、PAE 图、原始 `.json` 评分文件。

## 已知局限
- 短肽高度柔性，pLDDT 可能偏低，属正常现象。
- 预测构象不直接代表结合亲和力，需结合 HPEPDOCK 对接打分综合评估。

## 本项目贡献
将 AlphaFold2 用于 HER2 靶向多肽变体构象预测，结合 RMSD 分析，发现了比文献 L5 位点结构更刚性的 L6 和 L7 变体，为后续多肽药物设计提供新思路。
