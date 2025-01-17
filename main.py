
from gtts import gTTS
import time 
import playsound
import cv2
import pytesseract
# Specify the path to the Tesseract executable (Windows only)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Read the image
image = cv2.imread('D://OEE.png')

# Convert to grayscale for better OCR results
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Preprocess the image (optional)
# Apply thresholding
_, thresholded_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

# Perform OCR on the image
text = pytesseract.image_to_string(thresholded_image, lang='eng')

# Print the recognized text
print("Extracted Text:")
print(text)

tts = gTTS(text=str(text), lang='en')
tts.save("sound.mp3")
time.sleep(3)
playsound.playsound("sound.mp3", True)