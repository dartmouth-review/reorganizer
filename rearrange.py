import cv2
from os import listdir
from os.path import isfile, join
import os
import shutil

def rearrange(files):
    if "ordered" in files[0]:
        return False
    if len(files) % 4 != 0:
        return False
    new = []
    for i in range(0, len(files), 4):
        for j in range(2):
            new.append(files[i+j])
    for i in range(len(files)-4, -1, -4):
        for j in range(2,4):
            new.append(files[i+j])
    return new

def save(files, dir_path):
    extension = files[0].split(".")[-1]
    for i, file in enumerate(files):
        shutil.move(file, join(dir_path, f"ordered-{i}.{extension}"))

def scout_dir(dir_path="dir_test"):
    return ([x[0] for x in os.walk(dir_path) if len(x[0].split("/")) == 3])

def visualize(files):
    for file in files:
        image = cv2.imread(file)
        cv2.imshow("picture", image)
        cv2.waitKey(0)

def work_on_dir(dir_path="dir_test"):
    issues = scout_dir(dir_path=dir_path)
    for i, issue_path in enumerate(issues):
        files = [join(issue_path, f) for f in listdir(issue_path) if isfile(join(issue_path, f))]
        files = sorted(files, reverse=False)
        rearranged = rearrange(files)
        if rearranged != False:
            save(rearranged, issue_path)
        print(f"Processed {i+1} issues out of {len(issues)} | {((i/len(issues)) * 100):0.2f}%")



"""
TEST FUNCS
"""
def test():
    a = [1, 2, 11, 12, 3, 4, 9, 10, 5, 6, 7, 8]
    print(a)
    a = rearrange(a)
    print(a)

def test_with_files(dir_path="data"):
    files = [join(dir_path, f) for f in listdir(dir_path) if isfile(join(dir_path, f))]
    print(files)
    files = sorted(files, reverse=False)
    rearranged = rearrange(files)
    save(rearranged, dir_path)
    print(rearranged)



if __name__ == "__main__":
    # just call this function to the main directory path
    work_on_dir(dir_path="dir_test")
