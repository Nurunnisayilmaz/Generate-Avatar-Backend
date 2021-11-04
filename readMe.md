# Generate Avatar Backend

When a profile photo requested by the user is uploaded to the required field via the web-based user interface, a structure has been designed to process the sent photos with artificial intelligence algorithms and to create and send an output in the form of an avatar.

In this section, the back-end part has been developed. The backend is programmed with python and created with the rest service flask library. It takes the photo from the front-end and processes it on artificial intelligence, and returns the resulting avatar to the front-end.

The trained artificial intelligence used in the application https://github.com/minivision-ai/photo2cartoon is taken from this source.


