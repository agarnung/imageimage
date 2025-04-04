# imageimage

A Python program that converts images into image representations.

> [!WARNING]
> What?

Yeah, I mean, like this:

<p align="center">
  <img src="./assets/ex1.png" alt="ex1" title="ex1" style="display: inline-block; margin-right: 10px; width: 350px; height: 350px;" />
  <img src="./assets/ex1_imageified" alt="ex1_imageified" title="ex1_imageified" style="display: inline-block; width: 350px; height: 350px;" />
</p>
<br></br>
<p align="center">
  <img src="./assets/ex2.png" alt="ex2" title="ex2" style="display: inline-block; margin-right: 10px; width: 350px; height: 350px;" />
  <img src="./assets/ex2_imageified" alt="ex2_imageified" title="ex2_imageified" style="display: inline-block; width: 350px; height: 350px;" />
</p>

---

# Example of usage:

Clone the project:
```bash
git clone https://github.com/agarnung/imageimage.git
```

Install required dependencies (it is recommended tu use a virtual environment):
```bash
python3 -m pip install -r requirements.txt
```

> ![NOTE]
> Requirements generated with `pipreqs . --force`

Run the program in the root folder, e.g.:
```bash
python3 imageimage.py --file /home/alejandro/Pictures/lena.png --inputs ./image_database --out ./results 
```

Please refer to the program help:
```bash
python3 imageimage.py --help
```

---

# References:

- Inspired by [this](https://susanqq.github.io/UTKFace/icon/logoWall2.jpg) and [this](https://github.com/agarnung/asciimage/tree/main).

