# Django Polls Application

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![Chart.js](https://img.shields.io/badge/Chart.js-enabled-orange)

## Project Overview

This project is a web application built with Django.

It allows users to:
- view polls
- vote for answers
- see voting results

The project is based on the official Django tutorial and extended with a modern frontend interface.

---

## Features

- Display poll questions
- Vote for answers
- View voting results
- Progress bars for vote distribution
- Results chart using Chart.js
- Responsive Bootstrap design
- Poll management through Django Admin

---

## Technologies

- Python
- Django
- HTML
- CSS
- Bootstrap 5
- Chart.js
- SQLite

---

## Screenshots

### Home Page

![Home](images/home.png)

### Poll Page

![Detail](images/detail.png)

### Results Page

![Results](images/results.png)

### Django Admin

![Admin](images/admin.png)

---

## Project Structure

The project contains two main parts.

The **mysite** directory contains the main Django configuration files.

The **polls** application contains the core functionality of the project, including:

- models describing poll questions and answer choices
- views handling user interaction
- URL routing
- templates used to render pages
- static files for styling

Templates are located in:

templates/polls/

Static styles are located in:

static/polls/style.css

Screenshots used in the documentation are stored in the **images** directory.

The file **manage.py** is used to run Django management commands.

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies

```bash
pip install django
```

Apply migrations

```bash
python manage.py migrate
```

Run server

```bash
python manage.py runserver
```

Open in browser

http://127.0.0.1:8000/polls/

Admin panel

http://127.0.0.1:8000/admin/

---
---

# Part 2 — Image Recognition (Django + TensorFlow)

The second part of the project extends the Django application with an image recognition system.

A new Django application **vision** was created.  
It allows users to upload an image and detect the main object using a neural network.

The recognition is implemented using **TensorFlow / Keras MobileNetV2 pretrained on ImageNet**.

## Features

- upload JPG or PNG images
- neural network inference using MobileNetV2
- automatic image preprocessing
- grouping of detailed ImageNet classes into simple categories (Cat, Dog, Bird, etc.)
- confidence score for the detected object
- SHA256 caching for repeated images
- modern Bootstrap interface

## How it works

1. The user uploads an image.
2. The image is resized to **224x224** pixels.
3. The neural network predicts the top ImageNet classes.
4. Similar classes are grouped into simple categories.
5. The system displays the detected object and confidence score.

## Screenshots

### Upload Page

![Vision Upload](images/vision-upload.png)

### Example Result 1

![Vision Result 1](images/vision-result-1.png)

### Example Result 2

![Vision Result 2](images/vision-result-2.png)
