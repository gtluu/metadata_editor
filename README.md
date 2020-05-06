# Metadata File Generator

A simple tool to generate a metadata file intended to be used for feature based molecular networking in GNPS.

### Setup
1. Download the files in this repo and unzip.
2. If Python 2 is not set to PATH, do so.
  * Follow the instructions [here](https://gtluu.github.io/blanka/documentation/installation/index.html) to check if Python 2 is added to PATH and add it if it is not.
  * Note that ```pythonw.exe``` should also be added to PATH.

### Usage
1. Run ```run_metadata_file_generator.bat``` to start the program.
2. Use ```File > Add Files...``` to add the desired MS files used in your analysis. Alternatively, a .csv file previously made can be loaded by using ```File > Open .csv file...```.
3. Add an attribute by clicking on ```Add Attribute```. A pop-up window will allow you to enter your attribute (i.e. 'condition', 'strain', etc).
4. Highlight one or more rows and click on ```Set Attribute``` to set the attribute value for those rows.
5. Save your metadata file using ```File > Save to .csv...``` and selecting your desired output directory and filename.

#### To Do List
* Add function to delete rows from the table.
* Add function to delete columns from the table.
