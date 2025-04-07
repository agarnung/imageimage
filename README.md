# imageimage

A Python program that converts images into image representations.

> [!WARNING]
> What?

Yeah, I mean, mosaics, like this:

<table border="1" align="center">
  <tr>
    <th>Original image</th>
    <th>Mosaic</th>
  </tr>
  <tr>
    <td><img src="assets/camera.png" alt="camera.png" title="camera.png" style="width: 350px; height: 350px;" /></td>
    <td><img src="assets/camera_imageified.jpg" alt="camera_imageified" title="camera_imageified" style="width: 350px; height: 350px;" /></td>
  </tr>
  <tr>
    <td><img src="assets/baboon.png" alt="baboon.png" title="baboon.png" style="width: 350px; height: 350px;" /></td>
    <td><img src="assets/baboon_imageified.jpg" alt="baboon_imageified" title="baboon_imageified" style="width: 350px; height: 350px;" /></td>
  </tr>
  <tr>
    <td><img src="assets/flor.png" alt="flor.png" title="flor.png" style="width: 350px; height: 350px;" /></td>
    <td><img src="assets/flor_imageified.jpg" alt="flor_imageified" title="flor_imageified" style="width: 350px; height: 350px;" /></td>
  </tr>
</table>

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
python3 imageimage.py --file /opt/imageimage/assets/camera.tif --inputs /opt/imageimage/image_database/ --cols 25 --rows 25 --color_weight 1.0 --gradient_weight 0.1
```

Please refer to the program help:
```bash
python3 imageimage.py --help
```

---

# References:

- Inspired by [UTKFace](https://susanqq.github.io/UTKFace/icon/logoWall2.jpg) and [asciimage](https://github.com/agarnung/asciimage/tree/main).

