# PyMOL RMSD 计算操作步骤

## 工具信息
- 软件：PyMOL
- 版本：3.1.8
- 访问日期：2026-09-10

## 操作步骤
1. 打开 PyMOL，使用 `File -> Open` 加载 LTVSPWY.pdb 和突变体（如 LTVSAWY.pdb）。
2. 命令行输入 `align LTVSAWY, LTVSPWY`，计算 RMSD。
3. 记录控制台输出的 RMSD 值。
4. 使用 `bg_color white` 和 `ray 1200` 渲染图片，`File -> Export Image As -> PNG` 保存。
