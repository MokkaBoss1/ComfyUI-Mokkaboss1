# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack


# ██████╗ ██████╗  ██████╗ ███╗   ███╗██████╗ ████████╗███████╗██╗    ██╗██╗████████╗ ██████╗██╗  ██╗███████╗██████╗ 
# ██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██╔════╝██║    ██║██║╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗
# ██████╔╝██████╔╝██║   ██║██╔████╔██║██████╔╝   ██║   ███████╗██║ █╗ ██║██║   ██║   ██║     ███████║█████╗  ██████╔╝
# ██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██╔═══╝    ██║   ╚════██║██║███╗██║██║   ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗
# ██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║        ██║   ███████║╚███╔███╔╝██║   ██║   ╚██████╗██║  ██║███████╗██║  ██║
# ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝   ╚══════╝ ╚══╝╚══╝ ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                   
switch = ["1","2"]                                                                                                      


import random
import re

class PromptSwitcher:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "pos_prompt1": ("STRING", {"default": "# Positive Prompt #", "multiline": True}),
            "neg_prompt1": ("STRING", {"default": "# Negative Prompt #", "multiline": True}),
            "pos_prompt2": ("STRING", {"default": "# Positive Prompt #", "multiline": True}),
            "neg_prompt2": ("STRING", {"default": "# Negative Prompt #", "multiline": True}),
            "selection": ( switch,),
        }}

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("pos_prompt", "neg_prompt",)
    FUNCTION = "prompt_switcher"
    CATEGORY = "👑 MokkaBoss1/Text"

    def prompt_switcher(self, pos_prompt1, neg_prompt1, pos_prompt2, neg_prompt2, selection): 
        
        if selection == "1":
            pos_prompt = pos_prompt1
            neg_prompt = neg_prompt1
        else:
            pos_prompt = pos_prompt2
            neg_prompt = neg_prompt2
        
        return (pos_prompt, neg_prompt, )

NODE_CLASS_MAPPINGS = {"PromptSwitcher": PromptSwitcher}
NODE_DISPLAY_NAME_MAPPINGS = {"PromptSwitcher": "👑 PromptSwitcher"}
