# https://github.com/MokkaBoss1/ComfyUI_Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack 
#quick node to set SDXL-friendly aspect ratios showing their decimal values
# insprired by throttlekitty


# ███████╗██████╗ ██╗  ██╗██╗         ███████╗███╗   ███╗██████╗ ████████╗██╗   ██╗    ██╗      █████╗ ████████╗███████╗███╗   ██╗████████╗
# ██╔════╝██╔══██╗╚██╗██╔╝██║         ██╔════╝████╗ ████║██╔══██╗╚══██╔══╝╚██╗ ██╔╝    ██║     ██╔══██╗╚══██╔══╝██╔════╝████╗  ██║╚══██╔══╝
# ███████╗██║  ██║ ╚███╔╝ ██║         █████╗  ██╔████╔██║██████╔╝   ██║    ╚████╔╝     ██║     ███████║   ██║   █████╗  ██╔██╗ ██║   ██║   
# ╚════██║██║  ██║ ██╔██╗ ██║         ██╔══╝  ██║╚██╔╝██║██╔═══╝    ██║     ╚██╔╝      ██║     ██╔══██║   ██║   ██╔══╝  ██║╚██╗██║   ██║   
# ███████║██████╔╝██╔╝ ██╗███████╗    ███████╗██║ ╚═╝ ██║██║        ██║      ██║       ███████╗██║  ██║   ██║   ███████╗██║ ╚████║   ██║   
# ╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝     ╚═╝╚═╝        ╚═╝      ╚═╝       ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝   ╚═╝   
                                                                                                                                         


import torch

class SDXLEmptyLatent:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "batch_size": ("INT", {"default": 1, "min": 1, "max": 64}),
                    "aspectRatio": ([
                    "9:21 640x1536  (0.42)",
                    "9:19 704x1472  (0.48)",
                    "9:16 768x1344  (0.57)",
                    "5:8  768x1216  (0.63)",
                    "2:3  832x1216  (0.68)",
                    "3:4  896x1152  (0.78)",
                    "1:1  1024x1024 (1.00)",
                    "4:3  1152x896  (1.29)",
                    "3:2  1216x832  (1.46)",
                    "8:5  1216x768  (1.58)",
                    "16:9 1344x768  (1.75)",
                    "19:9 1472x704  (2.09)",
                    "21:9 1536x640  (2.40)"],)
            }
        }
    RETURN_TYPES = ("INT", "INT", "FLOAT", "LATENT", )
    RETURN_NAMES = ("Width", "Height", "Ratio", "Latent",)
    FUNCTION = "SDXL_AspectRatio"
    CATEGORY = "👑 MokkaBoss1/Image"

    def SDXL_AspectRatio(self, batch_size, aspectRatio):
        if aspectRatio == "1:1  1024x1024 (1.00)":
            width, height = 1024, 1024
        elif aspectRatio == "2:3  832x1216  (0.68)":
            width, height = 832, 1216
        elif aspectRatio == "3:4  896x1152  (0.78)":
            width, height = 896, 1152
        elif aspectRatio == "5:8  768x1216  (0.63)":
            width, height = 768, 1216
        elif aspectRatio == "9:16 768x1344  (0.57)":
            width, height = 768, 1344
        elif aspectRatio == "9:19 704x1472  (0.48)":
            width, height = 704, 1472
        elif aspectRatio == "9:21 640x1536  (0.42)":
            width, height = 640, 1536
        elif aspectRatio == "3:2  1216x832  (1.46)":
            width, height = 1216, 832
        elif aspectRatio == "4:3  1152x896  (1.29)":
            width, height = 1152, 896
        elif aspectRatio == "8:5  1216x768  (1.58)":
            width, height = 1216, 768
        elif aspectRatio == "16:9 1344x768  (1.75)":
            width, height = 1344, 768
        elif aspectRatio == "19:9 1472x704  (2.09)":
            width, height = 1472, 704
        elif aspectRatio == "21:9 1536x640  (2.40)":
            width, height = 1536, 640
        
        ratio = round(float(width/height),3)
        
        adj_width = width // 8
        adj_height = height // 8
        
        
        latent = torch.zeros([batch_size, 4, adj_height, adj_width])
        return (adj_width * 8, adj_height * 8, ratio, {"samples":latent}, )

            
NODE_CLASS_MAPPINGS = {
    "SDXLEmptyLatent": SDXLEmptyLatent
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXLEmptyLatent": "👑 SDXLEmptyLatent"
}