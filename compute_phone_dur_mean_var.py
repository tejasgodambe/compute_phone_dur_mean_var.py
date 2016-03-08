#!/usr/bin/python 
#INPUT: 1) ref.ctm.txt 
#	2) hyp.ctm.txt  
#OUTPUT: REF_HYP_mn_var_stats.txt 

import sys
import numpy as np

REF = {}
HYP = {}
mean_REF = {}
mean_HYP = {}
std_REF = {}
std_HYP = {} 

# Read phone list 
for ph in open('ph_list.txt', 'r'):
	ph = ph.split('\n')[0]
	REF[ph] = []
	HYP[ph] = []

# Read Ref phone durations into hash of array. 
for line in open('mobileoffice_mod.ref.ctm.txt', 'r'):
	line = line.split('\n')[0]
	ph = line.split(' ')[-1]
	dur = line.split(' ')[-2]
	REF[ph].append(float(dur))

# Read Hyp phone durations into hash of array. 
for line in open('mobileoffice_mod.8.hyp.ctm.txt', 'r'):
	line = line.split('\n')[0]
	ph = line.split(' ')[-1]
	dur = line.split(' ')[-2]
	HYP[ph].append(float(dur))

# Compute means and std. dev. for each phone and print
f = open('REF_HYP_mn_var_stats.txt', 'w')
f.write('Phones' + '		' + '#phns' + '		' + 'Ref_mn' + '		' + 'Ref_sd' + '		' + '#phns' + '		' + 'Hyp_mn' + '		' + 'Hyp_sd' + '\n')
f.write('------------------------------------------------------------------------------------------------------------\n')
for ph in open('ph_list.txt', 'r'):
	ph = ph.split('\n')[0]
	mean_REF[ph] = round(np.mean(REF[ph]),2)
	std_REF[ph] = round(np.std(REF[ph]), 2)
	mean_HYP[ph] = round(np.mean(HYP[ph]), 2)
	std_HYP[ph] = round(np.std(HYP[ph]), 2)
	
        f.write(ph + '		' + str(len(REF[ph])) + '		' + str(mean_REF[ph]) + '		' + str(std_REF[ph]) + '		' + str(len(HYP[ph])) + '		' + str(mean_HYP[ph]) + '		' + str(std_HYP[ph]) + '\n')
f.close()
