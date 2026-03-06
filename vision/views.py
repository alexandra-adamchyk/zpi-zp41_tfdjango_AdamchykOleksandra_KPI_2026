from pathlib import Path

from django.conf import settings
from django.shortcuts import render

from .forms import ImageUploadForm
from .services.hashing import sha256_for_uploaded_file
from .services.inference import predict_image

PREDICTION_CACHE = {}


def upload_image(request):
    prediction = None
    image_url = None
    cached = False

    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_image = form.cleaned_data["image"]

            file_hash = sha256_for_uploaded_file(uploaded_image)

            upload_dir = Path(settings.MEDIA_ROOT) / "uploads"
            upload_dir.mkdir(parents=True, exist_ok=True)

            extension = Path(uploaded_image.name).suffix.lower()
            safe_filename = f"{file_hash}{extension}"
            saved_path = upload_dir / safe_filename

            if not saved_path.exists():
                with open(saved_path, "wb+") as destination:
                    for chunk in uploaded_image.chunks():
                        destination.write(chunk)

            image_url = f"{settings.MEDIA_URL}uploads/{safe_filename}"

            if file_hash in PREDICTION_CACHE:
                prediction = PREDICTION_CACHE[file_hash]
                cached = True
            else:
                prediction = predict_image(saved_path)
                PREDICTION_CACHE[file_hash] = prediction

    else:
        form = ImageUploadForm()

    return render(
        request,
        "vision/upload.html",
        {
            "form": form,
            "prediction": prediction,
            "image_url": image_url,
            "cached": cached,
        },
    )