# AlphaFold 3 模型调用说明

## 一、模型信息
- 名称：AlphaFold Server (AlphaFold 3)
- 版本：在线公开版
- 来源：Google DeepMind
- 访问日期：2026-09-28

## 二、调用方式
通过网页界面在线调用，未部署本地权重，未进行训练或微调，仅作为推理工具。

## 三、调用参数
- Entity type: Protein
- Copies: 1
- MSA: 默认
- 其他参数：默认

## 四、输入输出
- 输入：单字母氨基酸序列（7肽）
- 输出：`.cif` 结构文件、`summary_confidences.json`（含 ranking_score）、`full_data.json`（含 pLDDT）

## 五、已知局限
- 短肽高度柔性，fraction_disordered=1.0，全局 ranking_score 稳定在 0.53 属正常现象。
- 预测构象不直接代表结合亲和力，需结合 HPEPDOCK 对接打分综合评估。

## 六、本项目贡献
将 AlphaFold 3 用于 HER2 靶向多肽变体构象预测，结合 RMSD 分析，发现了比文献 L5 位点结构更刚性的 L6 和 L7 变体。
