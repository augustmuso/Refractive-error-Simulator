import cv2
import numpy as np

class RefractiveErrorSimulator:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)

    def display_original_image(self):
        cv2.imshow('Original Image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def simulate_refractive_error(self, prescription):
        if 'DS' in prescription:
            # If 'DS' is present, simulate myopia or hyperopia
            sphere = float(prescription.replace('DS', ''))
            return self.simulate_myopia_or_hyperopia(sphere)
        elif 'DC' in prescription:
            # If 'DC' is present, simulate astigmatism
            cylinder = float(prescription.replace('DC', ''))
            return self.simulate_astigmatism(cylinder)
        else:
            # No refractive error, return the original image
            return self.image

    def simulate_myopia_or_hyperopia(self, sphere_strength):
        if sphere_strength > 0:
            # Simulate hyperopia
            return self.simulate_hyperopia(sphere_strength)
        elif sphere_strength < 0:
            # Simulate myopia
            return self.simulate_myopia(abs(sphere_strength))
        else:
            # No refractive error, return the original image
            return self.image

    def simulate_myopia(self, blur_strength):
        # Convert blur_strength to an integer
        blur_strength = int(blur_strength)
        
        # Ensure that the kernel size is odd
        ksize = (blur_strength * 2 + 1, blur_strength * 2 + 1)
        
        # Apply Gaussian blur to simulate myopia
        blurred_image = cv2.GaussianBlur(self.image, ksize, 0)
        return blurred_image

    def simulate_presbyopia(self, near_blur_strength):
        # Convert near_blur_strength to an integer
        near_blur_strength = int(near_blur_strength)
        
        # Ensure that the kernel size is odd
        ksize = (near_blur_strength * 2 + 1, near_blur_strength * 2 + 1)
        
        # Apply Gaussian blur to simulate presbyopia
        blurred_image = cv2.GaussianBlur(self.image, ksize, 0)
        return blurred_image

    def simulate_hyperopia(self, sphere_strength):
        sharpen_strength = 9 + sphere_strength
        sharpened_image = cv2.filter2D(self.image, -1, kernel=np.array([[-1, -1, -1], [-1, sharpen_strength, -1], [-1, -1, -1]]))
        return sharpened_image

    def simulate_astigmatism(self, cylinder_strength):
        # Create a meshgrid of coordinates
        rows, cols = self.image.shape[:2]
        x, y = np.meshgrid(np.arange(cols), np.arange(rows))

        # Apply distortion to the meshgrid
        x_distorted = x + cylinder_strength * np.sin(2 * np.pi * y / cols)
        y_distorted = y + cylinder_strength * np.sin(2 * np.pi * x / rows)

        # Use remap to apply the distortion to the image
        distorted_image = cv2.remap(self.image, x_distorted.astype(np.float32), y_distorted.astype(np.float32), interpolation=cv2.INTER_LINEAR)

        return distorted_image

# Example usage
image_path = r'C:\Users\mine\Desktop\Research\python\Refractive error Simulator\test.jpg'
simulator = RefractiveErrorSimulator(image_path)
simulator.display_original_image()

# Simulate myopia with a prescription of -2.00 DS
prescription = '-2.00DS'
myopia_image = simulator.simulate_refractive_error(prescription)
cv2.imshow('Myopia Simulation', myopia_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Simulate hyperopia with a prescription of +3.50 DS
prescription = '+3.50DS'
hyperopia_image = simulator.simulate_refractive_error(prescription)
cv2.imshow('Hyperopia Simulation', hyperopia_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Simulate astigmatism with a prescription of -1.25 DC
prescription = '-1.25DC'
astigmatism_image = simulator.simulate_refractive_error(prescription)
cv2.imshow('Astigmatism Simulation', astigmatism_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
