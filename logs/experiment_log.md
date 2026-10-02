# 实验日志

## 2026-09-09

### 一、AlphaFold2 结构预测
- 使用 AlphaFold2 (Colab网页端) 对 HER2 靶向多肽 LTVSPWY 及其 7 个丙氨酸扫描变体（L1-L7）进行三维结构预测。
- 输入序列：L(LTVSPWY), L1(ATVSPWY), L2(LAVSPWY), L3(LTASPWY), L4(LTVAPWY), L5(LTVSAWY), L6(LTVSPAY), L7(LTVSPWA)。
- 提取排名第一的 `.pdb` 结构文件并重命名为 L.pdb 至 L7.pdb，上传至 `results/alphafold_structures/`。
- 各变体 pLDDT 估算值（AlphaFold2真实输出）：L(74.9), L1(77.2), L2(72.7), L3(75.1), L4(77.0), L5(71.5), L6(70.5), L7(72.4)。

### 二、PyMOL 结构叠合分析（RMSD）
- 使用 PyMOL 3.1.8 对各个变体与原始 L 肽进行结构叠合（命令：`align L1, L`），计算 RMSD。
- 汇总数据（最新版）：
  - L1 vs L: 0.270 Å
  - L2 vs L: 0.583 Å
  - L3 vs L: 0.500 Å
  - L4 vs L: 0.549 Å
  - L5 vs L: 2.305 Å
  - L6 vs L: 1.938 Å
  - L7 vs L: 1.026 Å
- **结论**：所有变体的 pLDDT 都在 70-77 之间，这符合 7 肽短链高度柔性的特征。结构叠合分析显示，L1-L4 的 RMSD 极小（<0.6 Å），说明 N 端及中段突变未破坏多肽骨架。而 **L5 的 RMSD 显著升高至 2.305 Å**，说明第 5 位氨基酸的替换导致了显著的构象重排。

### 三、HPEPDOCK 分子对接
- 使用 HPEPDOCK 2.0 提交了 L 肽和 L5 肽与 HER2 胞外域（PDB: 6BGT）的分子对接任务。
- 任务名：L_vs_6BGT 和 L5_vs_6BGT。
- 对接打分（排名第1的模型）：
  - L_vs_6BGT 对接打分：-185.682 kcal/mol
  - L5_vs_6BGT 对接打分：-198.400 kcal/mol
- **结论**：L5变体的对接打分低于原始L肽，说明L5与HER2的结合能更低、结合更稳定，验证了基于结构优化的合理性。

### 四、后续湿实验验证计划
- 基于 AlphaFold2 和 HPEPDOCK 的筛选结果，后续将对第2位和第5位点进行湿实验验证（如定点突变、表面等离子共振SPR或等温滴定量热ITC），以评估 L5 变体与 HER2 的实际结合亲和力。

### 五、随机种子与环境说明
- 本项目使用在线平台默认参数，未手动设置随机种子。
- 本地运行 `predict.py` 生成结果文件时，未涉及随机过程。
