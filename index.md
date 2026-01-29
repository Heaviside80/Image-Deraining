---
layout: default
title: Image-Deraining 研究主页
description: 记录图像去雨领域的科研进展、复现笔记与性能评测。
---

# 🌧️ Image-Deraining 研究库

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Stars](https://img.shields.io/github/stars/你的用户名/Image-Deraining?style=social)

## 🖼️ 实验结果展示 (Results Preview)


<!-- <p align="center">
  <img src="./assets/images.jpeg" width="45%" width="400" height="300" style="object-fit: cover title="Input Rainy Image">
  <img src="./assets/treasure.png" width="45%" width="400" height="300" style="object-fit: cover title="Derained Result">
</p>
<p align="center">
  <b>左图：原始雨图 | 右图：去雨结果</b>
</p> -->

---
layout: default
title: Image-Deraining Demo
---


# 🌧️ 图像去雨效果展示

使用下方滑块左右拖动，对比去雨前后的细节表现：

<div style="width: 100%; max-width: 800px; margin: 0 auto;">
  <iframe 
    frameborder="0" 
    class="juxtapose" 
    width="100%" 
    height="500" 
    src="https://cdn.knightlab.com/libs/juxtapose/latest/embed/index.html?uid=8390b168-dd96-11ee-b693-b51909e4c3a3&label1=Rainy&label2=Derained&location=https://github.com/Heaviside80/Image-Deraining/raw/main/assets/images.jpeg&location2=https://github.com/Heaviside80/Image-Deraining/raw/main/assets/treasure.png">
  </iframe>
</div>

---

### 💡 无法看到滑块？
1. **查看正式网址**：请访问 `https://heaviside80.github.io/Image-Deraining/`（在 GitHub 仓库预览页是看不到滑动的）。
2. **强制刷新**：如果看到的是旧图，请按 `Ctrl + F5`。
3. **检查格式**：确认 `treasure.png` 的后缀确实是 `.png` 而不是 `.PNG`。
## 📖 项目简介
本项目致力于构建一个系统化的图像去雨学习路径。我们不仅关注传统的物理模型，更紧跟深度学习前沿（CNN, Transformer, Mamba）。

## 📂 快速跳转
- [📚 文献精读笔记](./Papers/) - 包含 DDN, PReNet, Restormer 等。
- [📊 实验性能对比](./Papers/#benchmark) - 统一数据集下的 PSNR/SSIM 表现。
- [🛠️ 开发工具库](./Utils/) - 包含图像质量评价脚本。
- [📅 数据集获取](./Datasets/) - 常用去雨数据集汇总。

## 🛠️ 环境要求
```bash
pip install -r requirements.txt
