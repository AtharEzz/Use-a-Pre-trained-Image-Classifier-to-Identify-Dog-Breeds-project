#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Athar Ezzeldin 
# DATE CREATED: 5th July 2024                                 
# REVISED DATE: 11th July 2024
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules

import os 
import re 


def extraxt_label (file_name):
    list_label=[]

    for f in file_name:
        
        remove_extintion= os.path.splitext(f)[0]  
        remove_digits = re.sub(r'[0-9]+','', remove_extintion)
       
        name=  remove_digits.replace("_", " ").strip().lower()
        list_label.append(name)
   
    return list_label
    
def create_label_file_dict(files, labels):
    
    
    
    create_dic = {}
    for file, label in zip (files, labels):
        if file not in create_dic:
            create_dic[file] = [label]
        else:
            print("** Warning: Duplicate files exist in directory:", 
                     file)
    
       
    return create_dic
    
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
   
    results_dic = {}
    files = os.listdir(image_dir)
    labels = extraxt_label (files)
    results_dic= create_label_file_dict(files, labels)
   
   
    return results_dic
