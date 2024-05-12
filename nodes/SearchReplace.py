# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗██████╗ ███████╗██████╗ ██╗      █████╗  ██████╗███████╗
# ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗██╔════╝██╔══██╗██║     ██╔══██╗██╔════╝██╔════╝
# ███████╗█████╗  ███████║██████╔╝██║     ███████║██████╔╝█████╗  ██████╔╝██║     ███████║██║     █████╗  
# ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║██╔══██╗██╔══╝  ██╔═══╝ ██║     ██╔══██║██║     ██╔══╝  
# ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║██║  ██║███████╗██║     ███████╗██║  ██║╚██████╗███████╗
# ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝
                                                                                                        
import random
import re

class SearchReplace:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "i_string": ("STRING", {"default": "string", "ForceInput": True}),
            "search_string": ("STRING", {"default": "", }),
            "replace_string": ("STRING", {"default": "", }),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("o_string",)
    FUNCTION = "searchreplace"
    CATEGORY = "👑 MokkaBoss1/Other"

    def searchreplace(self, i_string, search_string, replace_string,): 
        # Perform the search and replace
        o_string = i_string.replace(search_string, replace_string)
        return (o_string, )

NODE_CLASS_MAPPINGS = {"SearchReplace": SearchReplace}
NODE_DISPLAY_NAME_MAPPINGS = {"SearchReplace": "👑 SearchReplace"}

