# 📷 AI-Based Surveillance Image Restoration System

## 👨‍🎓 Student Details
- **Name:** Ashish Yadav  
- **Roll No:** 23010104413  
- **Course:** B.Tech CSE  
- **Subject:** Image Processing  
- **Assignment:** Surveillance Image Restoration System  
- **Date:** 25-02-2026  

---

## 📌 Project Overview

This project focuses on **image restoration techniques** for surveillance-style images such as:

- Parking areas  
- Street views  
- Corridors  

The system simulates real-world noise and restores images using spatial filtering techniques.

---

## 🎯 Objectives

- Convert surveillance images to grayscale  
- Add realistic noise (Gaussian & Salt-and-Pepper)  
- Apply restoration filters  
- Evaluate performance using **MSE** and **PSNR**  
- Compare filter performance analytically  

---

## 🧠 Techniques Used

### 🔹 Noise Models
- Gaussian Noise (Sensor Noise)
- Salt-and-Pepper Noise (Transmission Noise)

### 🔹 Restoration Filters
- Mean Filter
- Gaussian Filter
- Median Filter

---

## 📊 Performance Metrics

The system evaluates restoration quality using:

- **MSE (Mean Squared Error)**
- **PSNR (Peak Signal-to-Noise Ratio)**

---

## 🖼️ Output Results

All processed images are saved in the **outputs/** folder:

### ✔ Original Images
- original_1.png
- original_2.png
- original_3.png

### ✔ Noisy Images
- gaussian_noise_1.png
- saltpepper_noise_1.png
- etc...

### ✔ Restored Images
- mean_restored_1.png
- gaussian_restored_1.png
- median_restored_1.png

---

## 📈 Observations

| Noise Type | Best Filter | Reason |
|------------|-------------|--------|
| Gaussian Noise | Gaussian Filter | Smooths intensity variations effectively |
| Salt & Pepper Noise | Median Filter | Removes impulse noise while preserving edges |

---

## 🧪 Sample Runs

The system was tested on 3 surveillance-style images:

1. Parking Garage
2. Document-style CCTV frame
3. Corridor-style image

---

## ⚙️ How to Run

1. Install dependencies:

```bash
pip install opencv-python numpy
