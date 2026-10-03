# Model Card: AlphaFold 2 (via Colab)

## 一、模型基本信息
- **模型名称**：AlphaFold 2 (Colab 网页端)
- **版本**：AlphaFold2.ipynb (Colab Notebook)
- **来源**：DeepMind / ColabFold (https://colab.research.google.com/)
- **访问日期**：2026-09-09
- **模型类型**：蛋白质/多肽三维结构预测模型

## 二、适用范围
本项目使用 AlphaFold 2 预测 HER2 靶向多肽 LTVSPWY 及其 7 个丙氨酸扫描变体（L1-L7）的三维构象。
该模型适用于单链多肽及蛋白质复合物的结构预测。

## 三、输入与输出
- **输入**：单字母氨基酸序列（FASTA格式，7肽）。
- **输出**：
  - `.pdb` 三维结构文件（用于后续 PyMOL 分析和 HPEPDOCK 对接）
  - pLDDT 置信度图 (`.png`)，展示每个残基的局部预测置信度
  - PAE 对齐误差图 (`.png`)
  - `.json` 原始评分文件（包含 pLDDT 和 PAE 数值）

## 四、调用方式与训练说明
- **调用方式**：通过 Google Colab 网页界面在线调用，未部署本地权重。
- **训练说明**：本项目**未对 AlphaFold 2 进行训练或微调**，仅将其作为推理工具使用。参赛团队的实际创新贡献在于：输入序列的设计（丙氨酸扫描策略）、输出结果的结构分析（pLDDT、RMSD）以及后续的对接筛选与湿实验验证计划。

## 五、已知局限与特殊说明（关键）
- 本项目预测对象为**7肽短链**，其 `fraction_disordered=1.0`（100%无序），由于短肽在溶液中高度柔性，AlphaFold 预测的 pLDDT 数值普遍在 70-77 之间，这属于**正常现象，并非预测失败**。
- 预测构象**不能直接代表与 HER2 的结合亲和力**，需结合 HPEPDOCK 对接打分与后续实验验证。

## 六、本项目贡献与结论
将 AlphaFold 2 用于 HER2 靶向多肽的构象预测，结合 PyMOL 计算的 RMSD 分析，发现 L5 变体发生了显著构象变化（RMSD = 2.305 Å），提示其可能具有不同于原始肽的结合特性。随后通过 HPEPDOCK 验证了 L5（-198.400）比原始肽 L（-185.682）具有更强的 HER2 结合能力，为后续多肽药物设计提供了新思路。

## 七、相关辅助工具
- **HPEPDOCK 2.0**：多肽-蛋白分子对接，评估结合能力。详见 `models/HPEPDOCK_usage.md`。
- **PyMOL**：结构可视化与 RMSD 分析，版本 3.1.8。详见 `models/PyMOL_usage.md`。
