# 1. Define the project
## What is the project?
- **Sweet Dreams, Martian** is a project to build a DeepDream visualizer using images of Mars that is accessible in a web browser
- This project is going to be solved using HTML, CSS, Python, Django and TensorFlow
- It will get images from the NASA Mars Images API and choose one that is suitable for the Deep Learning model
- The image will then be put through a DeepDream algorithm
- after a certain interval of steps the image in the browser is updated repeatedly
## What is the Minimal Viable Product(MVP)?
### Web application
- user goes to a url
- project is right there
- without input from the user a picture from Mars is shown
### DeepDream algorithm
- the picture updates with each iteration of the deepdream algorithm
- with time the user can see the picture change

## What are the sprinkles?
### Buildings + Rockets are deep dreamed
- play around with model architecture, training data and hyperparameters
- buildings + cars + rockets
    - human technologies should start appearing on the image
### Blog Post
- `What is this?` link at the bottom of the demo
- user clicks on it, scrolls down to explanation
- topics
    - gets an image of Mars from the NASA REST API
    - chooses the best one for this image based on ...
    - uses ... to show the image
    - uses the DeepDream algorithm implemented with the TensorFlow and Keras packages in Python
    - info about DeepDream algorithm

