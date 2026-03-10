# Day 3: Image Generation & Prompt Reverse Engineering

## 📝 Task Overview
The goal of this exercise was to reverse-engineer a specific reference image of a person coding in a cafe and recreate it as closely as possible using **ZImage Turbo** on Hugging Face.

## ⚙️ Configuration
- **Model:** ZImage Turbo (SDXL)
- **Seed:** `70216`
- **Sampling Steps:** 4
- **Guidance Scale:** 1.5

## 🔍 Image Analysis & Prompt Engineering
To match the reference image, I identified the following key features:
* **Subject:** A young Asian woman wearing glasses and a cream-colored knitted sweater.
* **Action:** Coding/programming with a visible code editor on a laptop screen.
* **Environment:** A warm cafe setting with a round wooden table and a white coffee cup (latte art).
* **Lighting:** High-contrast natural side-lighting coming from a window.
* **Composition:** Medium shot, 35mm lens feel, with a soft bokeh (blurred) street background.

### Final Optimized Prompt:
> "Young Asian woman with glasses coding on laptop in a cozy cafe, latte art in white cup on round wooden table, soft natural window lighting, cinematic bokeh background, photorealistic, 35mm lens, high detail, calm atmosphere."

## 🖼️ Results
The final output successfully captured the lighting and the "developer" aesthetic of the original reference image while maintaining high fidelity using the provided seed.