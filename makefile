#
# Makefile for MHDOS built by Moravak
#

install:
	@echo "\033[0;34mBuilding MH DOS...\033[0m"
	python3 -m venv .
	bin/pip3 install -r requirements.txt
	bin/pyinstaller src/dos.py
	@echo "\033[0;34mBuilding successfull!\nRun MH DOS from dist/dos/dos\033[0m"
