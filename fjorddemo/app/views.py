import logging

from django.conf import settings
from django.shortcuts import render

from fjorddemo.app.forms import (
    NewJSONTextForm,
    NewJSONUploadForm,
    NewJSONURLForm,
)
from libfjordweb.models import SuppliedDataFile
from libfjordweb.views import ExploreDataView, InputDataView

logger = logging.getLogger(__name__)


def index(request):
    forms = {
        "json": {
            form_name: form_class()
            for form_name, form_class in JSON_FORM_CLASSES.items()
        },
    }

    return render(request, "fjorddemo/index.html", {"forms": forms})


JSON_FORM_CLASSES: dict = {
    "upload_form": NewJSONUploadForm,
    "text_form": NewJSONTextForm,
    "url_form": NewJSONURLForm,
}


class NewJSONInput(InputDataView):
    form_classes: dict = JSON_FORM_CLASSES  # type: ignore
    input_template = "fjorddemo/index.html"  # type: ignore
    allowed_content_types = settings.ALLOWED_JSON_CONTENT_TYPES
    content_type_incorrect_message = "This does not appear to be a JSON file."
    allowed_file_extensions = settings.ALLOWED_JSON_EXTENSIONS
    file_extension_incorrect_message = "This does not appear to be a JSON file."
    supplied_data_format = "json"  # type: ignore

    def get_active_form_key(self, forms, request_data):
        if "paste" in request_data:
            return "text_form"
        elif "url" in request_data:
            return "url_form"
        else:
            return "upload_form"

    def save_file_content_to_supplied_data(
        self, form_name, form, request, supplied_data
    ):
        if form_name == "upload_form":
            supplied_data.save_file(request.FILES["file_upload"])
        elif form_name == "text_form":
            supplied_data.save_file_contents(
                "input.json",
                form.cleaned_data["paste"],
                "application/json",
                None,
            )
        elif form_name == "url_form":
            supplied_data.save_file_from_source_url(
                form.cleaned_data["url"], content_type="application/json"
            )


class ExploreView(ExploreDataView):
    explore_template = "fjorddemo/explore.html"  # type: ignore

    def default_explore_context(self, supplied_data):
        return {
            # Misc
            "supplied_data_files": SuppliedDataFile.objects.filter(
                supplied_data=supplied_data
            ),
            "created_datetime": supplied_data.created.strftime(
                "%A, %d %B %Y %I:%M%p %Z"
            ),
            "created_date": supplied_data.created.strftime("%A, %d %B %Y"),
            "created_time": supplied_data.created.strftime("%I:%M%p %Z"),
        }
