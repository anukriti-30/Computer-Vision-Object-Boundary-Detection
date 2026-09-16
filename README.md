# Object Boundary Detection Using Image Processing

## 1. Project Overview

This project detects the edges and boundaries of objects present in an input image using basic computer vision and image processing techniques.

The project follows a sequence of image processing operations. The input image is first converted to grayscale and smoothed using Gaussian Blur. Canny Edge Detection is then applied to identify important edges. Morphological processing is used to improve the detected edges, after which contours are extracted to identify object boundaries.

## 2. Objectives

The main objectives of this project are:

* To convert a color image into grayscale.
* To reduce image noise using Gaussian Blur.
* To detect edges using the Canny Edge Detection algorithm.
* To improve the detected edges using morphological processing.
* To identify and draw object boundaries using contours.
* To save the intermediate and final results for analysis.

## 3. Technologies Used

* Python
* OpenCV
* NumPy
* VS Code

## 4. Computer Vision Techniques Used

### Grayscale Conversion

The input color image is converted into grayscale so that further image processing can be performed using intensity information.

### Gaussian Blur

Gaussian Blur is applied to reduce noise and small unwanted variations in the image before edge detection.

### Canny Edge Detection

Canny Edge Detection is used to identify significant intensity changes in the image and produce an edge image.

### Morphological Processing

Morphological closing is applied to connect nearby edge regions and reduce small gaps in detected edges.

### Contour Detection

Contours are extracted from the processed edge image. These contours are used to represent the boundaries of objects.

## 5. Project Structure

Computer_Vision_Object_Boundary_Detection/
│
├── input/
│   └── input.jpg
│
├── output/
│   ├── grayscale.jpg
│   ├── blurred.jpg
│   ├── edges.jpg
│   ├── morphology.jpg
│   └── final_boundaries.jpg
│
├── src/
│   └── main.py
│
├── requirements.txt
└── README.md

## 6. Requirements

The project requires Python 3 and OpenCV.

The required Python package is listed in `requirements.txt`.

## 7. Installation

Open a terminal in the project directory.

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required package:

```bash
pip install -r requirements.txt
```

## 8. Input

Place the image to be processed inside the `input` folder and name it:
input.jpg

The expected location is:
input/input.jpg

## 9. How to Run
From the main project directory, run:
python src/main.py 

The program processes the input image and saves the results in the `output` folder.

## 10. Output

The program generates the following files:

* `grayscale.jpg` — grayscale version of the input image.
* `blurred.jpg` — image after Gaussian smoothing.
* `edges.jpg` — edges detected using Canny Edge Detection.
* `morphology.jpg` — image after morphological processing.
* `final_boundaries.jpg` — original image with detected boundaries drawn on it.

The terminal also displays the number of detected boundaries.

## 11. Workflow

```text
Input Image
     ↓
Grayscale Conversion
     ↓
Gaussian Blur
     ↓
Canny Edge Detection
     ↓
Morphological Closing
     ↓
Contour Detection
     ↓
Object Boundary Visualization
```

## 12. Limitations

The quality of boundary detection depends on the input image, lighting conditions, object complexity, and the selected edge detection parameters. Images with heavy noise or very low contrast may produce unwanted edges.

## 13. Future Scope

The project can be extended by adding automatic parameter selection, noise removal techniques, object classification, or more advanced segmentation methods.

## 14. Conclusion

This project demonstrates a basic computer vision pipeline for detecting object boundaries from an image. It combines grayscale conversion, Gaussian smoothing, Canny edge detection, morphological processing, and contour detection to obtain the final boundary representation.
