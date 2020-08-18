"""
Downloads pretrained models using fastai2
"""
from fastai2.vision.all import * 
from fastai2.text.all import * 


print(list(model_meta.keys()))

vision_models = [xresnet18, xresnet34, xresnet50, xresnet101, resnet18, resnet34, resnet50, resnet101]
[m(pretrained=True) for m in vision_models]


text_models = [URLs.WT103_BWD, URLs.WT103_FWD, URLs.OPENAI_TRANSFORMER]
[untar_data(m, c_key='model') for m in text_models]