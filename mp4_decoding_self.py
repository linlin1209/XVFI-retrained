## You need ffmpeg version 4 to support the option '-pred mixed' which is new in version 4.
## The option '-pred mixed' gives smaller .png file size (lossless compression).
## The older version of ffmpeg also can be used without the option '-pred mixed'
## To install the ffmpeg version 4 in ubuntu, please run the below lines through terminal.

# conda install -c conda-forge ffmpeg

## Please modify the below code lines if needed.

import os, glob, sys

def check_folder(log_dir):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
#         print(log_dir, " created")
    return log_dir

try:
#################################################################
## Decode test set. About 6 GB with the option '-pred mixed'
#################################################################
#    test_types = sorted(glob.glob('./encoded_test/*/'))
#    for test_type in test_types:
#        samples = sorted(glob.glob(test_type + '*.mp4'))
#        for sample in samples:
#            new_dir = sample.replace('encoded_test','test').replace('.mp4','')
#            check_folder(new_dir)
#            cmd = "ffmpeg -i {} -pred mixed -start_number 0 {}/%04d.png".format(sample, new_dir)  # if ffmpeg version >= 4
#            # cmd = "ffmpeg -i {} -start_number 0 {}/%04d.png".format(sample, new_dir) # if ffmpeg version < 4
#            print(cmd)
#            if os.system(cmd):
#                raise KeyboardInterrupt


#################################################################
## Decode training set. About 240 GB with the option '-pred mixed'
#################################################################
    scenes = sorted(glob.glob('./self_filmed_encoded/*/'))
    for scene in scenes:
        samples = sorted(glob.glob(os.path.join(scene, '*.MOV')))
        for sample in samples:
            new_dir = sample.replace('self_filmed_encoded','self_filmed').replace('.MOV','')
            check_folder(new_dir)
            cmd = "ffmpeg -i {} -pred mixed -start_number 0 {}/%04d.png".format(sample, new_dir) # if ffmpeg version >= 4
            # cmd = "ffmpeg -i {} -start_number 0 {}/%04d.png".format(sample, new_dir) # if ffmpeg version < 4
            print(cmd)
            if os.system(cmd):
                raise KeyboardInterrupt

#################################################################
except KeyboardInterrupt:
    print("KeyboardInterrupt")
    sys.exit(0)
