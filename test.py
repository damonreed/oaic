from src.oaic.chat import chat_response
from src.oaic.image import image_response
from uuid import uuid4
import PIL.Image as Image
import io


system = """
You are a successful, bestselling hard fantasy and scifi author.  
You a master of language and subtlety.  
You avoid cliches and tropes and take pride in your originality.
You have a sense of humor in your work and you are not afraid to be dark and gritty.
"""

user = """
Develop a gritty fantasy plot outline for a graphic novel.  There is a slight steampunk aspect to the world.
The protagonist is a sly rogue named Lachance who is a master of disguise.  He is a bit of a loner and has a dark past.
His love interest is Rhiannah, a upright paladin who is a bit naive and idealistic.  She is a bit of a zealot and has a strong sense of justice.
One antagonist is Lachance's former lover Morbiena who is a rival rogue.  She is a femme fatale and has a very dark past.
The protagonist has pledged his loyalty to a powerful female firemage named Shalreah who runs a cirle of adventurers.
She has a noble bearing and mysterious motives.  She is a bit of a pyromaniac and has a dark sense of humor.  
Shalreah is supported by Solistah, a priest of the light who struggles with her own inner darkness.
"""

image_prompt = """
oil painting in the style of Disney's Haunted Mansion
fire mage from World of Warcraft
style is a mix of high fantasy and Victorian steampunk
She resembles Jessica Chastain and Gillian Anderson. 
Mid 40s, Dark red hair, green eyes, pale skin. Her hair is worn high in an up-do.  
She is dressed as a noblewoman in a green robe with gold trim.
Her arms are crossed and she is smiling very slightly.  
She is standing in front of a fireplace with a fire burning.
"""

imagepath = "~/Images/"
filename = f"{uuid4()}.png"

# print(chat_response(system, user))

# Create PIL image from generate_image
image_bytes = image_response(image_prompt)
image = Image.open(io.BytesIO(image_bytes))
image.show()
print(imagepath + filename)
image.save(imagepath + filename)
