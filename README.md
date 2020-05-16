# Metadata File Generator

A simple tool to generate a metadata file intended to be used for feature based molecular networking in GNPS.

## Easy Setup
Download the files [here](https://mega.nz/file/Xow2mSrT#hM1Hwga1gYvFd2ccbiirvT3jA9zfuOGKWfSYm1pBLbE) and unzip. Alternatively, a single executable (.exe) version can be found [here](https://mega.nz/file/DxhWBCpT#LPWKc9YRbHDj9crepNqDVhFzFUa1sytK7RsKwfHLff0).
* The single executable version has a much smaller file size but much slower startup time.
* Both versions are portable.

## Advanced Version Setup
1. Download the files in this repo and unzip.
2. If Python 2 is not set to PATH, do so.
  - Follow the instructions [here](https://gtluu.github.io/blanka/documentation/installation/index.html) to check if Python 2 is added to PATH and add it if it is not.
  - Note that ```pythonw.exe``` should also be added to PATH.
3. Install any missing dependencies.

#### Dependencies
* PyQt4
* pandas 1.0 or higher

## Usage
1. Run ```run_metadata_file_generator.bat``` or ```metadata_file_generator.exe``` to start the program.
2. Use ```File > Add Files...``` to add the desired MS files used in your analysis. Alternatively, a tab separated file previously made can be loaded by using ```File > Open .tsv file...```.
3. Add an attribute by clicking on ```Add Attribute```. A pop-up window will allow you to enter your attribute (i.e. 'condition', 'strain', etc).
4. Highlight one or more rows and click on ```Set Attribute``` to set the attribute value for those rows. A pop-up window will allow you to select which attribute to add for those rows, and a second pop-up window will allow you to enter a value.
5. Save your metadata file using ```File > Save to .tsv...``` and selecting your desired output directory and filename.

## To Do List
* Add function to delete rows from the table.
* Add function to delete columns from the table.
