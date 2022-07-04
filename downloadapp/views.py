from django.shortcuts import render

import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse


def download_file(request, filename='/last_cv.pdf'):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % 'my_cv.pdf'
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'Halem/cv.html')
