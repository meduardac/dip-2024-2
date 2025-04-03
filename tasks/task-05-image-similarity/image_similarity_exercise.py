# Redefinindo a função compare_images e suas métricas

def mse(i1: np.ndarray, i2: np.ndarray) -> float:
    """Calculate Mean Squared Error between two images"""
    return np.mean((i1 - i2) ** 2)

def psnr(i1: np.ndarray, i2: np.ndarray) -> float:
    """Calculate Peak Signal-to-Noise Ratio"""
    mse_val = mse(i1, i2)
    if mse_val == 0:
        return float('inf')
    return 20 * np.log10(1.0 / np.sqrt(mse_val))

def ssim(i1: np.ndarray, i2: np.ndarray) -> float:
    """Calculate simplified Structural Similarity Index"""
    C1 = (0.01) ** 2
    C2 = (0.03) ** 2
    
    mu1 = np.mean(i1)
    mu2 = np.mean(i2)
    
    sigma1_sq = np.var(i1)
    sigma2_sq = np.var(i2)
    sigma12 = np.mean((i1 - mu1) * (i2 - mu2))
    
    num = (2 * mu1 * mu2 + C1) * (2 * sigma12 + C2)
    den = (mu1**2 + mu2**2 + C1) * (sigma1_sq + sigma2_sq + C2)
    
    return num / den

def npcc(i1: np.ndarray, i2: np.ndarray) -> float:
    """Calculate Normalized Pearson Correlation Coefficient"""
    i1_centered = i1 - np.mean(i1)
    i2_centered = i2 - np.mean(i2)
    
    numerator = np.sum(i1_centered * i2_centered)
    denominator = np.sqrt(np.sum(i1_centered**2) * np.sum(i2_centered**2))
    
    return numerator / denominator if denominator != 0 else 0

def compare_images(i1: np.ndarray, i2: np.ndarray) -> dict:
    """Compare two normalized grayscale images using multiple similarity metrics."""
    if i1.shape != i2.shape:
        raise ValueError("Images must have the same dimensions")
        
    return {
        "mse": mse(i1, i2),
        "psnr": psnr(i1, i2),
        "ssim": ssim(i1, i2),
        "npcc": npcc(i1, i2)
    }

# Reexecutando os testes
results = {
    "img1_vs_img2": compare_images(img1, img2),
    "img1_vs_img3": compare_images(img1, img3),
    "img3_vs_img4": compare_images(img3, img4),
    "img4_vs_img4": compare_images(img4, img4),  # Comparação consigo mesma (deve ter erro 0)
}

results
