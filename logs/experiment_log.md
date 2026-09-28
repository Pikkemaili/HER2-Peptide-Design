# 实验日志

## 2026-09-28

### AlphaFold 结构预测
- 完成 L 肽（LTVSPWY）及 L1-L7 丙氨酸扫描变体的 AlphaFold 3 预测。
- 所有任务的 ranking_score 均为 0.53，fraction_disordered=1.0（符合短肽高度柔性的特征）。
- 各变体的 atom plddts 估算均值：L(≈82), L1(≈85), L2(≈80), L3(≈82), L4(≈80), L5(≈88), L6(≈94), L7(≈95)。
- 8 个预测结构（`_model_0.cif`）已提取并重命名为 `L.cif` 至 `L7.cif`，上传至 `results/alphafold_structures/`。

### HPEPDOCK 分子对接
- 已提交 L_vs_6BGT 和 L5_vs_6BGT 对接任务，等待结果。

## 随机种子
本项目使用在线平台默认参数，未手动设置随机种子。
