import base64
from io import BytesIO
from PIL import Image


def img_as_str(image_path: str) -> str:
    """Load img and convert it into a str

    Args:
        image_path (str): local filepath of image

    Returns:
        str: string as image
    """
    image = Image.open(image_path)
    image = image.resize((224, 224))
    buffered = BytesIO()
    image.save(buffered, format="JPEG")

    img_str = base64.b64encode(buffered.getvalue())
    return "data:image/jpeg;base64," + img_str.decode("ascii")