# PyMOL 使用说明

## 软件信息
- 名称：PyMOL
- 版本：3.1.8
- 来源：Schrödinger
- 使用许可：Evaluation License（评估版）
- 使用日期：2026-09-09

## 用途
1. 加载 AlphaFold2 预测的 `.pdb` 结构文件。
2. 使用 `align` 命令将突变体（L1-L7）与原始 L 肽进行结构叠合，计算 RMSD。
3. 生成结构对比图，用于展示构象变化。

## 关键命令
- 加载文件：`File -> Open` 或 `load L.pdb`
- 结构叠合：`align L1, L`
- 换颜色：`color blue, L1`
- 渲染图片：`bg_color white` -> `ray 1200` -> 保存图片

## 已知局限
仅用于可视化与结构比对，不提供结合亲和力或活性预测。
