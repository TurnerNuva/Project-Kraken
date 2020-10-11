# For object detection in local images
def localize_objects(path):
    """Localize objects in the local image."""


    from google.cloud import vision
    
    # Imports the Google Cloud client library
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # Recognizing objects in image
    # pylint: disable=no-member
    objects = client.object_localization(
        image=image).localized_object_annotations

    # Outputting data/preparing it for transmission back to USV
    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))

    return objects


# #For object detection in remote images
# def localize_objects_uri(uri):
#     """Localize objects in the image on Google Cloud Storage

#     Args:
#     uri: The path to the file in Google Cloud Storage (gs://...)
#     """
#     from google.cloud import vision
#     client = vision.ImageAnnotatorClient()

#     image = vision.Image()
#     image.source.image_uri = uri

#     # pylint: disable=no-member
#     objects = client.object_localization(
#         image=image).localized_object_annotations

#     print('Number of objects found: {}'.format(len(objects)))
#     for object_ in objects:
#         print('\n{} (confidence: {})'.format(object_.name, object_.score))
#         print('Normalized bounding polygon vertices: ')
#         for vertex in object_.bounding_poly.normalized_vertices:
#             print(' - ({}, {})'.format(vertex.x, vertex.y))