def bitwise_and(img1, img2, mask=None):
    # Check the dimensions of images
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions")
    # Check if mask is provided and has the same dimensions as the images
    if mask is not None and mask.shape[:2] != img1.shape[:2]:
        raise ValueError("Mask must have the same dimensions as the images")

    # Initialize result image
    result = np.zeros(img1.shape, dtype=np.uint8)

    # Apply bitwise AND to each pixel
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            # Check the mask value if mask is provided
            if mask is None or mask[i, j] == 255:  # Apply the operation only if no mask or mask value is 255
                for k in range(img1.shape[2]):  # Processing each channel (R, G, B)
                    result[i, j, k] = img1[i, j, k] & img2[i, j, k]

    return result


def bitwise_or(img1, img2, mask=None):
    # Check the dimensions of images
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions")
    # Check if mask is provided and has the same dimensions as the images
    if mask is not None and mask.shape[:2] != img1.shape[:2]:
        raise ValueError("Mask must have the same dimensions as the images")

    # Initialize result image
    result = np.zeros(img1.shape, dtype=np.uint8)

    # Apply bitwise OR to each pixel
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            # Check the mask value if mask is provided
            if mask is None or mask[i, j] == 255:  # Apply the operation only if no mask or mask value is 255
                for k in range(img1.shape[2]):  # Processing each channel (R, G, B)
                    result[i, j, k] = img1[i, j, k] | img2[i, j, k]

    return result


def bitwise_xor(img1, img2, mask=None):
    # Check the dimensions of images
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions")
    # Check if mask is provided and has the same dimensions as the images
    if mask is not None and mask.shape[:2] != img1.shape[:2]:
        raise ValueError("Mask must have the same dimensions as the images")

    # Initialize result image
    result = np.zeros(img1.shape, dtype=np.uint8)

    # Apply bitwise XOR to each pixel
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            # Check the mask value if mask is provided
            if mask is None or mask[i, j] == 255:  # Apply the operation only if no mask or mask value is 255
                for k in range(img1.shape[2]):  # Processing each channel (R, G, B)
                    result[i, j, k] = img1[i, j, k] ^ img2[i, j, k]

    return result


import numpy as np


def bitwise_not(img, mask=None):
    # Check if mask is provided and has the same dimensions as the images
    if mask is not None and mask.shape[:2] != img.shape[:2]:
        raise ValueError("Mask must have the same dimensions as the images")

    # Check the number of channels in the image
    if len(img.shape) == 2:
        num_channels = 1
    elif len(img.shape) == 3:
        num_channels = img.shape[2]
    else:
        raise ValueError("Invalid image shape")

    # Initialize result image
    result = np.zeros(img.shape, dtype=np.uint8)

    # Apply bitwise NOT to each pixel
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if mask is None or mask[i, j] == 255:  # Apply the operation only if no mask or mask value is 255
                if num_channels == 1:
                    result[i, j] = ~img[i, j]
                else:
                    for k in range(num_channels):  # Process each channel (R, G, B)
                        result[i, j, k] = ~img[i, j, k]

    return result
