# PaletteX

PaletteX is a feature-rich, fullscreen desktop drawing application built with Python and OpenCV, designed for intuitive shape-based sketching and freehand drawing. The project includes a custom toolbar with tools for selecting shapes, adjusting brush thickness, choosing colors, filling areas, and more - all laid out in a clean, visually structured UI.

What sets this project apart is its use of a custom-built library, spectrasketch.ShapeLab, developed specifically to simplify drawing geometric shapes and modularize canvas operations.

Sketchy is ideal for hobbyists, students, or developers looking to explore drawing mechanics, GUI design, and OpenCV’s creative potential.

---

## Key Features

- **Full-Screen Drawing Canvas**
- **Custom Toolbar Interface**
- **Shape Drawing Modes**: Rectangle, Circle, Line, Triangle, Stars, Polygonal shapes, Heart, and more.
- **Freehand Drawing**
- **Fill Tool (Flood Fill)**
- **Eraser Tool**
- **Color Palette with 30 Preset Colors**
- **Adjustable Brush Thickness**
- **Interactive Icon Grid Layout**
- **Visual Shape Preview While Drawing**

---

![PaletteX Art](assets/test_image)

---

## Library Structure

This application leverages a custom-built library called `spectrasketch`, specifically the `ShapeLab` class, to abstract and simplify drawing operations.

The library includes:
- Easy-to-use methods for drawing various geometric shapes
- Simplified commands for drawing operations like `circle`, `line`, `rectangle`, `triangle`, `heart`, `star`, and more
- Custom parameters for angle and rotation

---

## Dependencies

Ensure you have the following Python packages installed:

```bash
pip install opencv-python numpy screeninfo spectrasketch
```

---

## Mode Selection

Each toolbar section corresponds to a feature:

Selection: Reserved for future use (e.g., layers, selection tools).

Image Tools: Pencil, eraser, fill, exit.

Brush Thickness: Six levels of brush thickness.

Brush Shapes: Placeholder (can be extended).

Shape Drawing Tools: A wide range of geometric and custom shapes.

Color Palette: 30 preset colors.

Copilot Section: Placeholder label ("Sketchy").

Layers Section: Reserved for future layer management.

---

## Future Enhancements that are being worked on

Undo/Redo functionality

Save/Export canvas as image

Rotation and transformation tools

Layer management system

---

