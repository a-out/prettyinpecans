import markdown
import uuid
from datetime import datetime
import os
import re

def preprocess_markdown(md_text):
    # remove [jump] signifier
    return re.sub(r'\[jump\]', '', md_text)

def render_markdown(md_text, images=[]):
    image_ref = ""

    for image in images:
        image_url = image.image.url
        image_ref = "{}\n[{}]: {}".format(image_ref, image, image_url)

    md = "{}\n{}".format(preprocess_markdown(md_text), image_ref)
    return markdown.markdown(md)

def before_jump(body):
    # return the section before the [jump] signifier
    return ''.join(body.split('[jump]')[:1])

def random_file_path(img_instance, filename):
    now = datetime.now()
    file_ext = filename.split('.')[-1]
    path =  "{y}/{m}/{n}.{e}".format(
        y=now.year,
        m=now.month,
        n=uuid.uuid4().hex,
        e=file_ext
    )
    return os.path.join('images', path)

def teaser(body, num_words):
    words = body.split(' ')[:num_words]
    truncated = ' '.join(words)
    return truncated + '...'