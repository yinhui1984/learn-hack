#!/usr/bin/env python3

from hanziconv import HanziConv # pip3 install hanziconv
import glob

def convert_to(oldFile, newFile, toSimplified=True):
    with open(oldFile, 'r', encoding='utf-8') as file:
        origin_text = file.read()

    if toSimplified:
        converted_text = HanziConv.toSimplified(origin_text)
    else:
        converted_text = HanziConv.toTraditional(origin_text)

    with open(newFile, 'w', encoding='utf-8') as file:
        file.write(converted_text)


if __name__ == '__main__':

    md_files = glob.glob('*.md')

    choice = input("Select:\n 1. convert to simple Chinese \n 2. convert to traditional Chinese: \n")

    if choice == '1':
        for md_file in md_files:
            convert_to(oldFile=md_file, newFile=md_file, toSimplified=True)
    elif choice == '2':
        for md_file in md_files:
            convert_to(oldFile=md_file, newFile=md_file, toSimplified=False)
    else:
        print("Invalid choice. Please select either 1 or 2.")

