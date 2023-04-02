# ScriptAssist

### Attention: 
All new features are implemented in the **dev** branch.

## About
This is a GUI application that allows users to modify a script, execute it and see its output side-by-side. The supported scripting languages are Swift and Kotlin.


### Adjust script configuration

<img width="1050" alt="image" src="https://user-images.githubusercontent.com/69808568/228081637-69a5e585-a152-490f-b98f-bfb3c7ae0979.png">

### Edit and execute the script


<img width="1050" alt="image" src="https://user-images.githubusercontent.com/69808568/229319423-4e6afe86-2029-491f-ab95-f9c1f732001c.png">

<img width="1050" alt="image" src="https://user-images.githubusercontent.com/69808568/229319392-999ef698-ab49-4124-9164-29a94e1ccc3f.png">


## Installation

### Requirements
Before running ensure you have the following software:
- Python 3.x
- pip3

To run scripts on the chosen language you need to install the necessary dependencies:
- For Swift: Download Swift from the official [website](https://www.swift.org/download/).
- For Kotlin: Install the Kotlin compiler from the official [website](https://kotlinlang.org/docs/command-line.html).


### Running

1. Clone the repository:
```
git clone https://github.com/rakhmukova/ScriptAssist.git
```

2. Change to the project directory:
```
cd ScriptAssist
```

3. Create a virtual environment and activate it:
```
python3 -m venv venv
source venv/bin/activate
```


4. Install necessary packages
```
pip3 install -r requirements.txt
```

5. Run the application
```
cd src
python3 main.py
```

6. To deactivate the virtual environment you can run the following command:
```
deactivate
```

### Tests
In order to run tests use the following command in the roor directory:
```
pytest
```

