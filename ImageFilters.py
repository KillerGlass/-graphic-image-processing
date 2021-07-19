#!/usr/bin/env python
# coding: utf-8

# In[115]:


import matplotlib.pyplot as plt
from skimage.io import imshow, imread,imread_collection
from sklearn.model_selection import train_test_split
from skimage import color,exposure
from glob import glob
import numpy as np
import argparse
import imageio
import os


# In[59]:


def DataFilters(dataset=None, Gray=True,equaHist=True,equaAdap=True,formatImg='jpg'):
   
    args = argparse.ArgumentParser(description='multiple-image histogram plot')
    args.add_argument('--dataset', help='dataset para plot', type=str, default=None)
    args.add_argument('--equaHist', help='colunas do grafico', type=bool, default=False)
    args.add_argument('--Gray', help='colunas do grafico', type=bool, default=False)
    args.add_argument('--equaAdap', help='colunas do grafico', type=bool, default=False)
    args.add_argument('--formatImg', help='formato das imagens', type=str, default="jpg")
    
    args = args.parse_args(["--dataset", dataset,
                           "--equaHist", str(equaHist),
                            "--equaAdap", str(equaAdap),
                            "--Gray", str(Gray),
                            "--formatImg", formatImg])
    
    args.dataset = glob(args.dataset + '/*.' + args.formatImg)
    args.dataset = imread_collection(args.dataset)
    if Gray:
        args.dataset = [color.rgb2gray(x) for x in args.dataset]
        
    if args.equaHist:
        args.dataset = [exposure.equalize_hist(x) for x in args.dataset]
        
    if args.equaAdap:
        args.dataset = [exposure.equalize_adapthist(x) for x in args.dataset]
    
  
    return args.dataset


# In[62]:


imagem = DataFilters(dataset='imagem',Gray=False,equaAdap=False,formatImg='jpeg')
imshow(imagem[0])


# In[ ]:


def DataFilters(dataset=None, Gray=True,equaHist=True,equaAdap=True,formatImg='jpg'):
   
    args = argparse.ArgumentParser(description='multiple-image histogram plot')
    args.add_argument('--dataset', help='dataset para plot', type=str, default=None)
    args.add_argument('--equaHist', help='colunas do grafico', type=bool, default=False)
    args.add_argument('--Gray', help='colunas do grafico', type=bool, default=False)
    args.add_argument('--equaAdap', help='colunas do grafico', type=bool, default=False)
    args.add_argument('--formatImg', help='formato das imagens', type=str, default="jpg")
    
    args = args.parse_args(["--dataset", dataset,
                           "--equaHist", str(equaHist),
                            "--equaAdap", str(equaAdap),
                            "--Gray", str(Gray),
                            "--formatImg", formatImg])
    
    args.dataset = glob(args.dataset + '/*.' + args.formatImg)
    args.dataset = imread_collection(args.dataset)
    if Gray:
        args.dataset = [color.rgb2gray(x) for x in args.dataset]
        
    if args.equaHist:
        args.dataset = [exposure.equalize_hist(x) for x in args.dataset]
        
    if args.equaAdap:
        args.dataset = [exposure.equalize_adapthist(x) for x in args.dataset]
    
  
    return args.dataset


# In[162]:


def EquaAdapthist(dataset,canal):
    dataset_canal = []
    for imagem in dataset:
        final_img = imagem
        for i in range(imagem.shape[0]):

            final_img[i][:,canal] = exposure.equalize_hist(imagem[i][:,2])
        dataset_canal.append(final_img)
        
    return dataset_canal


# In[163]:


def EquaHistograma(dataset,canal):
    dataset_canal = []
    for imagem in dataset:
        final_img = imagem
        for i in range(imagem.shape[0]):

            final_img[i][:,canal] = exposure.equalize_adapthist(imagem[i][:,2])
        dataset_canal.append(final_img)
        
    return dataset_canal


# In[166]:


def DataFilters(dataset=None,canal=None, equaHist=True,equaAdap=True,formatImg='jpg'):
   
    args = argparse.ArgumentParser(description='multiple-image histogram plot')
    args.add_argument('--dataset', help='dataset para plot', type=str, default=None)
    args.add_argument('--equaHist', help='colunas do grafico', type=bool, default=False)
    args.add_argument('--canal', help='colunas do grafico', type=str, default=None)
    args.add_argument('--equaAdap', help='colunas do grafico', type=bool, default=False)
    args.add_argument('--formatImg', help='formato das imagens', type=str, default="jpg")
    
    args = args.parse_args(["--dataset", dataset,
                           "--equaHist", str(equaHist),
                            "--equaAdap", str(equaAdap),
                            "--canal", canal,
                            "--formatImg", formatImg])
    
    args.dataset = glob(args.dataset + '/*.' + args.formatImg)
    args.dataset = imread_collection(args.dataset)
    
    dataset_canal = []
    
    if args.equaHist:
        if args.canal=='blue':
            dataset_canal = EquaHistograma(args.dataset,0)
            
        if args.canal=='red':
            dataset_canal = EquaHistograma(args.dataset,1)
            
        if args.canal=='green':
            dataset_canal = EquaHistograma(args.dataset,2)

    if args.equaAdap:
        
        if args.canal=='blue':
            dataset_canal = EquaAdapthist(args.dataset,0)
            
        if args.canal=='red':
            dataset_canal = EquaAdapthist(args.dataset,1)
            
        if args.canal=='green':
            dataset_canal = EquaAdapthist(args.dataset,2)

      
    return dataset_canal


# In[167]:


imagem = DataFilters(dataset='imagem',canal="green",equaAdap=False,formatImg='jpeg')
imshow(imagem[0])


# In[154]:


def PathSave(dataset,path):

    if not os.path.exists(path):
        os.makedirs(path)
    
    for i in dataset:
        img = imread(i)
        if '/' in i:
            ind = i.index('/')
            out, i = i.split('/') 
        imageio.imwrite(path + '/' + i, img) 
    


# In[155]:


def DataSplit(dataset=None,size_test=0.2, size_validation=0.1,path_train='Train',path_validation='Validation',path_test="Test",formatImg='jpg'):
    
    args = argparse.ArgumentParser(description='multiple-image histogram plot')
    args.add_argument('--dataset', help='dataset para plot', type=str, default=None)
    args.add_argument('--size_test', help='colunas do grafico', type=float, default=0.2)
    args.add_argument('--size_validation', help='colunas do grafico', type=float, default=0.1)
    args.add_argument('--path_train', help='dataset para plot', type=str, default="Train")
    args.add_argument('--path_test', help='dataset para plot', type=str, default="Test")
    args.add_argument('--path_validation', help='dataset para plot', type=str, default="Validation")
    args.add_argument('--formatImg', help='formato das imagens', type=str, default="jpg")
    
    args = args.parse_args(["--dataset", dataset,
                           "--size_test", str(size_test),
                            "--size_validation", str(size_validation),
                            "--path_validation",path_validation,
                            "--path_test",path_test,
                            "--path_train",path_train,
                            "--formatImg", formatImg])
    
    args.dataset = glob(args.dataset + '/*.' + args.formatImg)
    
    train,test = train_test_split(args.dataset,test_size=args.size_test,random_state=1)
    train,validation = train_test_split(train,test_size=args.size_validation,random_state=1)

    
    PathSave(train,args.path_train)
    
    PathSave(validation,args.path_validation)
    
    PathSave(test,args.path_test)
    
    train = imread_collection(train)
    test = imread_collection(test)
    validation = imread_collection(validation)
    

    
    return train,validation,test


# In[156]:


imagem = DataSplit(dataset='imagem',formatImg='jpeg')


# In[ ]:




