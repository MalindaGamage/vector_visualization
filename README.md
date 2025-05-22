# Vector Visualization Project

This Python project visualizes **2D vectors** using **NumPy** and **Matplotlib**, displaying them as arrows from the origin.

## 🚀 Features

* Visualizes multiple 2D vectors on a single plot
* Customizable colors and labels for each vector
* Automatic scaling of plot axes
* High-quality output image generation

## 📦 Installation

1. **Clone this repository**:

   ```bash
   git clone <your-repo-url>
   cd vector-visualization-project
   ```

2. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## 🧠 Usage

Run the main script:

```bash
python vector_plot.py
```

This will generate a plot in the `output/` directory showing the example vectors.

### ✏️ Customizing Vectors

To visualize your own vectors, modify the `vectors`, `colors`, and `labels` lists in the `if __name__ == "__main__":` block of `vector_plot.py`.

**Example:**

```python
vectors = [
    np.array([3, 2]),
    np.array([-2, 4])
]
colors = ['purple', 'orange']
labels = ['Vector A', 'Vector B']
```

## 📷 Output Example

A sample plot will be generated in the `output/` directory showing labeled arrows for each vector.

## 📚 Dependencies

* Python 3.7+
* NumPy
* Matplotlib

These are listed in the `requirements.txt` file:

```txt
numpy
matplotlib
```

## 📁 Folder Structure

```
vector-visualization-project/
├── vector_plot.py          # Main script to visualize vectors
├── requirements.txt        # Required Python packages
├── README.md               # Project documentation
└── output/                 # Output folder for saved plots
```

## 📌 How to Use This Project

1. Create a new directory for the project
2. Add the three files (`vector_plot.py`, `requirements.txt`, and `README.md`)
3. Create an `output` directory
4. Set up the virtual environment and install dependencies (as shown above)
5. Run the script:

   ```bash
   python vector_plot.py
   ```

The script will generate a plot showing vectors (e.g., red, blue, and green arrows) in the `output/` directory. You can easily change them by editing the lists in `vector_plot.py`.

## 📝 License

This project is open source and available under the **MIT License**.

---

Built with 💻 using Python & Matplotlib. Happy visualizing! 📈
