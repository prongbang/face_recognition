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

## Install OpenCV
```
pip install opencv-python
```

## Install face_recognition
```
pip install face_recognition
```

## Run
```
python main.py
```