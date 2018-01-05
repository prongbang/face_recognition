# Windows
## Step 1: Install [Python 2.7 or 3.6](https://www.python.org/downloads/)

# Mac OSX
## Step 1: Install Homebrew
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

## Step 2: Update Homebrew
```
brew update
```

## Step 3: Install Python
```
brew install python
```

## Step 4: Installing boost
```
brew install boost --with-python
```

## Step 5: Installing boost-python
```
brew install boost-python
```

## Step 6: Confirm boost and boost-python is installed
```
brew list | grep 'boost'
```
> boost

> boost-python

## [Read More...](https://www.pyimagesearch.com/2015/04/27/installing-boost-and-boost-python-on-osx-with-homebrew/)


# How to use ```face_recognition```

### ```pip``` or ```pip2``` for python2 
### ```pip3``` for python3

## Step 1: Copy image to ```image``` directory

## Step 2: Install OpenCV 
```
pip install opencv-python
```

## Step 3: Install face_recognition
```
pip install face_recognition
```

## Step 4: Run
```
python main.py
```
