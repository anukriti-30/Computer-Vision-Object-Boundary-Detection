import cv2
import os

# Input and output paths
input_path = "input/input.jpg"
output_folder = "output"

# Create output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Read image
image = cv2.imread(input_path)

if image is None:
    print("Error: Image not found.")
    exit()

# 1. Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 3. Detect edges using Canny
edges = cv2.Canny(blur, 50, 150)

# 4. Apply morphological operation
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
morphology = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# 5. Find object boundaries
contours, _ = cv2.findContours(
    morphology,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

boundary_image = image.copy()

cv2.drawContours(
    boundary_image,
    contours,
    -1,
    (0, 255, 0),
    2
)

# Save results
cv2.imwrite("output/grayscale.jpg", gray)
cv2.imwrite("output/blurred.jpg", blur)
cv2.imwrite("output/edges.jpg", edges)
cv2.imwrite("output/morphology.jpg", morphology)
cv2.imwrite("output/final_boundaries.jpg", boundary_image)

print("Processing completed successfully.")
print("Number of objects/boundaries detected:", len(contours))
print("Results saved in the output folder.")