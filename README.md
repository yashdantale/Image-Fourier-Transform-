# Image-Fourier-Transform-
### The app is built on Streamlit
This app allows users to visualize the Fourier transform of an uploaded image and reconstruct the original image from its Fourier spectrum. The app first converts the uploaded image to grayscale, resizes it, and normalizes the pixel values to be between -1 and 1. It then applies a 2D Fourier transform to the normalized image and plots the magnitude spectrum, which represents the frequencies present in the image. The user can also view the phase spectrum, which represents the relative phase of each frequency component. Finally, the app can reconstruct the original image from the Fourier spectrum by applying an inverse Fourier transform and normalizing the pixel values to be between 0 and 255.

## Technologies Used

Python 3.9.2

Streamlit 1.4.0

NumPy 1.20.1

Matplotlib 3.4.1

Pillow 8.1.0

SciPy 1.6.1

## Installation
Clone the repository: git clone https://github.com/yashdantale/Image-Fourier-Transform-

Change into the directory: cd image-fourier-transform
Create a virtual environment: python3 -m venv venv
Activate the virtual environment: source venv/bin/activate
Install the requirements: pip install -r requirements.txt

Sure, here's a sample README file for the image Fourier transform app:

Image Fourier Transform
This app allows you to visualize the Fourier transform of an image and reconstruct the original image from its Fourier spectrum.

Technologies Used
Python 3.9.2
Streamlit 1.4.0
NumPy 1.20.1
Matplotlib 3.4.1
Pillow 8.1.0
SciPy 1.6.1
Installation
Clone the repository: git clone https://github.com/your-username/image-fourier-transform.git
Change into the directory: cd image-fourier-transform
Create a virtual environment: python3 -m venv venv
Activate the virtual environment: source venv/bin/activate
Install the requirements: pip install -r requirements.txt

## Usage
Activate the virtual environment: source venv/bin/activate
Run the app: streamlit run app.py

Upload an image and adjust the size slider

View the grayscale, normalized, and Fourier transformed images

Optionally, view the phase spectrum and reconstruct the original image from the Fourier spectrum

## Contributors
Your Name - @yashdantale

## License

This project is licensed under the MIT License - see the LICENSE file for details.
