#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Convert a GrotLoc ground truth output file to a Numpy ground truth
file compatible with VPR-Bench
"""
import ast
import numpy as np

def grotloc_to_numpy_gt(input_file, output_file, max_index):
    
    # First column is query image index, second column is list of indices
    #  of correct matches for the query images
    gt=np.zeros([max_index,2], dtype=object)
    indices = np.arange(max_index)
    gt[:,0] = indices
    gt[:,1] = [list() for _ in range(max_index)]

    with open(input_file, 'r') as file:
        for line in file:
            t = ast.literal_eval(line)
            gt[t[0]][1].append(t[1])
    print(gt)
    np.save(output_file, gt)


if __name__ == '__main__':
    INPUT_FILE = '/home/nsoncini/Documents/SLAM/datasets/KITTI_odom/grotloc_gt0/candidates_pairs.txt'
    OUTPUT_FILE = '/home/nsoncini/Documents/SLAM/VPR-Bench_work/datasets/KITTI_00/ground_truth_new.npy'
    MAX_INDEX = 4541

    grotloc_to_numpy_gt(INPUT_FILE, OUTPUT_FILE, MAX_INDEX)
