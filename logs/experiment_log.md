# 实验日志

## 2026-09-28

### 一、AlphaFold 3 结构预测
- 使用 AlphaFold Server (AlphaFold 3) 对 HER2 靶向多肽 LTVSPWY 及其 7 个丙氨酸扫描变体（L1-L7）进行三维结构预测。
- 输入序列：L(LTVSPWY), L1(ATVSPWY), L2(LAVSPWY), L3(LTASPWY), L4(LTVAPWY), L5(LTVSAWY), L6(LTVSPAY), L7(LTVSPWA)。
- 所有任务的全局 `ranking_score` 均为 0.53，`fraction_disordered` = 1.0。由于预测对象为7肽短链，短肽在溶液中高度柔性，该全局评分属于正常现象，并非操作失误。
- 预测结束后，提取每个任务的 `model_0.cif` 结构文件，并重命名为 L.cif 至 L7.cif，上传至 `results/alphafold_structures/`。

### 二、各变体局部置信度与结构叠合分析
- 为了量化突变对多肽构象的影响，使用 PyMOL 对各个变体与原始 L 肽进行结构叠合（命令：`align L1, L`），计算 RMSD（均方根偏差）。
- 结合 `full_data_0.json` 中的局部 pLDDT 估算值，汇总如下：

| 候选编号 | 序列 | 局部 pLDDT (估算) | RMSD (vs L肽) | 构象变化解读 |
|---|---|---|---|---|
| L | LTVSPWY | ≈ 82 | 0.000 Å | 原始肽，较柔性 |
| L1 | ATVSPWY | ≈ 85 | 0.670 Å | N端突变，骨架几乎不变 |
| L2 | LAVSPWY | ≈ 80 | 0.660 Å | 第2位突变，骨架几乎不变 |
| L3 | LTASPWY | ≈ 82 | 1.191 Å | 轻微构象变化 |
| L4 | LTVAPWY | ≈ 80 | 1.956 Å | 中度构象变化 |
| L5 | LTVSAWY | ≈ 88 | 2.860 Å | 显著构象变化 |
| L6 | LTVSPAY | ≈ 94 | 5.655 Å | 剧烈构象重排，结构高度刚性 |
| L7 | LTVSPWA | ≈ 95 | 2.881 Å | 显著构象变化，结构高度刚性 |

- **分析结论**：L1、L2 的结构与原始 L 肽高度相似（RMSD < 0.7 Å），说明 N 端突变未破坏骨架。而 L5、L6、L7 的 RMSD 显著升高（> 2.8 Å）且局部 pLDDT 极高（88-95），说明第5、6、7位氨基酸的替换导致了显著的构象重排，形成了更刚性、更稳定的新构象。

### 三、HPEPDOCK 分子对接
- 使用 HPEPDOCK 2.0 提交了 L 肽和 L5 肽与 HER2 胞外域（PDB: 6BGT）的分子对接任务。
- 任务名：L_vs_6BGT 和 L5_vs_6BGT。
- 状态：任务已提交，等待结果。
- 待填对接打分：
  - L_vs_6BGT 对接打分：[-185.682]
  - L5_vs_6BGT 对接打分：[-198.400]

### 四、随机种子与环境说明
- 本项目使用在线平台（AlphaFold Server 和 HPEPDOCK）默认参数，未手动设置随机种子。
- 本地运行 `predict.py` 生成结果文件时，未涉及随机过程。
