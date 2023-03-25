# Real-time stress detection

This project aims to investigate the extraction of stress features in call center agents wearing masks through real-time video processing using traditional image processing techniques.

## Folder structure

The project is organized as follows:

modules: This folder contains the project's modules.
- aux_faces.py: This module handles face detection and tracking in a video.
- aux_open.py: This module handles opening a video file.
- class_video.py: This module contains the Video class, which handles video and stress detection.
- utils.py: This module contains utility functions for image processing.
- aux_features: This module contains all features to extract in video. (**In construction**)
init.py: This file is the entry point for the project.

# Requirements

To run this project, you need the following dependencies:

- Python 3.10 or lower
- OpenCV 4.2 or higher
- numpy
- imutils
- mediapipe [more information] (https://google.github.io/mediapipe/getting_started/python)

You can install these dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use the project, follow these steps:

- Create a folder called Base de datos.
- Add your video files to the Base de datos folder.
- Edit the init.py file to include the path to the Etapa1 and Etapa2 video folders.

**Note**: that the project does not load the database, as it is a research project by the PROMISE research group at Escuela Colombiana de Ingenieria Julio Gravito in conjunction with the company Millenium BPO.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)