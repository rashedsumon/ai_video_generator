# utils/video_utils.py
import os
import cv2
import numpy as np
from pathlib import Path

def generate_video_from_prompts(prompt: str, style: str, fps: int = 24, duration: int = 10) -> str:
    """
    Generates an AI video from textual prompt using OpenCV.
    
    Args:
        prompt (str): Video description
        style (str): Animation style
        fps (int): Frames per second
        duration (int): Video duration in seconds
    
    Returns:
        str: Path to generated video
    """
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "sample_output.avi"  # OpenCV-friendly format

    width, height = 640, 360
    total_frames = fps * duration

    # VideoWriter using OpenCV
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))

    for i in range(total_frames):
        # Placeholder frame (gradient effect)
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        color_value = int((i / total_frames) * 255)
        frame[:] = (color_value, 255 - color_value, (color_value * 2) % 255)
        
        # Add text prompt on first frame
        if i == 0:
            cv2.putText(frame, prompt, (50, height // 2), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (255, 255, 255), 2, cv2.LINE_AA)
        
        out.write(frame)

    out.release()
    return str(output_path)
