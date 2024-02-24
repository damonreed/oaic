from .client import get_client
import requests

client = get_client()


def image_response(image_prompt):
    image_url = (
        client.images.generate(
            model="dall-e-3",
            prompt=image_prompt,
        )
        .data[0]
        .url
    )

    # Get the image in bytes
    image = requests.get(image_url).content

    return image
