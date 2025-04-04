# imageimage

A Python program that converts images into image representations.

> [!NOTE] What?

Yeah, I mean, like this:

# Demo

<p align="center">
  <img src="./assets/ex1.png" alt="ex1" title="ex1" style="display: inline-block; margin-right: 10px; width: 350px; height: 350px;" />
  <img src="./assets/ex1_imageified" alt="ex1_imageified" title="ex1_imageified" style="display: inline-block; width: 350px; height: 350px;" />,
</p>
along with <a href="https://github.com/agarnung/asciimage/blob/main/assets/circle_ascii.txt" target="_blank">its .txt colleague.</a>
<br></br>
<p align="center">
  <img src="./assets/ex2.png" alt="ex2" title="ex2" style="display: inline-block; margin-right: 10px; width: 350px; height: 350px;" />
  <img src="./assets/ex2_imageified" alt="ex2_imageified" title="ex2_imageified" style="display: inline-block; width: 350px; height: 350px;" />,
</p>
along with <a href="https://github.com/agarnung/asciimage/blob/main/assets/lena_ascii.txt" target="_blank">its .txt colleague.</a>

---

### Example of usage:

Clone the project:
```bash
git clone https://github.com/agarnung/imageimage.git
```

Install required dependencies (it is recommended tu use a virtual environment):
```bash
python3 -m pip install -r requirements.txt
```

Run the program in the root folder, e.g.:
```bash
python3 imageimage.py --file /home/alejandro/Pictures/lena.png --inputs ./image_database --out ./results 
```

Please refer to the program help:
```bash
python3 asciimage.py --help
```

---

### References:

- [GeeksforGeeks: Converting Image to ASCII Image in Python](https://www.geeksforgeeks.org/converting-image-ascii-image-python/)
- [ASCII Art Generator](https://dahtah.github.io/imager/ascii_art.html)
- [GitHub: Image to ASCII by ajratnam](https://github.com/ajratnam/image-to-ascii)

---

### Other consulted links:

- [Python aalib (kaiju)](https://github.com/kaiju/python-aalib/tree/master)
- [Python aalib (jwilk)](https://github.com/jwilk/python-aalib)

---

### TODO:

- Improve the resolution of the image formed from the text, with `scale=1`.
- If an `int` argument is at the last of the command, EOF may corrupt the arg parsing. Protect this.
- Add color to letters in order to convert RGB images.
- Inspired by [this](https://susanqq.github.io/UTKFace/icon/logoWall2.jpg) and [this](https://github.com/agarnung/asciimage/tree/main).

