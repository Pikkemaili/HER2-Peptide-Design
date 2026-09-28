# Model Card: AlphaFold 3 (via AlphaFold Server)

## 一、模型基本信息
- **模型名称**：AlphaFold Server (AlphaFold 3)
- **版本**：在线公开版 (Web Server)
- **来源**：Google DeepMind (https://alphafoldserver.com)
- **访问日期**：2026-09-28
- **模型类型**：蛋白质/多肽三维结构预测模型

## 二、适用范围
本项目使用 AlphaFold 3 预测 HER2 靶向多肽 LTVSPWY 及其 7 个丙氨酸扫描变体（L1-L7）的三维构象。
该模型适用于单链多肽及蛋白质复合物的结构预测。

## 三、输入与输出
- **输入**：单字母氨基酸序列（FASTA格式，7肽）。
- **输出**：
  - `.cif` 三维结构文件
  - `summary_confidences.json`：包含 ranking_score、ptm等全局置信度
  - `full_data.json`：包含 atom plddts（局部置信度0-100）、PAE矩阵等

## 四、调用方式与训练说明
- **调用方式**：通过网页界面在线调用，未部署本地权重。
- **训练说明**：本项目**未对 AlphaFold 3 进行训练或微调**，仅将其作为推理工具使用。参赛团队的实际创新贡献在于：输入序列的设计（丙氨酸扫描策略）、输出结果的结构分析（pLDDT、RMSD）以及后续的对接筛选。

## 五、已知局限与特殊说明（关键）
- 本项目预测对象为**7肽短链**，其 `fraction_disordered=1.0`（100%无序），由于短肽在溶液中高度柔性，AlphaFold 的全局 `ranking_score` 稳定在 0.53，这属于**正常现象，并非预测失败**。
- 局部 `pLDDT` 分数（例如 L6≈94, L7≈95）和结构叠合 RMSD 存在显著差异，证明突变确实导致了局部构象重排。
- 预测构象**不能直接代表与 HER2 的结合亲和力**，需结合 HPEPDOCK 对接打分与后续实验验证。

## 六、本项目贡献与结论
将 AlphaFold 3 用于 HER2 靶向多肽的构象预测，结合 PyMOL 计算的 RMSD 分析，发现 L5、L6、L7 变体发生了显著构象变化，并形成了更稳定的刚性结构，提示其可能是比文献报道的 L5 更优的候选多肽，为后续多肽药物设计提供了新思路。

## 七、相关辅助工具
- **HPEPDOCK 2.0**：多肽-蛋白分子对接，评估结合能力。详见 `models/HPEPDOCK_usage.md`。
- **PyMOL**：结构可视化与 RMSD 分析。详见 `models/PyMOL_usage.md`。
