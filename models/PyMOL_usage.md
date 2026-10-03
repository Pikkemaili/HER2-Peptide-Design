# PyMOL 使用说明

## 一、软件信息
- 名称：PyMOL
- 版本：3.1.8
- 来源：Schrödinger
- 使用许可：Evaluation License（评估版）
- 使用日期：2026-09-09

## 二、用途
1. 加载 AlphaFold2 预测的 `.pdb` 结构文件（L.pdb 至 L7.pdb）。
2. 使用 `align` 命令将突变体（L1-L7）与原始 L 肽进行结构叠合，计算 RMSD。
3. 生成结构对比图并标注每个残基，用于展示构象变化。

## 三、关键命令
- 加载文件：`File -> Open` 或 `load L.pdb`
- 结构叠合：`align L1, L`
- 主链/侧链分别着色：`color blue, L1 and backbone` 和 `color cyan, L1 and sidechain`
- 标注所有残基：`label L1 and name CA, "resn resi"`
- 渲染图片：`bg_color white` -> `ray 1200` -> `File -> Export Image As -> PNG`

## 四、输入与输出
- 输入：AlphaFold2 输出的 `.pdb` 结构文件。
- 输出：结构叠合图（PNG格式，存于 `results/pymol_images/`），以及记录在 `logs/experiment_log.md` 中的 RMSD 数值。

## 五、已知局限
- 仅用于可视化与结构比对，不提供结合亲和力或活性预测。
- RMSD 仅反映结构偏差，不代表结合强弱，需结合 HPEPDOCK 对接打分综合评估。

## 六、本项目贡献
利用 PyMOL 3.1.8 对 8 条候选肽进行结构叠合分析，结果发现：
- L1-L4 的 RMSD 极小（<0.6 Å），说明 N 端及中段突变未破坏多肽骨架。
- **L5 的 RMSD 显著升高至 2.305 Å**，说明第 5 位氨基酸的替换导致了显著的构象重排。
该结果为后续选择 L5 进行 HPEPDOCK 对接和湿实验验证提供了关键的结构依据。

## 七、对接复合物可视化

对接结果的可视化命令保存在 `src/` 目录下：
- `src/visualize_L.pml`：查看原始肽 L 与 HER2 的结合模式。
- `src/visualize_L5.pml`：查看 L5 变体与 HER2 的结合模式。

使用方法：
1. 启动 PyMOL，在命令行输入 `cd 到你的仓库根目录`。
2. 输入 `@src/visualize_L.pml` 或 `@src/visualize_L5.pml`。
3. 脚本会自动加载 6BGT 和对接复合物，显示结合口袋、氢键和关键残基标签。

生成的图片已保存在 `results/docking_visualization/`。
