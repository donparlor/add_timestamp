import io
from PIL import Image, ImageDraw, ImageFont
from homeassistant.components.camera import DEFAULT_CONTENT_TYPE

def add_timestamp_to_image(hass, call):
    input_image_path = call.data.get("input_image_path")
    output_image_path = call.data.get("output_image_path")

    with open(input_image_path, "rb") as input_image_file:
        input_image = Image.open(input_image_file)

        draw = ImageDraw.Draw(input_image)
        font = ImageFont.load_default()

        timestamp = hass.states.get("sensor.date").state
        draw.text((10, 10), timestamp, font=font)

        input_image.save(output_image_path)