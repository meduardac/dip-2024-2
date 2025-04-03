import numpy as np

def apply_geometric_transformations(img: np.ndarray) -> dict:
    # 1. Translating image (shifting right and down)
    shift_x, shift_y = 10, 10  # Shift values
    translated = np.zeros_like(img)
    translated[shift_y:, shift_x:] = img[:-shift_y, :-shift_x]
    
    # 2. Rotating image (90 degrees clockwise)
    rotated = np.rot90(img, k=-1)
    
    # 3. Horizontally stretching image (scaling width by 1.5)
    height, width = img.shape
    new_width = int(width * 1.5)
    stretched = np.zeros((height, new_width), dtype=img.dtype)
    x_indices = (np.arange(new_width) / 1.5).astype(int)
    x_indices[x_indices >= width] = width - 1
    stretched[:, :] = img[:, x_indices]
    
    # 4. Horizontally mirroring image (flipping along vertical axis)
    mirrored = img[:, ::-1]
    
    # 5. Barrel distortion (simple radial transformation)
    def barrel_distortion(img):
        h, w = img.shape
        distorted = np.zeros_like(img)
        cx, cy = w // 2, h // 2
        max_radius = np.sqrt(cx**2 + cy**2)
        for y in range(h):
            for x in range(w):
                dx, dy = x - cx, y - cy
                radius = np.sqrt(dx**2 + dy**2) / max_radius
                factor = 1 + 0.3 * radius**2  # Simple radial distortion factor
                new_x = int(cx + dx * factor)
                new_y = int(cy + dy * factor)
                if 0 <= new_x < w and 0 <= new_y < h:
                    distorted[y, x] = img[new_y, new_x]
        return distorted
    
    distorted = barrel_distortion(img)
    
    return {
        "translated": translated,
        "rotated": rotated,
        "stretched": stretched,
        "mirrored": mirrored,
        "distorted": distorted
    }
