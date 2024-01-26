# Refractive Error Simulator

This Python script simulates refractive errors such as myopia, hyperopia, and astigmatism on an input image. It uses the OpenCV library for image processing.

## Usage

1. Install the required dependencies:

    ```bash
    pip install opencv-python numpy
    ```

2. Modify the `image_path` variable in the script to point to your input image file.

3. Run the script:

    ```bash
    python refractive_error_simulator.py
    ```

4. Follow the on-screen instructions to view the original image and simulated refractive errors.

## Script Overview

- The script uses the `RefractiveErrorSimulator` class to perform simulations.
- It reads an input image specified by the `image_path`.
- Three types of refractive errors can be simulated: myopia, hyperopia, and astigmatism.
- The simulations are displayed using the OpenCV library.

## Example Usage

1. Display the original image:

    ```python
    simulator.display_original_image()
    ```

2. Simulate myopia with a prescription of -2.00 DS:

    ```python
    prescription = '-2.00DS'
    myopia_image = simulator.simulate_refractive_error(prescription)
    cv2.imshow('Myopia Simulation', myopia_image)
    ```

3. Simulate hyperopia with a prescription of +3.50 DS:

    ```python
    prescription = '+3.50DS'
    hyperopia_image = simulator.simulate_refractive_error(prescription)
    cv2.imshow('Hyperopia Simulation', hyperopia_image)
    ```

4. Simulate astigmatism with a prescription of -1.25 DC:

    ```python
    prescription = '-1.25DC'
    astigmatism_image = simulator.simulate_refractive_error(prescription)
    cv2.imshow('Astigmatism Simulation', astigmatism_image)
    ```

5. Close the image windows:

    ```python
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ```

Feel free to customize the script according to your needs. If you have any questions or issues, please let me know.

Dependencies
OpenCV: https://pypi.org/project/opencv-python/
NumPy: https://pypi.org/project/numpy/

License
This project is licensed under the MIT License - see the LICENSE file for details.
