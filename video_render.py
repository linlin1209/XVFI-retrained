import os,shutil,subprocess

ori_dir  = os.getcwd()
main_folders = ['color_contrast_30fps','speed_30fps','rigid_30fps','self_filmed_30fps']
for main_folder in main_folders:
   os.chdir(main_folder)
   img_dirs = [ _ for _ in os.listdir() if os.path.isdir(_) ]
   for img_dir in img_dirs:
      os.chdir(img_dir)
      # use all the orginal pic to render the original 60 fps video using png files
      subprocess.call("ffmpeg -r 60 -i %04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p 60fps.mp4",shell=True)
      # split them into odd and even pics
      odd_count = 0 # since ffmpeg can only do consequtive (with out any break)
      even_count = 0
      imgs = [ _ for _ in os.listdir() if _.split('.')[-1] == 'png']
      imgs = sorted(imgs,key=lambda x:int(x.split('.')[0]))
      if os.path.isdir('odd') is False:
         os.makedirs('odd')
      if os.path.isdir('even') is False:
         os.makedirs('even')
      for img in imgs: 
         number  = int(img.split('.')[0])
         if number % 2 == 0:
            shutil.move(img,'even/{:04d}.png'.format(even_count))
            even_count += 1
         else:
            shutil.move(img,'odd/{:04d}.png'.format(odd_count))
            odd_count += 1
      # render 30 fps using even and odd png pics only
      os.chdir('odd')
      subprocess.call("ffmpeg -r 30 -i %04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p ../odd_30fps.mp4",shell=True)
      os.chdir('..')
      os.chdir('even')
      subprocess.call("ffmpeg -r 30 -i %04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p ../even_30fps.mp4",shell=True)
      os.chdir('..')
      
      os.chdir('..')
      
   os.chdir('..')
