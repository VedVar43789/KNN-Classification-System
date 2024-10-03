"""
DSC 20 Project
Name(s): Ishaan Gosain , Vedant Vardhaan
PID(s):  A17855615, A17752898
Sources: None
"""

import numpy as np
import os
from PIL import Image

NUM_CHANNELS = 3


# --------------------------------------------------------------------------- #

def img_read_helper(path):
    """
    Creates an RGBImage object from the given image file
    """
    # Open the image in RGB
    img = Image.open(path).convert("RGB")
    # Convert to numpy array and then to a list
    matrix = np.array(img).tolist()
    # Use student's code to create an RGBImage object
    return RGBImage(matrix)


def img_save_helper(path, image):
    """
    Saves the given RGBImage instance to the given path
    """
    # Convert list to numpy array
    img_array = np.array(image.get_pixels())
    # Convert numpy array to PIL Image object
    img = Image.fromarray(img_array.astype(np.uint8))
    # Save the image object to path
    img.save(path)


# --------------------------------------------------------------------------- #

# Part 1: RGB Image #
class RGBImage:
    """
    Represents an image in RGB format
    """

    def __init__(self, pixels):
        """
        Initializes a new RGBImage object

        # Test with non-rectangular list
        >>> pixels = [
        ...              [[255, 255, 255], [255, 255, 255]],
        ...              [[255, 255, 255]]
        ...          ]
        >>> RGBImage(pixels)
        Traceback (most recent call last):
        ...
        TypeError

        # Test instance variables
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img.pixels
        [[[255, 255, 255], [0, 0, 0]]]
        >>> img.num_rows
        1
        >>> img.num_cols
        2
        """
        # YOUR CODE GOES HERE #
        # Raise exceptions here
        if not isinstance(pixels, list) or not pixels or \
                not all(isinstance(row, list) and row and len(row) == len(pixels[0]) for row in pixels) or \
                not all(isinstance(pixel, list) and len(pixel) == 3 for row in pixels for pixel in row) or \
                not all(0 <= intensity <= 255 and isinstance(intensity, int) for row in pixels for pixel in row for intensity in pixel):
            raise TypeError()
        self.pixels = pixels
        self.num_rows = len(pixels)
        self.num_cols = len(pixels[0])

    def size(self):
        """
        Returns the size of the image in (rows, cols) format

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img.size()
        (1, 2)
        """
        # YOUR CODE GOES HERE #
        return (self.num_rows,self.num_cols)

    def get_pixels(self):
        """
        Returns a copy of the image pixel array

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_pixels = img.get_pixels()

        # Check if this is a deep copy
        >>> img_pixels                               # Check the values
        [[[255, 255, 255], [0, 0, 0]]]
        >>> id(pixels) != id(img_pixels)             # Check outer list
        True
        >>> id(pixels[0]) != id(img_pixels[0])       # Check row
        True
        >>> id(pixels[0][0]) != id(img_pixels[0][0]) # Check pixel
        True
        """
        # YOUR CODE GOES HERE #
        
        return [[[k for k in j] for j in i]  for i in self.pixels]

    def copy(self):
        """
        Returns a copy of this RGBImage object

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_copy = img.copy()

        # Check that this is a new instance
        >>> id(img_copy) != id(img)
        True
        """
        # YOUR CODE GOES HERE #

        self.copy=RGBImage.get_pixels(self)
        return self.copy

    def get_pixel(self, row, col):
        """
        Returns the (R, G, B) value at the given position

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)

        # Test with an invalid index
        >>> img.get_pixel(1, 0)
        Traceback (most recent call last):
        ...
        ValueError

        # Run and check the returned value
        >>> img.get_pixel(0, 0)
        (255, 255, 255)
        """
        # YOUR CODE GOES HERE #

        if not type(row) ==int or not type(col)==int:
            raise TypeError()

        if not row<self.num_rows or not col<self.num_cols or not row>=0 or not col>=0:
            raise ValueError()

        return tuple(self.pixels[row][col])

    def set_pixel(self, row, col, new_color):
        """
        Sets the (R, G, B) value at the given position

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)

        # Test with an invalid new_color tuple
        >>> img.set_pixel(0, 0, (256, 0, 0))
        Traceback (most recent call last):
        ...
        ValueError

        # Check that the R/G/B value with negative is unchanged
        >>> img.set_pixel(0, 0, (-1, 0, 0))
        >>> img.pixels
        [[[255, 0, 0], [0, 0, 0]]]
        """
        # YOUR CODE GOES HERE #
        if not type(row) ==int or not type(col)==int:
            raise TypeError()
        if not row<self.num_rows or not col<self.num_cols or not row>=0 or not col>=0 or not all([i<=255 for i in new_color]):
            raise ValueError()
        if not isinstance(new_color,tuple) or not len(new_color)==3 or not all([isinstance(i,int) for i in new_color]):
            raise ValueError()

        cur_color=self.pixels[row][col]
        if new_color[0]>=0 and new_color[0]<=255:
            cur_color[0]=new_color[0]
        if new_color[1]>=0 and new_color[1]<=255:
            cur_color[1]=new_color[1]
        if new_color[2]>=0 and new_color[2]<=255:
            cur_color[2]=new_color[2]
        
        self.pixels[row][col]=cur_color
        





# Part 2: Image Processing Template Methods #
class ImageProcessingTemplate:
    """
    Contains assorted image processing methods
    Intended to be used as a parent class
    """

    def __init__(self):
        """
        Creates a new ImageProcessingTemplate object

        # Check that the cost was assigned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost
        0
        """
        # YOUR CODE GOES HERE #
        self.cost = 0

    def get_cost(self):
        """
        Returns the current total incurred cost

        # Check that the cost value is returned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost = 50 # Manually modify cost
        >>> img_proc.get_cost()
        50
        """
        # YOUR CODE GOES HERE #
        return self.cost

    def negate(self, image):
        """
        Returns a negated copy of the given image

        # Check if this is returning a new RGBImage instance
        >>> img_proc = ImageProcessingTemplate()
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_negate = img_proc.negate(img)
        >>> id(img) != id(img_negate) # Check for new RGBImage instance
        True

        # The following is a description of how this test works
        # 1 Create a processor
        # 2/3 Read in the input and expected output
        # 4 Modify the input
        # 5 Compare the modified and expected
        # 6 Write the output to file
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()                            # 1
        >>> img = img_read_helper('img/test_image_32x32.png')                 # 2
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_negate.png')  # 3
        >>> img_negate = img_proc.negate(img)                               # 4
        >>> img_negate.pixels == img_exp.pixels # Check negate output       # 5
        True
        >>> img_save_helper('img/out/test_image_32x32_negate.png', img_negate)# 6
        """
        # YOUR CODE GOES HERE #
        new_image=[]
        pixels=image.copy()
        new_image=RGBImage([ [[  255-k for k in j]for j in i] for i in pixels])
        return new_image

    def grayscale(self, image):
        """
        Returns a grayscale copy of the given image

        # See negate for info on this test
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_gray.png')
        >>> img_gray = img_proc.grayscale(img)
        >>> img_gray.pixels == img_exp.pixels # Check grayscale output
        True
        >>> img_save_helper('img/out/test_image_32x32_gray.png', img_gray)
        """
        # YOUR CODE GOES HERE #
        pixels=image.copy()
        new_image=RGBImage([ [[sum(j)//3,sum(j)//3,sum(j)//3]for j in i]   for i in pixels])
        return new_image


    def rotate_180(self, image):
        """
        Returns a rotated version of the given image

        # See negate for info on this test
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_rotate.png')
        >>> img_rotate = img_proc.rotate_180(img)
        >>> img_rotate.pixels == img_exp.pixels # Check rotate_180 output
        True
        >>> img_save_helper('img/out/test_image_32x32_rotate.png', img_rotate)
        """
        # YOUR CODE GOES HERE #
        pixels=image.copy()
        
        #new_image=[ [ pixels[j][targetX]  for j in range(image.num_rows)]  for i in range(image.num_cols)//2 ] 
        new_image=[ [pixels[j] [i] for j in range(image.num_rows)] for i in range(image.num_cols) ]
        rotate=[ i[::-1]   for i in new_image]
        new_image1=[ [rotate[i] [j] for i in range(len(rotate[0]))] for j in range (len(rotate))]
        new_image2=RGBImage([ j[::-1] for j in new_image1])
        return new_image2

    def get_average_brightness(self, image):
        """
        Returns the average brightness for the given image

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_proc.get_average_brightness(img)
        86
        """
        # YOUR CODE GOES HERE #
        pixels=image.copy()
        lst=[ sum(j)//3  for i in pixels for j in i]
        return sum(lst)//len(lst)

    def adjust_brightness(self, image, intensity):
        """
        Returns a new image with adjusted brightness level

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_adjusted.png')
        >>> img_adjust = img_proc.adjust_brightness(img, 75)
        >>> img_adjust.pixels == img_exp.pixels # Check adjust_brightness
        True
        >>> img_save_helper('img/out/test_image_32x32_adjusted.png', img_adjust)
        """
        # YOUR CODE GOES HERE #
        pixels=image.copy()
        new_image=RGBImage([ [[ k+intensity if k+intensity >0 and k+intensity<=255 else 0 if k+intensity <0 else 255 for k in j]for j in i ]   for i in pixels])
        return new_image

    def blur(self, image):
        """
        Returns a new image with the pixels blurred

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_blur.png')
        >>> img_blur = img_proc.blur(img)
        >>> img_blur.pixels == img_exp.pixels # Check blur
        True
        >>> img_save_helper('img/out/test_image_32x32_blur.png', img_blur)
        """
        # YOUR CODE GOES HERE #
        new_pixels = []

        for i in range(image.num_rows):
            new_row = []
            for j in range(image.num_cols):
                r_sum, g_sum, b_sum = 0, 0, 0
                count = 0

                for x in range(max(0, i - 1), min(image.num_rows, i + 2)):
                    for y in range(max(0, j - 1), min(image.num_cols, j + 2)):
                        r, g, b = image.pixels[x][y]
                        r_sum += r
                        g_sum += g
                        b_sum += b
                        count += 1

              
                r_avg=r_sum // count
                g_avg=g_sum // count
                b_avg= b_sum // count

                new_row.append([r_avg, g_avg, b_avg])

            new_pixels.append(new_row)

        return RGBImage(new_pixels)



# Part 3: Standard Image Processing Methods #
class StandardImageProcessing(ImageProcessingTemplate):
    """
    Represents a standard tier of an image processor
    """
    

    def __init__(self):
        """
        Creates a new StandardImageProcessing object

        # Check that the cost was assigned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost
        0
        """
        # YOUR CODE GOES HERE #
        self.cost = 0
        self.coupon=0

    def negate(self, image):
        """
        Returns a negated copy of the given image

        # Check the expected cost
        >>> img_proc = StandardImageProcessing()
        >>> img_in = img_read_helper('img/square_32x32.png')
        >>> negated = img_proc.negate(img_in)
        >>> img_proc.get_cost()
        5

        # Check that negate works the same as in the parent class
        >>> img_proc = StandardImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_negate.png')
        >>> img_negate = img_proc.negate(img)
        >>> img_negate.pixels == img_exp.pixels # Check negate output
        True
        """
        # YOUR CODE GOES HERE #
        if self.coupon==0:
            self.cost+=5
        else:
            self.coupon-=1
        

        return super().negate(image)

    def grayscale(self, image):
        """
        Returns a grayscale copy of the given image
        >>> img_proc = StandardImageProcessing()
        >>> img_in = img_read_helper('img/square_32x32.png')
        >>> grayscale = img_proc.grayscale(img_in)
        >>> img_proc.get_cost()
        6
        """
        # YOUR CODE GOES HERE #
        if self.coupon==0:
            self.cost+=6
        else:
            self.coupon-=1
        return super().grayscale(image)

    def rotate_180(self, image):
        """
        Returns a rotated version of the given image
        >>> img_proc = StandardImageProcessing()
        >>> img_in = img_read_helper('img/square_32x32.png')
        >>> rotate = img_proc.rotate_180(img_in)
        >>> img_proc.get_cost()
        10
        """
        # YOUR CODE GOES HERE #
        if self.coupon==0:
            self.cost+=10
        else:
            self.coupon-=1
        return super().rotate_180(image)

    def adjust_brightness(self, image, intensity):
        """
        Returns a new image with adjusted brightness level
        
        """
        # YOUR CODE GOES HERE #
        if self.coupon==0:
            self.cost+=1
        else:
            self.coupon-=1
        return super().adjust_brightness(image)

    def blur(self, image):
        """
        Returns a new image with the pixels blurred
        """
        # YOUR CODE GOES HERE #
        if self.coupon==0:
            self.cost+=5
        else:
            self.coupon-=1
        return super().blur(image)

    def redeem_coupon(self, amount):
        """
        Makes the given number of methods calls free

        # Check that the cost does not change for a call to negate
        # when a coupon is redeemed
        >>> img_proc = StandardImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_proc.redeem_coupon(1)
        >>> img = img_proc.rotate_180(img)
        >>> img_proc.get_cost()
        0
        
        """
        # YOUR CODE GOES HERE #
        if type(amount) != int:
            raise TypeError()
        if amount <=0:
            raise  ValueError()
        self.coupon+=amount



# Part 4: Premium Image Processing Methods #
class PremiumImageProcessing(ImageProcessingTemplate):
    """
    Represents a paid tier of an image processor
    """

    def __init__(self):
        """
        Creates a new PremiumImageProcessing object

        # Check the expected cost
        >>> img_proc = PremiumImageProcessing()
        >>> img_proc.get_cost()
        50
        """
        # YOUR CODE GOES HERE #
        self.cost = 50

    def chroma_key(self, chroma_image, background_image, color):
        """
        Returns a copy of the chroma image where all pixels with the given
        color are replaced with the background image.

        # Check output
        >>> img_proc = PremiumImageProcessing()
        >>> img_in = img_read_helper('img/square_32x32.png')
        >>> img_in_back = img_read_helper('img/test_image_32x32.png')
        >>> color = (255, 255, 255)
        >>> img_exp = img_read_helper('img/exp/square_32x32_chroma.png')
        >>> img_chroma = img_proc.chroma_key(img_in, img_in_back, color)
        >>> img_chroma.pixels == img_exp.pixels # Check chroma_key output
        True
        >>> img_save_helper('img/out/square_32x32_chroma.png', img_chroma)
        """
        # YOUR CODE GOES HERE #
        if not isinstance(chroma_image,RGBImage) or not isinstance(background_image,RGBImage):
            raise TypeError()
        if not chroma_image.num_rows==background_image.num_rows and not chroma_image.num_cols==background_image.num_cols:
            raise ValueError()
        
        pixel_chroma=chroma_image.copy()
        new=RGBImage(pixel_chroma)
        back_pixel=background_image.copy()
        for i in range(background_image.num_rows):
            
            for j in range(background_image.num_cols):
                 if pixel_chroma[i][j]==list(color):
                     new.set_pixel(i,j,tuple(back_pixel[i][j]))
                 
            
        return new


    
    def sticker(self, sticker_image, background_image, x_pos, y_pos):
        """
        Returns a copy of the background image where the sticker image is
        placed at the given x and y position.

        # Test with out-of-bounds image and position size
        >>> img_proc = PremiumImageProcessing()
        >>> img_sticker = img_read_helper('img/square_6x6.png')
        >>> img_back = img_read_helper('img/test_image_32x32.png')
        >>> x, y = (31, 0)
        >>> img_proc.sticker(img_sticker, img_back, x, y)
        Traceback (most recent call last):
        ...
        ValueError

        # Check output
        >>> img_proc = PremiumImageProcessing()
        >>> img_sticker = img_read_helper('img/square_6x6.png')
        >>> img_back = img_read_helper('img/test_image_32x32.png')
        >>> x, y = (3, 3)
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_sticker.png')
        >>> img_combined = img_proc.sticker(img_sticker, img_back, x, y)
        >>> img_combined.pixels == img_exp.pixels # Check sticker output
        True
        >>> img_save_helper('img/out/test_image_32x32_sticker.png', img_combined)
        """
        # YOUR CODE GOES HERE #

        if not isinstance(sticker_image,RGBImage) or not isinstance(background_image,RGBImage):
            raise TypeError()
        if sticker_image.num_rows > background_image.num_rows or sticker_image.num_cols > background_image.num_cols:
            raise ValueError()
        if not isinstance(x_pos, int) or not isinstance(y_pos, int):
            raise TypeError()
        if x_pos + sticker_image.num_rows > background_image.num_rows or y_pos + sticker_image.num_cols > background_image.num_cols:
            raise ValueError()

        copy=background_image.copy()
        new=RGBImage(copy)

        
        for i in range(sticker_image.num_rows):
            for j in range(sticker_image.num_cols):

                new.set_pixel(x_pos+i,y_pos+j,tuple(sticker_image.get_pixel(i,j)))
        return new
     

    def edge_highlight(self, image):
        """
        Returns a new image with the edges highlighted

        # Check output
        >>> img_proc = PremiumImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_edge = img_proc.edge_highlight(img)
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_edge.png')
        >>> img_exp.pixels == img_edge.pixels # Check edge_highlight output
        True
        >>> img_save_helper('img/out/test_image_32x32_edge.png', img_edge)
        """
        # YOUR CODE GOES HERE #

        img_copy = image.copy()
        channel = [[sum(col)//3 for col in row] for row in img_copy]

        kernel = [
            [-1,-1,-1],
            [-1,8, -1],
            [-1,-1,-1]
        ]
  
        edged_image = []
        for i in range(len(channel)):
            edged_row = []
            for j in range(len(channel[0])):
                edge_value = 0
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if 0 <= i + x < len(channel) and 0 <= j + y < len(channel[0]):
                            edge_value += channel[i + x][j + y] * kernel[x + 1][y + 1]
                edge_value = max(0, min(edge_value, 255))
                edged_row.append(edge_value)
            edged_image.append(edged_row)

        final_edged_img = [[[val,val,val] for val in row] for row in edged_image]
        return RGBImage(final_edged_img)


# Part 5: Image KNN Classifier #
class ImageKNNClassifier:
    """
    Represents a simple KNNClassifier
    """

    def __init__(self, k_neighbors):
        """
        Creates a new KNN classifier object
        """
        # YOUR CODE GOES HERE #
        self.k_neighbors=k_neighbors

    def fit(self, data):
        """
        Stores the given set of data and labels for later
        """
        # YOUR CODE GOES HERE #
        if len(data)<self.k_neighbors:
            raise ValueError()
        self.data=data

    def distance(self, image1, image2):
        """
        Returns the distance between the given images

        >>> img1 = img_read_helper('img/steve.png')
        >>> img2 = img_read_helper('img/knn_test_img.png')
        >>> knn = ImageKNNClassifier(3)
        >>> knn.distance(img1, img2)
        15946.312896716909
        """
        # YOUR CODE GOES HERE #
        if not isinstance(image1,RGBImage) or not isinstance(image2,RGBImage):
            raise TypeError()

        if not image1.num_cols==image2.num_cols or not \
image1.num_rows==image2.num_rows:
            raise ValueError()

        square= sum((image1.get_pixel(i, j)[p] - \
image2.get_pixel(i, j)[p])**2 for i in range(image1.num_rows) \
for j in range(image1.num_cols) for p in range(3))
        return square**0.5


    def vote(self, candidates):
        """
        Returns the most frequent label in the given list

        >>> knn = ImageKNNClassifier(3)
        >>> knn.vote(['label1', 'label2', 'label2', 'label2', 'label1'])
        'label2'
        """
        # YOUR CODE GOES HERE #
        d={}
        for i in candidates:
            if i not in d:
                d[candidates.count(i)]=i 
        maxi=max(d)
        return d[maxi]



    def predict(self, image):
        """
        Predicts the label of the given image using the labels of
        the K closest neighbors to this image

        The test for this method is located in the knn_tests method below
        """
        # YOUR CODE GOES HERE #
        if not self.data:
            raise ValueError()

        distances = [(self.distance(image, data_image), label) for \
data_image, label in self.data]

        sorted_distances = sorted(distances, key=lambda x: x[0])\
[:self.k_neighbors]

        neighbors_labels = [label for distance, label in sorted_distances]

        predicted_label = self.vote(neighbors_labels)
        return predicted_label


def knn_tests(test_img_path):
    """
    Function to run knn tests

    >>> knn_tests('img/knn_test_img.png')
    'nighttime'
    """
    # Read all of the sub-folder names in the knn_data folder
    # These will be treated as labels
    path = 'knn_data'
    data = []
    for label in os.listdir(path):
        label_path = os.path.join(path, label)
        # Ignore non-folder items
        if not os.path.isdir(label_path):
            continue
        # Read in each image in the sub-folder
        for img_file in os.listdir(label_path):
            train_img_path = os.path.join(label_path, img_file)
            img = img_read_helper(train_img_path)
            # Add the image object and the label to the dataset
            data.append((img, label))

    # Create a KNN-classifier using the dataset
    knn = ImageKNNClassifier(5)

    # Train the classifier by providing the dataset
    knn.fit(data)

    # Create an RGBImage object of the tested image
    test_img = img_read_helper(test_img_path)

    # Return the KNN's prediction
    predicted_label = knn.predict(test_img)
    return predicted_label