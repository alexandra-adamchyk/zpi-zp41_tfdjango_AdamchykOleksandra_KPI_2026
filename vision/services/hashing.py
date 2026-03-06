import hashlib

def sha256_for_uploaded_file(uploaded_file):
    hasher = hashlib.sha256()

    for chunk in uploaded_file.chunks():
        hasher.update(chunk)

    return hasher.hexdigest()