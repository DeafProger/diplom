from django.forms import ModelForm
from main.models import Record


class StyleFormMixin:
    """Класс для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"


class RecordForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Record
        exclude = ['result']
