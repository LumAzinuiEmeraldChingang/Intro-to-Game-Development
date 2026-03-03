# Intro-to-Game-Development
# Lum Azinui Emerald Chingang – Pygame Character Animation

## 📌 Project Overview

This project is a simple 2D character movement and animation system built using **Pygame**.  
The application creates an 800x600 game window where a character can move in four directions using the arrow keys while displaying a running animation.

The character:
- Moves left and right
- Moves forward and backward (up and down)
- Animates only while moving
- Flips direction when turning
- Is restricted within the window boundaries

---

## 🎮 Features

- ✅ 800x600 Game Window
- ✅ Arrow Key Movement (Up, Down, Left, Right)
- ✅ Frame-Based Running Animation
- ✅ Sprite Flipping When Turning
- ✅ Delta Time Movement (Smooth & Frame-Rate Independent)
- ✅ Window Boundary Limits (Character cannot leave screen)
- ✅ Idle State When Not Moving

---

## 🛠 Requirements

- Python 3.x
- Pygame

Install Pygame if not already installed:
pip install pygame

---

## 📘 Project Structure
project_folder/
│
├── main.py
├── 0.png
├── 1.png
├── 2.png
└── 3.png

If you want to add more frames, update:
TOTAL_FRAMES = <number_of_images>

---

## NoteImportant:
All sprite images must:
- Be .png format
- Have the same dimensions
- Be placed in the same folder as the Python file
- Be named sequentially starting from 0.png

  ---

## ▶️ How to Run

- Open terminal or command prompt.
- Navigate to the project folder.
- Run:
    python Milestone1_LumAzinuiEmeraldChingang_Track.py
