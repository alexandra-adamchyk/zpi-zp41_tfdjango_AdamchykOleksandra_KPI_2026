from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

    def clean_image(self):
        image = self.cleaned_data["image"]

        allowed_types = ["image/jpeg", "image/png"]
        if image.content_type not in allowed_types:
            raise forms.ValidationError("Only JPG and PNG files are allowed.")

        max_size = 5 * 1024 * 1024  # 5 MB
        if image.size > max_size:
            raise forms.ValidationError("File is too large. Maximum size is 5 MB.")

        return image