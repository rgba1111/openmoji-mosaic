# OpenMoji Mosaic

<img width="640" alt="Example" src="https://github.com/rgba1111/openmoji-mosaic/assets/103372269/24edd64f-d6fd-4425-be1a-d1334e5b99bc">

## Algorithm
[Demo Video](https://vimeo.com/452873113)

Design of an algorithm for analyzing and sorting graphics.
Demonstration by creating a mosaic graphic.

The script anlyses the emoji to be displayed and rasterizes it by color values. On this matrix an emoji from the sorted library is placed, which corresponds to the closest matching average color value. Search, selection and placement is done by the automation library PyAutoGUI.
Sample database: OpenMoji (72 x 72 px, Color)

## How to use
* Make sure to have installed PyAutoGUI and Python3.
* Unzip the images folder or use your own set of images.
* Run the openmoji-mosaic.py in the same folders as the images or adjust the file directory specification in the script
### Options
* Use the bottom part of the code to clean and sort a custom set of images to use them as mosaic bits.
* Change the "goal.png" to get a different mosaic as result.

## Appendix
### Sources
* [OpenMoji](https://openmoji.org/)
* [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)

### Notes
Learn more on my website: [moritzkuhn.com](https://moritzkuhn.com/projects/OpenMoji-py)

OpenMoji is published under the Creative Commons Share Alike License 4.0: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/#)

Last tested 2020.
