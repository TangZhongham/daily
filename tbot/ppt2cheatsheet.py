# transfer all pptx into cheatsheets.
# argparse,python-pptx,python-docx
import argparse
from pptx import Presentation


class Slides2CheatSheet():
    def __init__(self, slides_dir, slides_num=0):
        self.slides_dir = slides_dir
        self.slides_num = slides_num
        print("There are" + self.slides_num + "different slides under dir" + self.slides_dir + ".")
        return

    def read_slides(self):
        return

    def transfer(self):
        return "all text"

    def purify(self):
        return

    def save(self):
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This program is designed to extract all slides '
                                                 'and put it into one double paged letter sized docx file.')


    files = Slides2CheatSheet()
    files.transfer()