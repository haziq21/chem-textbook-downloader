import grequests
from io import BytesIO
from PIL import Image

# Create a generator of unsent HTTP requests to each image URL
rs = (
    grequests.get(
        f"https://online.anyflip.com/kqdza/crea/files/mobile/{i}.jpg?1605684914"
    )
    for i in range(1, 314)
)


# Create an Image object out of each HTTP response
imgs = [Image.open(BytesIO(x.content)) for x in grequests.map(rs)]
# Write all the images to a PDF
imgs[0].save("textbook.pdf", save_all=True, append_images=imgs[1:])
