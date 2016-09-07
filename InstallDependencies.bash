#!/bin/bash

echo "Installing..."
if [[ $(python -c 'import sys; print(sys.version_info[:][0]>2)') == "False" ]]; then
	# Python 2
	echo "Pyhton version lower than 3 found on system"
	echo "installing pip..."
	sudo apt-get install python-pip
	echo "installing Beautiful soup 4..."
	sudo pip install bs4
else
	# Python 3
	echo "Pyhton version 3 or higher found on system"
	echo "installing Beautiful soup 4..."
	sudo apt-get install python3-bs4
fi
echo "Installation complete!"
