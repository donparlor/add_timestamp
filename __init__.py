from .services import add_timestamp_to_image

DOMAIN = "add_timestamp"

def setup(hass, config):
    hass.services.register(DOMAIN, "add_timestamp_to_image", add_timestamp_to_image)
    return True