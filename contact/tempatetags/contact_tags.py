from atexit import register
import re
from django import template
from contact.forms import ContactForm

register = template.Library()


@register.inclusion_tag("contacts/form.html")
def contact_form():
    return {"contact_form": ContactForm()}