from math import log10, sqrt
from skimage.metrics import structural_similarity
import cv2
import os
import numpy as np
  
def PSNR(true,predict): 
    mse = np.mean((true - predict) ** 2)
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

def SSIM(true,predict):
   # 4. Convert the images to grayscale
   grayA = cv2.cvtColor(true, cv2.COLOR_BGR2GRAY)
   grayB = cv2.cvtColor(predict, cv2.COLOR_BGR2GRAY)

   # 5. Compute the Structural Similarity Index (SSIM) between the two
   #    images, ensuring that the difference image is returned
   (score, diff) = structural_similarity(grayA, grayB, full=True)
   diff = (diff * 255).astype("uint8")
   return score

  
def main():
   main_prefixes = ['speed','rigid','color_contrast']
   for main_prefix in main_prefixes:
      fps_60 = '../XVFI/{}_60fps'.format(main_prefix)
      fps_30 = '{}_30fps'.format(main_prefix)
      img_dirs = [ _ for _ in os.listdir(fps_60) if os.path.isdir('{}/{}'.format(fps_60,_)) ]
      for img_dir in img_dirs:
         f = open('result.txt','a')
         psnr_all = []
         ssim_all = []
         imgs = [ _ for _ in os.listdir('{}/{}/odd'.format(fps_60,img_dir)) if _.split('.')[-1] == 'png']
         imgs = sorted(imgs,key=lambda x:int(x.split('.')[0]))
         for img in imgs: 
            true = '{}/{}/odd/{}'.format(fps_60,img_dir,img)
            generate = '{}/{}/odd/{}'.format(fps_30,img_dir,img)
            if os.path.isfile(true) is False or os.path.isfile(generate) is False: continue
            true_img = cv2.imread(true)
            interpolate = cv2.imread(generate)
            value = PSNR(true_img, interpolate)
            ssim = SSIM(true_img, interpolate)
            psnr_all.append(value)
            ssim_all.append(ssim)
         print('{:<20s} {:<20s} psnr: {:<10.4f}, ssim: {:<10.4f}'.format(main_prefix,img_dir,np.mean(np.array(psnr_all)),np.mean(np.array(ssim_all))))
         f.write('{:<20s} {:<20s} psnr: {:<10.4f}, ssim: {:<10.4f}\n'.format(main_prefix,img_dir,np.mean(np.array(psnr_all)),np.mean(np.array(ssim_all))))
         f.close()
       
if __name__ == "__main__":
    main()
