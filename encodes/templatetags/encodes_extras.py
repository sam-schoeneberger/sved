import datetime
import math
import zoneinfo

from django import template
from django.conf import settings


register = template.Library()


@register.filter
def datetime_duration(start: datetime.datetime, end: datetime.datetime) -> str:
    return str(end - start).split(".")[0]


@register.filter
def datetime_convert(dt: datetime.datetime) -> str:
    local_tz = zoneinfo.ZoneInfo(settings.TIME_ZONE)
    return dt.replace(tzinfo=zoneinfo.ZoneInfo("UTC")).astimezone(local_tz).strftime("%Y/%m/%d %R")


@register.filter
def profile_id_rename(profile_name: str) -> str:
    return profile_name.replace(".", "").replace(" ", "_").replace("(", "").replace(")", "")


@register.simple_tag
def conversion_rate(file_duration: int, start_time: datetime.datetime, end_time: datetime.datetime) -> str:
    return str(round(float(file_duration) / float((end_time - start_time).seconds), 2))


@register.simple_tag
def encode_rate(original_size: int, compressed_size: int) -> str:
    return f"{str(round((float(compressed_size) / float(original_size)) * 100.0, 2))}%"


@register.simple_tag
def format_bytes(file_size: int) -> str:
    if file_size and file_size > 0:
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(file_size, 1024)))
        s = round(file_size / math.pow(1024, i), 2)
        return "{}{}".format(s, size_name[i])
    else:
        return "0B"
