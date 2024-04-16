from ComfyUI_Mokkaboss1.nodes.DoubleClipTextEncode import DoubleClipTextEncode
from ComfyUI_Mokkaboss1.nodes.HashText import HashText
from ComfyUI_Mokkaboss1.nodes.IndoorBackgrounds import IndoorBackgrounds
from ComfyUI_Mokkaboss1.nodes.LandscapeBackgrounds import LandscapeBackgrounds
from ComfyUI_Mokkaboss1.nodes.NatureColours import NatureColours
from ComfyUI_Mokkaboss1.nodes.OptimalCrop import OptimalCrop
from ComfyUI_Mokkaboss1.nodes.seveninabox import seveninabox
from ComfyUI_Mokkaboss1.nodes.UrbanColours import UrbanColours
from ComfyUI_Mokkaboss1.nodes.X_In_a_Dress import X_In_a_Dress
from ComfyUI_Mokkaboss1.nodes.X_In_a_Suit import X_In_a_Suit
from ComfyUI_Mokkaboss1.nodes.WrapText import WrapText
from ComfyUI_Mokkaboss1.nodes.AspectRatioCondition import AspectRatioCondition
from ComfyUI_Mokkaboss1.nodes.SDXLAspectRatioDec import SDXLAspectRatioDec
from ComfyUI_Mokkaboss1.nodes.ZoomCrop import ZoomCrop
from ComfyUI_Mokkaboss1.nodes.IntFloatDict import IntFloatDict
from ComfyUI_Mokkaboss1.nodes.WorkflowSettings import WorkflowSettings
from ComfyUI_Mokkaboss1.nodes.IntStringDict import IntStringDict
from ComfyUI_Mokkaboss1.nodes.ConnectImage import ConnectImage
from ComfyUI_Mokkaboss1.nodes.ConnectString import ConnectString
from ComfyUI_Mokkaboss1.nodes.ConnectInteger import ConnectInteger
from ComfyUI_Mokkaboss1.nodes.ConnectFloat import ConnectFloat
from ComfyUI_Mokkaboss1.nodes.ConnectLatent import ConnectLatent
from ComfyUI_Mokkaboss1.nodes.TimeStamp import TimeStamp
from ComfyUI_Mokkaboss1.nodes.SaveWithMetaData import SaveWithMetaData
from ComfyUI_Mokkaboss1.nodes.TricolorComposition import TricolorComposition
from ComfyUI_Mokkaboss1.nodes.Colors import Colors
from ComfyUI_Mokkaboss1.nodes.HSL import HSL
from ComfyUI_Mokkaboss1.nodes.EmbeddingLoader import EmbeddingLoader

NODE_CLASS_MAPPINGS = {
    "DoubleClipTextEncode": DoubleClipTextEncode,
    "HashText": HashText,
    "IndoorBackgrounds": IndoorBackgrounds,   
    "LandscapeBackgrounds": LandscapeBackgrounds,
    "NatureColours": NatureColours,
    "OptimalCrop": OptimalCrop,
    "seveninabox": seveninabox,
    "UrbanColours": UrbanColours,
    "X_In_a_Dress": X_In_a_Dress,
    "X_In_a_Suit": X_In_a_Suit,
    "WrapText": WrapText,
    "AspectRatioCondition": AspectRatioCondition,
    "SDXLAspectRatioDec": SDXLAspectRatioDec,
    "ZoomCrop": ZoomCrop,
    "IntFloatDict": IntFloatDict,
    "WorkflowSettings": WorkflowSettings,
    "IntStringDict": IntStringDict,
    "ConnectImage": ConnectImage,
    "ConnectInteger": ConnectInteger,
    "ConnectString": ConnectString,
    "ConnectFloat": ConnectFloat,
    "ConnectLatent": ConnectLatent,
    "TimeStamp": TimeStamp,
    "SaveWithMetaData": SaveWithMetaData,
    "TricolorComposition": TricolorComposition,
    "Colors": Colors,
    "HSL": HSL,
    "EmbeddingLoader": EmbeddingLoader,
    
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "DoubleClipTextEncode": "👑 DoubleClipTextEncode",
    "HashText": "👑 HashText",
    "IndoorBackgrounds": "👑 IndoorBackgrounds",
    "LandscapeBackgrounds": "👑 LandscapeBackgrounds",
    "NatureColours": "👑 NatureColours(deprecated)",
    "OptimalCrop": "👑 OptimalCrop",
    "seveninabox": "👑 7inabox(deprecated)",
    "UrbanColours": "👑 UrbanColours(deprecated)",
    "X_In_a_Dress": "👑 X_In_a_Dress",
    "X_In_a_Suit": "👑 X_In_a_Suit",
    "WrapText": "👑 WrapText",
    "AspectRatioCondition": "👑 AspectRatioCondition",
    "SDXLAspectRatioDec": "👑 SDXLAspectRatioDec",
    "ZoomCrop": "👑 ZoomCrop",
    "IntFloatDict": "👑 IntFloatDict",
    "WorkflowSettings": "👑 WorkflowSettings",
    "IntStringDict": "👑 IntStringDict",
    "ConnectImage": "👑 ConnectImage",
    "ConnectInteger": "👑 ConnectInteger",
    "ConnectString": "👑 ConnectString",
    "ConnectFloat": "👑 ConnectFloat",
    "ConnectLatent": "👑 ConnectLatent",
    "TimeStamp": "👑 TimeStamp",
    "SaveWithMetaData": "👑 SaveWithMetaData",
    "TricolorComposition": "👑 TricolorComposition",
    "Colors":"👑 Colors",
    "HSL", "👑 HSL",
    "EmbeddingLoader", "👑 EmbeddingLoader",
}
print ("👑 Mokkaboss1 28 Custom Nodes: Loaded")
