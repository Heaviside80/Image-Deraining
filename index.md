---
layout: default
---

---
layout: default
title: Image-Deraining 研究主页
description: 记录图像去雨领域的科研进展、复现笔记与性能评测。
---

# 🌧️ Image-Deraining 研究库

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Stars](https://img.shields.io/github/stars/你的用户名/Image-Deraining?style=social)

## 🖼️ 实验结果展示 (Results Preview)

<p align="center">
  <img src="https://github.com/Heaviside80/Image-Deraining/raw/main/assets/images.jpeg" width="45%" title="Input Rainy Image">
  <img src="https://github.com/Heaviside80/Image-Deraining/raw/main/assets/images.jpeg" width="45%" title="Derained Result">
</p>

## 🚀 交互式去雨效果对比 (Interactive Slider)


<style>
  .comparison-slider {
    position: relative;
    width: 100%;
    max-width: 800px;
    margin: 20px auto;
    overflow: hidden;
    cursor: ew-resize;
  }
  .comparison-slider img {
    display: block;
    width: 100%;
    height: auto;
  }
  .overlay-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 50%; /* 初始显示比例 */
    height: 100%;
    overflow: hidden;
    border-right: 3px solid white;
    z-index: 2;
  }
  .overlay-image img {
    width: 800px; /* 必须与父容器 max-width 一致 */
    height: auto;
  }
</style>

<div class="comparison-slider" onmousemove="moveSlider(event)" ontouchmove="moveSlider(event)">
  <img src="./assets/images.jpeg" alt="After">
  
  <div class="overlay-image" id="slider-overlay">
    <img src="./assets/images.jpeg" alt="Before">
  </div>
</div>

<script>
  function moveSlider(e) {
    const slider = document.getElementById('slider-overlay');
    const container = slider.parentElement;
    const rect = container.getBoundingClientRect();
    let x = (e.pageX || e.touches[0].pageX) - rect.left;
    if (x < 0) x = 0;
    if (x > rect.width) x = rect.width;
    slider.style.width = (x / rect.width * 100) + '%';
  }
</script>

<p align="center"><i>左右移动鼠标查看去雨前后对比</i></p>


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
