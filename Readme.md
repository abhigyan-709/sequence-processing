# How to run the code & test

## 1. Prepare the virtual environment

### For Mac or Unix based system: 

```bash 
# make sure the virtual environment is installed in the system
python3 -m venv venv

# activate the virtual environment
source ./venv/bin/activate
```

### For Windows based system: 

```bash
# initialize the virtual env
python -m venv venv   

# activate the virtual environment if you are using the powershell
venv\Scripts\activate   
```

## 2. Clone the code & Install the Requirements & dependencies

```bash
# clone the code from git hub
# get into working directory

git clone https://github.com/abhigyan-709/home-work.git

# get into the main directory and make sure you have activated the virtual env according to the system
# install dependencies

pip install -r requirements.txt
```

## 3. Guide to run the code & details about the code 

### function based execution - procedural based execution

To run & test the file, you can run below commands, when you have successfully cloned the code.
Make sure you have installed all the dependencies and files, including csv for data input, & the virtual environment is activated.

```bash
# move to the directory where you have cloned and activated the virtual environment
# load, run, display the output and save the processed data in the new csv file.

python sequence_processing.py
# when prompted the for input, enter the desired or required sequences between 0 to 1000 & hit enter
# wait for the truncated output and csv file to be generated.

# test the file with the given or desired input, which will create the seperate csv file and it will also re-write the current generated csv file
pytest feature_test.py

# Note: the above file re-writing is not expected feature, but it will be removed after debugging.  
```

### class based execution - for deployment over the large scale systems
The class based execution format is strictly based for large scale deployments and for the usage of data structures, if more time will be provided for deployment purpose & feature upgrades.
