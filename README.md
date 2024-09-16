# Quantum Dot-Based Chemical Nanosensors Animation

This project is an interactive Pygame animation that explains the concept of Quantum Dot-Based Chemical Nanosensors, with a focus on CdS quantum dots prepared by microemulsion. The animation provides a visual and educational journey through various aspects of quantum dots and their application in chemical sensing.

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Scenes](#scenes)
6. [Customization](#customization)
7. [Contributing](#contributing)
8. [License](#license)

## Features

- Interactive Pygame animation
- 7 educational scenes covering different aspects of quantum dots
- Gradient backgrounds for visual appeal
- Particle animation in the introduction scene
- Click-through functionality to navigate scenes
- Explanatory text for each scene

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- Pygame library

## Installation

1. Clone this repository or download the source code.

2. Install the required Pygame library using pip:

   ```
   pip install pygame
   ```

## Usage

To run the animation:

1. Navigate to the project directory in your terminal.

2. Run the following command:

   ```
   python anim.py
   ```

3. The animation will start, cycling through different scenes automatically.

4. Click anywhere on the screen to manually advance to the next scene.

5. To exit the animation, close the window or press Ctrl+C in the terminal.

## Scenes

The animation consists of 7 scenes:

1. Introduction to Quantum Dot-Based Chemical Nanosensors
2. CdS Quantum Dot Preparation (Microemulsion)
3. Quantum Dot Fluorescence
4. Analyte Detection
5. Quantum Confinement Effect
6. Size-Dependent Optical Properties
7. Surface Functionalization

Each scene includes visual elements and explanatory text to help understand the concepts.

## Customization

You can customize various aspects of the animation:

- Modify colors in the color definitions at the top of the script.
- Adjust the `scene_duration` variable to change how long each scene is displayed.
- Edit the explanatory text in each `draw_scene_X()` function.
- Add or modify scenes by creating new `draw_scene_X()` functions and updating the main loop.

## Contributing

Contributions to this project are welcome. To contribute:

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them with clear commit messages.
4. Push your changes to your fork.
5. Submit a pull request with a description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

For any questions or issues, please open an issue on the GitHub repository.
