# coding: utf-8
import os, fnmatch, random
from common.models import Attachment
from django.contrib.contenttypes.models import ContentType

cwd = os.getcwd()


def add_attachment(obj, is_main=True, is_secondary=False):
    attachment = Attachment(file=get_file(), object_id=obj.id,
                            content_type=ContentType.objects.get_for_model(obj), is_main=is_main,
                            is_secondary=is_secondary)
    attachment.save()


def add_doc_attachment(obj):
    attachment = Attachment(file="plv.xls", object_id=obj.id, content_type=ContentType.objects.get_for_model(obj),
                            is_main=False, comment="Дополнительный файл")
    attachment.save()


lorem = """
    <div>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab atque blanditiis consequuntur dolor dolorem
        doloremque dolorum ea, est id labore laborum modi numquam provident quaerat reprehenderit,
        temporibus veritatis voluptas voluptatum.
    </div>
"""

short_lorem = """
    <div>
        Temporibus veritatis voluptas
        voluptatum.
    </div>
"""

title = 'Temporibus veritatis voluptas'

attach_dir = "attachment/fixture"
media = "%s/media" % cwd
media_dir = "%s/%s" % (media, attach_dir)
attachments = []

for file_item in os.listdir(media_dir):
    if not fnmatch.fnmatch(file_item, "*_crop.jpg"): attachments.append(file_item)


def get_file():
    return "%s/%s" % (attach_dir, random.choice(attachments))
