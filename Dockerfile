FROM pytorch/pytorch

RUN apt-get update -y 
RUN apt-get upgrade -y 

RUN apt-get install -y --no-install-recommends build-essential \
         cmake \
         git \
         curl \
         vim \
         zip \
         unzip \
		 tmux \
		 curl \ 
		 wget \ 
		 ack \ 
		 gcc \ 
		 python-dev \ 
		 libaio-dev \ 
		 proxychains4 \ 
		 libtool \
		 autoconf \
		 pkg-config \
		 automake \
		 tcsh \ 
		 unixodbc-dev


RUN pip install --upgrade pip
RUN conda update conda
RUN conda update conda-build


RUN git clone https://github.com/fastai/fastai-docs.git --depth 1
RUN git clone https://github.com/fastai/fastai.git --depth 1  && git clone https://github.com/fastai/fastcore.git --depth 1
RUN git clone https://github.com/fastai/nbdev
RUN git clone https://github.com/fastai/nbdev_template



RUN git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
RUN sh ~/.vim_runtime/install_awesome_vimrc.sh


COPY environment.yaml ./environment.yaml
RUN conda env create -f environment.yaml

COPY download_models.py ./download_models.py
COPY download_testdata.py ./download_testdata.py
RUN python download_models.py 
RUN python download_testdata.py
