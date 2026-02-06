import os
import sys

from pdf2image import convert_from_path
from PIL import Image

# 解除PIL图片大小限制，避免大分辨率图片报错
Image.MAX_IMAGE_PIXELS = None


def convert(pdf_path, output_dir, dpi=300, max_dim=None):
    """
    高清PDF转图片

    Args:
        pdf_path: PDF文件路径
        output_dir: 输出目录
        dpi: 分辨率（默认300，可选400/600）
        max_dim: 最大尺寸（默认None表示不限制，保持原始分辨率）
    """
    images = convert_from_path(pdf_path, dpi=dpi)

    for i, image in enumerate(images):
        width, height = image.size

        # 如果设置了max_dim且图片超过限制，则等比缩放
        if max_dim and (width > max_dim or height > max_dim):
            scale_factor = min(max_dim / width, max_dim / height)
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)
            image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        image_path = os.path.join(output_dir, f"page_{i+1}_dpi{dpi}.png")
        image.save(image_path, "PNG", optimize=True)
        print(f"Saved page {i+1} as {image_path} (size: {image.size}, dpi: {dpi})")

    print(f"Converted {len(images)} pages to PNG images at {dpi} DPI")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: convert_pdf_to_images_hd.py [input pdf] [output directory] [dpi]")
        print("  dpi: optional, default 300, recommend 300/400/600")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_directory = sys.argv[2]
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 300

    convert(pdf_path, output_directory, dpi=dpi)
