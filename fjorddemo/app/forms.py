from django import forms
from django.conf import settings


class NewJSONUploadForm(forms.Form):
    file_field_names = ["file_upload"]
    file_upload = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "accept": ",".join(
                    settings.ALLOWED_JSON_CONTENT_TYPES
                    + settings.ALLOWED_JSON_EXTENSIONS
                )
            }
        ),
        label="",
    )


class NewJSONTextForm(forms.Form):
    file_field_names: list = []
    paste = forms.CharField(label="Paste (JSON only)", widget=forms.Textarea)


class NewJSONURLForm(forms.Form):
    file_field_names: list = []
    url = forms.URLField(label="URL")
