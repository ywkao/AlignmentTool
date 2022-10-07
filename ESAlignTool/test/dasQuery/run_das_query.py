#!/usr/bin/env python
import subprocess

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d", help = "Look for data events and dowload microAODs"  , action="store_true")
parser.add_argument("-q", help = "General das query"  , action="store_true")
args = parser.parse_args()

def exe(command):
    subprocess.call('echo "%s" >> lumi_2022b.txt' % command, shell=True)
    subprocess.call(command, shell=True)

def search():
    #subprocess.call('dasgoclient --query="file dataset=/EGamma/Run2022A-EcalESAlign-PromptReco-v1/ALCARECO" > list_2022a.txt', shell=True)
    #subprocess.call('dasgoclient --query="file dataset=/EGamma/Run2022B-EcalESAlign-PromptReco-v1/ALCARECO" > list_2022b.txt', shell=True)

    exe('echo "# init lumi" > lumi_2022b.txt')
    rootfiles = [
        "/store/data/Run2022B/EGamma/ALCARECO/EcalESAlign-PromptReco-v1/000/355/207/00000/a7b89716-0f32-4e93-b8eb-411f6c249a74.root", # 9720 
        "/store/data/Run2022B/EGamma/ALCARECO/EcalESAlign-PromptReco-v1/000/355/207/00000/1d603b01-c334-4dfc-9be9-c6e00c155364.root", # 46539
        "/store/data/Run2022B/EGamma/ALCARECO/EcalESAlign-PromptReco-v1/000/355/208/00000/15078f76-e399-45ef-9bc7-f3cb6fa4bd15.root", # 82511 
        "/store/data/Run2022B/EGamma/ALCARECO/EcalESAlign-PromptReco-v1/000/355/208/00000/36aeb8bd-e519-4703-ba1c-b5ef957b8c43.root", # 54356 
        "/store/data/Run2022B/EGamma/ALCARECO/EcalESAlign-PromptReco-v1/000/355/208/00000/3a7ae264-b873-407b-9cf1-e26b5d3770c8.root", # 55320 
        "/store/data/Run2022B/EGamma/ALCARECO/EcalESAlign-PromptReco-v1/000/355/208/00000/5d20fe70-69ff-4d9a-b411-e2e87234ae62.root", # 68503 
        "/store/data/Run2022B/EGamma/ALCARECO/EcalESAlign-PromptReco-v1/000/355/208/00000/88de3fea-582c-4de0-bdd3-226eebd5062b.root", # 77750 
        "/store/data/Run2022B/EGamma/ALCARECO/EcalESAlign-PromptReco-v1/000/355/208/00000/8b212576-55ad-49d9-9b32-34b8eac24265.root", # 71099 
        "/store/data/Run2022B/EGamma/ALCARECO/EcalESAlign-PromptReco-v1/000/355/208/00000/8cd10f57-9782-4791-a567-b2027859c894.root", # 64408 
        "/store/data/Run2022B/EGamma/ALCARECO/EcalESAlign-PromptReco-v1/000/355/208/00000/aab1e6a1-cd7b-41ea-bb73-987e92e40b02.root", # 70695 
        "/store/data/Run2022B/EGamma/ALCARECO/EcalESAlign-PromptReco-v1/000/355/208/00000/ee911dd4-28eb-470f-9a82-c2b2f43f5722.root", # 68491 
        "/store/data/Run2022B/EGamma/ALCARECO/EcalESAlign-PromptReco-v1/000/355/208/00000/fb817839-4c8f-4589-9640-9ee12a8fd5c8.root", # 55298 
        "/store/data/Run2022B/EGamma/ALCARECO/EcalESAlign-PromptReco-v1/000/355/208/00000/fd84ed0a-a472-4b16-936d-e8124d1ebb50.root", # 6143
    ]

    for f in rootfiles:
        command = 'dasgoclient --query="lumi file=%s" >> lumi_2022b.txt' % f
        exe(command)

def search_files():
    datasets = [
        #"/EGamma/Run2022A-EcalESAlign-PromptReco-v1/ALCARECO",
        "/EGamma/Run2022B-EcalESAlign-PromptReco-v1/ALCARECO",
        "/EGamma/Run2022C-EcalESAlign-PromptReco-v1/ALCARECO",
        #"/EGamma/Run2022D-EcalESAlign-PromptReco-v1/ALCARECO",
        "/EGamma/Run2022D-EcalESAlign-PromptReco-v2/ALCARECO",
        #"/EGamma/Run2022D-EcalESAlign-PromptReco-v3/ALCARECO",
        "/EGamma/Run2022E-EcalESAlign-PromptReco-v1/ALCARECO",
    ]

    for i, dataset in enumerate(datasets):
        command = 'dasgoclient --query="file dataset=%s" > new_files_0%d.txt' % (dataset, i)
        #command = 'dasgoclient --query="file dataset=%s"' % (dataset)
        exe(command)

if __name__ == "__main__":
    search_files()
    #search()
    print ">>> finished!"
