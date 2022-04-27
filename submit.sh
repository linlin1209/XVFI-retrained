#!/bin/bash

#SBATCH --job-name test 
#SBATCH -N 1
#SBATCH -n 10
#SBATCH --gpus-per-node=2
#SBATCH -t 4:00:00
#SBATCH -A partner
#SBATCH -o del.out
#SBATCH -e del.err


python main.py --phase 'train' --exp_num 1 --dataset 'X4K1000FPS' --module_scale_factor 2 --S_trn 1 --S_tst 1
