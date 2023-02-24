import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft2, ifft2
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Image Fourier Transform", page_icon=":art:")
st.title('Image Fourier Transform')
# st.write('This app allows you to visualize the Fourier transform of an image and reconstruct the original image from its Fourier spectrum.')
st.info("This app allows users to visualize the Fourier transform of an uploaded image and reconstruct the original image from its Fourier spectrum. The app first converts the uploaded image to grayscale, resizes it, and normalizes the pixel values to be between -1 and 1. It then applies a 2D Fourier transform to the normalized image and plots the magnitude spectrum, which represents the frequencies present in the image. The user can also view the phase spectrum, which represents the relative phase of each frequency component. Finally, the app can reconstruct the original image from the Fourier spectrum by applying an inverse Fourier transform and normalizing the pixel values to be between 0 and 255.")
def create_image(image, n):
    # convert the image to grayscale and resize it
    gray_image = np.array(image.convert('L').resize((n, n), resample=Image.BILINEAR))
    
    # normalize the pixel values to be between -1 and 1
    normalized_image = (gray_image / 255.0) * 2 - 1
    
    return normalized_image


def plot_fourier_transform(image):
    # apply 2D Fourier transform
    f = fft2(image)
    
    # shift the zero frequency component to the center of the spectrum
    fshift = np.fft.fftshift(f)
    
    # plot the magnitude spectrum
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    fig, ax = plt.subplots()
    im = ax.imshow(magnitude_spectrum, cmap='gray')
    ax.axis('off')
    fig.colorbar(im, ax=ax)
    
    # return the Fourier spectrum
    return fshift, fig

def create_image_from_fourier(fshift):
    # shift the zero frequency component back to the top-left corner of the spectrum
    f = np.fft.ifftshift(fshift)
    
    # apply the inverse Fourier transform
    image = np.real(ifft2(f))
    
    # normalize the pixel values to be between 0 and 255
    normalized_image = ((image + 1) / 2.0) * 255.0
    
    return normalized_image.astype(np.uint8)



# allow the user to upload an image
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# if an image was uploaded, process it
if uploaded_file is not None:
    st.success("Image Uploaded Successfully")
        
    # load the image and display it
    col1, col2= st.columns(2)
    with col1:
        st.subheader('Original Image')
        image = Image.open(uploaded_file)
        st.image(image, width=300)
        
    
    # convert the image to grayscale and display it
    with col2:
        st.subheader('Grayscale Image')
        grayscale_image = image.convert('L')
        st.image(grayscale_image, width=300)
    
    
    # allow the user to specify the size of the image
    st.subheader("Image Size Slider")
    n = st.slider('Image size', min_value=32, max_value=1024, step=32)
    
    
    # create the image and display it
    st.subheader('Normalized Image')
    normalized_image = create_image(image, n)
    st.image(normalized_image, width=300, clamp=True)
    st.info("In image processing, normalization refers to the process of adjusting the values of an image so that they fall within a desired range. A normalized image typically has pixel values that range from 0 to 1 or from -1 to 1, which makes it easier to apply certain image processing techniques. Normalization can be used to improve contrast, remove noise, or prepare an image for analysis.")
    
    
    
    # apply the Fourier transform and display the magnitude spectrum
    st.subheader('Magnitude Spectrum')
    fshift, fig = plot_fourier_transform(normalized_image)
    st.pyplot(fig)
    st.info("The Fourier transform of an image represents sinusoidal gratings with different frequencies, amplitudes, orientations, and phases. The brighter dots indicate the prominent gratings, and the central dot represents the DC component, which is the average brightness of the image. Taking the logarithm of the Fourier transform reduces the central dot's brightness and reveals more subtle patterns.")
    
    
    # display the phase spectrum
    st.subheader('Phase Spectrum')
    st.write('Phase spectrum:')
    st.text(np.angle(fshift))
    st.info("The phase spectrum is the Fourier transform of an image, showing the phase angle associated with each frequency component. It provides information on the orientation and spatial relationships between different components in the image. By analyzing the phase spectrum, we can extract features and patterns that may not be immediately visible in the original image.")
    
    
    # create the image from the Fourier transform and display it
    st.subheader('Reconstructed Image')
    original_image = create_image_from_fourier(fshift)
    original_image = Image.fromarray(original_image)
    st.image(original_image, width=300)
    st.info("The reconstructed image derived from the Fourier transform of the original image is the image that has been reconstructed by taking the inverse Fourier transform of the Fourier transform of the original image. This process involves converting the Fourier transform, which is a representation of the image in the frequency domain, back into the spatial domain. The resulting image should be nearly identical to the original image, but may contain some small differences due to numerical errors or loss of information during the Fourier transform.")
    st.success('All operations ran successfully')


st.write('')
st.write('')

st.write('Made with :heart: by Yash Dantale')
    
