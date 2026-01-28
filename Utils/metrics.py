import cv2
import numpy as np
import os
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

def calculate_metrics(img_path, gt_path):
    """
    计算去雨图像与真值图(Ground Truth)之间的PSNR和SSIM
    """
    # 读取图片 (确保以彩色模式读取)
    img = cv2.imread(img_path)
    gt = cv2.imread(gt_path)

    if img is None or gt is None:
        return None, None

    # 统一尺寸（防止某些模型输出尺寸略有偏差）
    if img.shape != gt.shape:
        img = cv2.resize(img, (gt.shape[1], gt.shape[0]))

    # 计算 PSNR
    # data_range=255 表示像素值范围是 0-255
    current_psnr = psnr(gt, img, data_range=255)

    # 计算 SSIM
    # channel_axis=2 表示处理彩色图片
    current_ssim = ssim(gt, img, channel_axis=2, data_range=255)

    return current_psnr, current_ssim

# --- 使用示例 ---
if __name__ == "__main__":
    # 填入你的测试图和原图路径
    test_img = "results/sample_01_derained.png"
    ground_truth = "data/test/gt/sample_01.png"
    
    p, s = calculate_metrics(test_img, ground_truth)
    if p:
        print(f"📊 Results:")
        print(f"PSNR: {p:.2f} dB")
        print(f"SSIM: {s:.4f}")
    else:
        print("❌ Error: Could not load images.")
