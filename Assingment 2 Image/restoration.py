# ==========================================================
# Name: Ashish Yadav
# Roll No: 23010104413
# Course: B.Tech CSE
# Unit: Image Processing
# Assignment Title: Surveillance Image Restoration System
# Date: 25-02-2026
# ==========================================================

import cv2
import numpy as np
import os

# ========== CREATE OUTPUT FOLDER ==========
output_folder = "outputs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ========== IMAGE PATHS (3 SAMPLE RUNS) ==========
image_paths = [
    r"C:\Users\gtcam\OneDrive\Desktop\Assingment 2 Image\parking-garage-with-surveillance-cameras-enhanced-security-monitoring_416256-87302.jpg",
    r"C:\Users\gtcam\OneDrive\Desktop\document_scanner\OIP.webp",
    r"C:\Users\gtcam\OneDrive\Desktop\document_scanner\2nd image.webp"
]

# ========== FUNCTIONS ==========

def add_gaussian_noise(image):
    mean = 0
    sigma = 25
    noise = np.random.normal(mean, sigma, image.shape).astype(np.uint8)
    noisy = cv2.add(image, noise)
    return noisy

def add_salt_pepper_noise(image):
    noisy = image.copy()
    prob = 0.02
    rnd = np.random.rand(*image.shape)
    noisy[rnd < prob] = 0
    noisy[rnd > 1 - prob] = 255
    return noisy

def mean_filter(image):
    return cv2.blur(image, (5, 5))

def gaussian_filter(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

def median_filter(image):
    return cv2.medianBlur(image, 5)

def mse(original, restored):
    return np.mean((original - restored) ** 2)

def psnr(original, restored):
    mse_value = mse(original, restored)
    if mse_value == 0:
        return 100
    return 10 * np.log10((255 ** 2) / mse_value)

# ========== PROCESSING PIPELINE ==========

print("\n================ IMAGE RESTORATION SYSTEM ================\n")

for idx, path in enumerate(image_paths):

    print(f"\nProcessing Image {idx+1}...")

    # ---------- LOAD ----------
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Save original
    cv2.imwrite(f"{output_folder}/original_{idx+1}.png", gray)

    # ---------- TASK 2: NOISE ----------
    gaussian_noisy = add_gaussian_noise(gray)
    sp_noisy = add_salt_pepper_noise(gray)

    cv2.imwrite(f"{output_folder}/gaussian_noise_{idx+1}.png", gaussian_noisy)
    cv2.imwrite(f"{output_folder}/saltpepper_noise_{idx+1}.png", sp_noisy)

    # ---------- TASK 3: RESTORATION ----------
    mean_restored = mean_filter(gaussian_noisy)
    gaussian_restored = gaussian_filter(gaussian_noisy)
    median_restored = median_filter(sp_noisy)

    cv2.imwrite(f"{output_folder}/mean_restored_{idx+1}.png", mean_restored)
    cv2.imwrite(f"{output_folder}/gaussian_restored_{idx+1}.png", gaussian_restored)
    cv2.imwrite(f"{output_folder}/median_restored_{idx+1}.png", median_restored)

    # ---------- TASK 4: METRICS ----------
    mse_mean = mse(gray, mean_restored)
    psnr_mean = psnr(gray, mean_restored)

    mse_gaussian = mse(gray, gaussian_restored)
    psnr_gaussian = psnr(gray, gaussian_restored)

    mse_median = mse(gray, median_restored)
    psnr_median = psnr(gray, median_restored)

    # ---------- TASK 5: ANALYSIS ----------
    print("\n--- Performance Metrics ---")
    print(f"Mean Filter -> MSE: {mse_mean:.2f}, PSNR: {psnr_mean:.2f}")
    print(f"Gaussian Filter -> MSE: {mse_gaussian:.2f}, PSNR: {psnr_gaussian:.2f}")
    print(f"Median Filter -> MSE: {mse_median:.2f}, PSNR: {psnr_median:.2f}")

    print("\n--- Best Methods ---")

    if psnr_gaussian > psnr_mean:
        print("Best for Gaussian Noise: Gaussian Filter")
    else:
        print("Best for Gaussian Noise: Mean Filter")

    print("Best for Salt & Pepper Noise: Median Filter")

    print("\n--- Theoretical Justification ---")
    print("Gaussian filter smooths intensity variations effectively.")
    print("Mean filter reduces noise but blurs edges.")
    print("Median filter removes impulse noise without damaging edges.")

    print("\n--------------------------------------------------")

print("\nAll images processed successfully.")
print(f"Check the '{output_folder}' folder for output results.\n")