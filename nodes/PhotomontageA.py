# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# ██████╗ ██╗  ██╗ ██████╗ ████████╗ ██████╗ ███╗   ███╗ ██████╗ ███╗   ██╗████████╗ █████╗  ██████╗ ███████╗     █████╗ 
# ██╔══██╗██║  ██║██╔═══██╗╚══██╔══╝██╔═══██╗████╗ ████║██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝    ██╔══██╗
# ██████╔╝███████║██║   ██║   ██║   ██║   ██║██╔████╔██║██║   ██║██╔██╗ ██║   ██║   ███████║██║  ███╗█████╗      ███████║
# ██╔═══╝ ██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██║   ██║██║╚██╗██║   ██║   ██╔══██║██║   ██║██╔══╝      ██╔══██║
# ██║     ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗    ██║  ██║
# ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝
                                                                                                                       
from PIL import Image
import numpy as np
import torch

# functions

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

def create_rect_image(hex_color, width, height):

    # Check if the hex_color is a valid hex code
    if not isinstance(hex_color, str) or not hex_color.startswith('#') or len(hex_color) not in [4, 7]:
        raise ValueError("Invalid hex color code. It should start with '#' followed by 3 or 6 hexadecimal characters.")
    
    # Create a new image with the given dimensions and color
    image = Image.new('RGB', (width, height), hex_color)
    
    return image


def resize_image(image, new_width, new_height):

    # Resize the image using ANTIALIAS filter (Lanczos) for high-quality downsampling
    resized_img = image.resize((new_width, new_height), Image.LANCZOS)

    return resized_img


def crop_image(image, target_aspect_ratio):

    img_width, img_height = image.size

    # Calculate the new width and height keeping aspect ratio
    if img_width / img_height > target_aspect_ratio:
        # Width is too large
        new_width = int(img_height * target_aspect_ratio)
        new_height = img_height
        left = (img_width - new_width) // 2
        upper = 0
        right = left + new_width
        lower = img_height
    else:
        # Height is too large
        new_height = int(img_width / target_aspect_ratio)
        new_width = img_width
        left = 0
        upper = (img_height - new_height) // 2
        right = img_width
        lower = upper + new_height

    # Define the crop box and crop
    crop_box = (left, upper, right, lower)
    cropped_image = image.crop(crop_box)
    return cropped_image


def superimpose_images(base_image, top_image, offset_x, offset_y):

    # Create a copy of base_image to avoid altering the original image
    result_image = base_image.copy()

    # If top_image has an alpha channel, use it as the mask
    if top_image.mode == 'RGBA':
        mask = top_image.split()[3]  # The alpha channel is the mask
        result_image.paste(top_image, (offset_x, offset_y), mask)
    else:
        result_image.paste(top_image, (offset_x, offset_y))

    return result_image


# main class

class PhotomontageA:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "spacing": ("INT", {"default": 0, "min": 0, "max": 500}),
            "unit_width": ("INT", {"default": 1024, "min": 512, "max": 99999}),
            "unit_height": ("INT", {"default": 1024, "min": 512, "max": 99999}),
            "rec1_image1": ("IMAGE", ),
            "rec1_image2": ("IMAGE", ),
            "rec1_image3": ("IMAGE", ),
            "rec2_image4": ("IMAGE", ),
            "rec2_image5": ("IMAGE", ),
            "rec1_image6": ("IMAGE", ),
            "rec1_image7": ("IMAGE", ),
            "rec1_image8": ("IMAGE", ),
            
        }}

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("output_image", "parameters")
    FUNCTION = "photomontage_a"
    CATEGORY = "👑 MokkaBoss1/Image"

    def photomontage_a(self, spacing, unit_width, unit_height, rec1_image1, rec1_image2, rec1_image3, rec2_image4, rec2_image5, rec1_image6, rec1_image7, rec1_image8): 
        
        #images loaded into comfyui via LoadImage have the format tensor and need to be converted to PIL before processing  
        
        # calculating the proper dimensions for all the elements
        
        page_width = int((4*spacing)+(3*unit_width))
        page_height = int((4*spacing)+(3*unit_height))
        rec1_image_width = unit_width
        rec1_image_height = unit_height
        rec2_image_width = unit_width
        rec2_image_height = int((spacing + 3*unit_height)/2)
        rec1_image_ar = round((rec1_image_width / rec1_image_height),3)
        rec2_image_ar = round((rec2_image_width / rec2_image_height),3)

        # create background

        background_image = create_rect_image("""#FFFFFF""", page_width, page_height)

        # crop all input images to correct dimensions
        
        image1 = crop_image(tensor2pil(rec1_image1), rec1_image_ar)
        image2 = crop_image(tensor2pil(rec1_image2), rec1_image_ar)
        image3 = crop_image(tensor2pil(rec1_image3), rec1_image_ar)
        image4 = crop_image(tensor2pil(rec2_image4), rec2_image_ar)
        image5 = crop_image(tensor2pil(rec2_image5), rec2_image_ar)
        image6 = crop_image(tensor2pil(rec1_image6), rec1_image_ar)
        image7 = crop_image(tensor2pil(rec1_image7), rec1_image_ar)
        image8 = crop_image(tensor2pil(rec1_image8), rec1_image_ar)      
        
        # resize images to calculated values
        
        image1 = resize_image(image1, rec1_image_width, rec1_image_height)
        image2 = resize_image(image2, rec1_image_width, rec1_image_height)
        image3 = resize_image(image3, rec1_image_width, rec1_image_height)     
        image4 = resize_image(image4, rec2_image_width, rec2_image_height)
        image5 = resize_image(image5, rec2_image_width, rec2_image_height)        
        image6 = resize_image(image6, rec1_image_width, rec1_image_height)
        image7 = resize_image(image7, rec1_image_width, rec1_image_height)
        image8 = resize_image(image8, rec1_image_width, rec1_image_height)        

 
        # superimpose images onto empty background
        
        background_image1 = (superimpose_images(background_image,  image1, spacing, spacing))
        background_image2 = (superimpose_images(background_image1, image2, spacing, ((2*spacing) + unit_height)))
        background_image3 = (superimpose_images(background_image2, image3, spacing, ((3*spacing) + (2*unit_height))))
        background_image4 = (superimpose_images(background_image3, image4, ((2*spacing) + unit_width), spacing))
        background_image5 = (superimpose_images(background_image4, image5, ((2*spacing) + unit_width), ((2*spacing) + rec2_image_height)))
        background_image6 = (superimpose_images(background_image5, image6, ((3*spacing)+(2*unit_width)), spacing))
        background_image7 = (superimpose_images(background_image6, image7, (3 * spacing) + (2 * unit_width), ((2*spacing) +unit_height)))
        output_image      = (superimpose_images(background_image7, image8, ((3*spacing)+(2*unit_width)), ((3*spacing) + (2*unit_height))))

        # return photomontage, parameters

        rec1_image_mp = round((rec1_image_height * rec1_image_width) / (1024*1024),3)
        rec2_image_mp = round((rec1_image_height * rec2_image_width) / (1024*1024),3)
        parameters = f"Rectangular1 image width: {rec1_image_width},\nRectangular1 image height: {rec1_image_height}\nRectangular1 image aspect ratio: {rec1_image_ar}\nRectangular1 image megapixels: {rec1_image_mp}\nRectangular2 image width: {rec2_image_width},\nRectangular2 image height: {rec2_image_height},\nRectangular2 image aspect ratio: {rec2_image_ar},\nRectangular2 image megapixels: {rec2_image_mp}\nPage width: {page_width},\nPage height: {page_height}"
        
        output_pil = pil2tensor(output_image)
        print("Type of output image:", type(output_pil))
        
        return (output_pil, parameters)

        


NODE_CLASS_MAPPINGS = {"PhotomontageA": PhotomontageA}
NODE_DISPLAY_NAME_MAPPINGS = {"PhotomontageA": "👑 PhotomontageA"}

