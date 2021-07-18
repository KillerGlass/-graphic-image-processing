#!/usr/bin/env python
# coding: utf-8

# In[151]:


import matplotlib.pyplot as plt
from skimage.io import imshow, imread,imread_collection
from skimage import color,exposure
from glob import glob
import numpy as np
import argparse


# In[152]:


def MultiPlot(rows=0, columns=0, width=10, height=30, dataset=None, formatImg="jpg"):
    
    '''
    A função subplots será usada para criar os boxes da imagem

    For para rows percorrerá as linhas e o for para cols pecorrerá as linhas

    K será usada como variavel de controle, para imagens

    '''
    args = argparse.ArgumentParser(description='multiple image plot')
    args.add_argument('--dataset', help='dataset para plot', type=str, default=None)
    args.add_argument('--rows', help='linhas do grafico', type=int, default=None)
    args.add_argument('--columns', help='colunas do grafico', type=int, default=None)
    args.add_argument('--height', help='altura da imagem', type=int, default=10)
    args.add_argument('--width', help='largura imagem', type=int, default=10)
    args.add_argument('--formatImg', help='formato das imagens', type=str, default="jpg")
    args = args.parse_args(["--dataset", dataset,
                           "--rows", str(rows),
                           '--columns',str(columns),
                           "--height", str(height),
                           "--width", str(width),
                           "--formatImg", formatImg])

    fig, ax = plt.subplots(args.rows, args.columns,figsize=(args.height,args.width))

    imagens = glob(args.dataset + '/*.' + args.formatImg)
    imagens = imread_collection(imagens)
    
    k = 0
    imshow(imagens[0])
    for i in range(args.rows):
        for j in range(args.columns):
            ax[i,j].imshow(imagens[k])
            if k < len(imagens):
                k+=1

    plt.show()


def MultiHistPlot(rows=0, columns=0, width=10, height=30, dataset=None, formatImg='jpg'):

    args = argparse.ArgumentParser(description='multiple-image histogram plot')
    args.add_argument('--dataset', help='dataset para plot', type=str, default=None)
    args.add_argument('--rows', help='linhas do grafico', type=int, default=None)
    args.add_argument('--columns', help='colunas do grafico', type=int, default=None)
    args.add_argument('--height', help='altura da imagem', type=int, default=30)
    args.add_argument('--width', help='largura imagem', type=int, default=10)
    args.add_argument('--formatImg', help='formato das imagens', type=str, default="jpg")
    args = args.parse_args(["--dataset", dataset,
                           "--rows", str(rows),
                           '--columns',str(columns),
                           "--height", str(height),
                           "--width", str(width),
                           "--formatImg", formatImg])

    fig, ax = plt.subplots(args.rows, args.columns,figsize=(args.height,args.width))

    imagens = glob(args.dataset + '/*.' + args.formatImg)
    imagens = imread_collection(imagens)

    k = 0
    for i in range(args.rows):
        for j in range(args.columns):
           
            #criando matriz de uns, usando as dimensoes e tamanho da imagem
            weights = np.ones(imagens[k].ravel().shape) / float(imagens[k].size)
            #criando grafico de histogramas
            ax[i,j].hist(imagens[k].flatten(), bins=256,weights=weights)
            if k < len(imagens):
                k+=1

    plt.show()    
        


# In[153]:


MultiHistPlot(2,3,10,dataset='imagem',formatImg='jpeg')


# In[154]:


dic = {"Map":[1,2,3,4,5],"Precision":[8,7,6,4,2],"Recall":[3,4,5,6,8],"Acuracia":[9,8,7,9,9]}


# In[155]:


import pandas as pd
df = pd.DataFrame(dic)
df


# In[156]:


def LearnPlot(Epochs=1,Dataset=None,MetricsName=None,Titulo="Grafico de Metricas",Eixo_x="Eixo X",Eixo_y="Eixo_Y",Height=8,Width=15, Save=False):

    Epochs = [x for x in range(Epochs)]
    plt.figure(figsize=(Width,Height))
    for i in MetricsName:
        
        plt.plot(Epochs,Dataset[i],label=i)
        plt.grid(True)
        plt.legend()
        
    plt.ylabel(Eixo_y)
    plt.xlabel(Eixo_x)

    if Save:
        plt.savefig(Titulo+'.svg')

    plt.show()


# In[20]:


LearnPlot(5, df,["Map","Precision","Recall","Acuracia"],"Grafico de metricas","Epoch","Result")


# In[189]:


def MultiImage(imagem=None, width=20, height=10, norm=True,gray=True,equa=True,equaGray=True):
   
    args = argparse.ArgumentParser(description='multiple-image histogram plot')
    args.add_argument('--imagem', help='dataset para plot', type=str, default=None)
    args.add_argument('--norm', help='linhas do grafico', type=bool, default=False)
    args.add_argument('--gray', help='colunas do grafico', type=bool, default=False)
    args.add_argument('--equa', help='colunas do grafico', type=bool, default=False)
    args.add_argument('--equaGray', help='colunas do grafico', type=bool, default=False)
    args.add_argument('--height', help='altura da imagem', type=int, default=10)
    args.add_argument('--width', help='largura imagem', type=int, default=30)

    args = args.parse_args(["--norm",str( norm),
                           '--gray',str(gray),
                           "--equa", str(equa),
                           "--equaGray", str(equaGray),
                           "--height", str(height),
                           "--width", str(width),
                            "--imagem", imagem,])

    args.imagem = imread(args.imagem)
    plt.figure(figsize=(args.width,args.height))
    
    if args.norm:
        plt.subplot(421), plt.imshow(args.imagem)
        weights = np.ones(args.imagem.ravel().shape) / float(args.imagem.size)
        plt.subplot(422),  plt.hist(args.imagem.flatten(), bins=256,weights=weights)
    if args.gray:
        img_gray = color.rgb2gray(args.imagem)
        plt.subplot(423), plt.imshow(img_gray,plt.cm.gray)
        weights = np.ones(img_gray.ravel().shape) / float(img_gray.size)
        plt.subplot(424),  plt.hist(img_gray.flatten(), bins=256,weights=weights)
        
    if args.equa:
        img_gray = exposure.equalize_hist(args.imagem)
        plt.subplot(425), plt.imshow(img_gray,plt.cm.gray)
        weights = np.ones(img_gray.ravel().shape) / float(img_gray.size)
        plt.subplot(426),  plt.hist(img_gray.flatten(), bins=256,weights=weights)
        
    if args.equaGray:
        img_gray = exposure.equalize_hist(color.rgb2gray(args.imagem))
        plt.subplot(427), plt.imshow(img_gray,plt.cm.gray)
        weights = np.ones(img_gray.ravel().shape) / float(img_gray.size)
        plt.subplot(428),  plt.hist(img_gray.flatten(), bins=256,weights=weights)


# In[190]:


MultiImage("imagem/The Grey Jay.jpeg",20,10)


# In[ ]:





# In[ ]:




