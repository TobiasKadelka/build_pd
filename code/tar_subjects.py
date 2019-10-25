#!/usr/bin/env python
# coding: utf8
import os

inputPath = "/data/BnB1/BNM-ARC/MultiState_BACKUP/PD_raw/unzipped_PD_raw/PD_HHU/"
outputPath = "/data/BnB_USER/Kadelka/PD/source_data/"

# the next two functions just check, if under a certain file path are .dcm or .IMA files.
def is_IMA( folderpath ):
	for folder in os.listdir( folderpath ):
		if ".DS_Store" in folder:
			continue
		for file in os.listdir( folderpath + folder ):
			if ".IMA" in file:
				return True
	return False

def is_dcm( folderpath ):
	for folder in os.listdir( folderpath ):
		if ".DS_Store" in folder:
			continue
		for file in os.listdir( folderpath + folder ):
			if ".dcm" in file:
                        	return True
	return False


# the main function generates mkdir and find commands for creating tar balls per subjects in the outputPath.
def main():
	for subject in os.listdir(inputPath):
		if "DS_Store" in subject:
			continue
		if is_IMA(inputPath + subject + "/DICOM/"):
			print ("mkdir -p " + outputPath + subject + "/")
			print ("find " + inputPath + subject + "/DICOM/ -name \"*.IMA\" | tar -cvf " + outputPath + subject + "/" + subject + ".tar -T -")
		elif is_dcm(inputPath + subject + "/DICOM/"):
			print ("mkdir -p " + outputPath + subject + "/")
			print ("find " + inputPath + subject + "/DICOM/ -name \"*.dcm\" | tar -cvf " + outputPath + subject + "/" + subject + ".tar -T -")

main()
