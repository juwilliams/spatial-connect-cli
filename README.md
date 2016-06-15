# SpatialConnect
A python based command line interface for managing spatial container configuration.


## About
SpatialConnect is a command line interface for creating JSON files which describe “containers” of data. These containers specify both where data comes from, how to process it and how to transmit it between WebEOC and ArcGIS.


## Requirements
* A windows machine to run the accompanying Windows Console Application

* A bash shell (terminal, cygwin, iterm, terminator etc) and basic knowledge of shell commands

* Python 2.7 or greater


## Installation
`pip install connect`

or if you have forked and are adding features to a development version

`pip install -e .` from your clone directory


## SpatialConnect File System Anatomy:
* container/config.json : this file details connection information for integrated systems
* container/container.json : this file resides within a container directory and details specific information about a targeted data source such as an ArcGIS featureclass or a WebEOC Board/View.
* container/fields.json : this file describes what elements of a data source that you care about and how to translate fields between systems
* push|pull/history.json : this file contains unique hashes that represent records extracted from or pushed to systems. This allows the SpatialConnect system to avoid sending the same record twice to target systems.
* container/relationships.json : this file maintains information about how containers and their records are related. This file is the key to performing updates to records in target systems.
* container/temp : this folder contains any temporary files that are downloaded as a part of sourcing a system for data.


## Examples
It is important to note that all commands are executed within the scope of your current directory. Certain commands expect that your current directory be at a specific location in the SpatialConnect directory hierarchy.

* Create a directory to serve as the home of all your containers

`$ mkdir connect`

* Initialize your directory

`$ connect config`

Answer the following questions, if you choose to not setup your connection details now you can edit the file directly later. Make sure to complete this step before attempting to run the Windows console application.

* Create a container

`$ connect create my_container -d webeoc -s your_feature_class -f arcgis -g point`

This will create a sub-directory called my_directory (connect/my_directory) which contains a push directory, pull directory, as well as the files fields.json and relationships.json. Inside both the push and pull directories you will find a history.json file.

* Add fields to your container

`$ connect addfield my_field my_field_to string 50`

This new field will be added to the fields.json file for the container directory you are currently in.


## Advantages over previous systems
Previous incarnations of SpatialConnect (GeoServices, GeoHub) were advancements towards the aim of providing an easy to use interface for a wide range of data collection tools and sources. Over time however, it became apparent that our scope had become too broad and the maintenance of those versions had become too burdensome to both myself and the end-user. SpatialConnect as it exists today is a dramatic improvement in both stability and ease of use, providing the end user with a simple command line interface that produces JSON configuration files, which the complimenting legacy Windows console application can read and process. This new version is also built with the larger emergency mangement community in mind, available for installation using the Python language package manager standard (PyPi), and the source made available for community contributions on github.com.
