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


"""
Downloads test data used in FastAI
"""
from IPython import get_ipython
from fastai2.data.external import download_data, URLs
from fastai2.torch_core import parallel
import pickle

urls = ['ADULT_SAMPLE','BIWI_SAMPLE','CAMVID_TINY','CIFAR','COCO_TINY','IMDB','IMDB_SAMPLE',
        'ML_SAMPLE','MNIST','MNIST_SAMPLE','MNIST_TINY','PETS']
url_list = [URLs.__dict__[k] for k in urls]
files = [(print(f'Downloading {u}'), download_data(u)) for u in url_list]
