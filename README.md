# cloud-scraper
A simple app to take screenshots of web pages listed in a file and save them to disk.

## Usage

```
# This script will create a python virtual environment and setup playwright
./setup_ubuntu.sh

# activate the virtual environment
source scraper-venv/bin/activate

# run the script
python3 scraper.py
```

### Running the script in the background

```
nohup python3 -u screenshot.py &
```

Logs will be written to `nohup.out`.