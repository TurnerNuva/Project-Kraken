
# For detection of local image
def detect_labels(path):
    """Detects labels in the file."""

    # Imports the Google Cloud client library
    from google.cloud import vision
    import io
    
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory 
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    # pylint: disable=no-member
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('\nLabels:')

    for label in labels:
        print(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


# #For detection of remote images
# def detect_labels_uri(uri):
#     """Detects labels in the file located in Google Cloud Storage or on the
#     Web."""
#     from google.cloud import vision
#     client = vision.ImageAnnotatorClient()
#     image = vision.Image()
#     image.source.image_uri = uri

#     # pylint: disable=no-member
#     response = client.label_detection(image=image)
#     labels = response.label_annotations
#     print('Labels:')

#     for label in labels:
#         print(label.description)

#     if response.error.message:
#         raise Exception(
#             '{}\nFor more info on error messages, check: '
#             'https://cloud.google.com/apis/design/errors'.format(
#                 response.error.message))