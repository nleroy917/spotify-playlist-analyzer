#!/bin/bash

echo ""
echo "  ______   _______     ___    _________  _____  _______     _  ____      ____   ______  " 
echo "./ ____ \ |_   __ \  ./   \. |  _   _  ||_   _||_   __ \   / \|_  _|    |_  _|.| ____ \ "
echo "| (___ \_|  | |__) |/  .-.  \|_/ | | \_|  | |    | |__) | / _ \ \ \  /\  / /  | (___ \_|"
echo " _.____|.   |  ___/ | |   | |    | |      | |    |  ___/ / ___ \ \ \/  \/ /    _.____\. " 
echo "| \____) | _| |_    \  \-/  /   _| |_    _| |_  _| |_  _/ /   \ \_\  /\  /    | \____) |" 
echo " \______./ |_____|   \.___./   |_____|  |_____||_____||____| |____|\/  \/      \______|"
echo ""
echo "Written by: Nathan LeRoy"
echo "Twitter: @NathanJLeRoy"
echo "GitHub: @NLeRoy917"
echo ""
echo "Installing latest gecko-driver . . . "

mkdir gecko/
install_dir="gecko/"
json=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest)

if [[ $(uname) == "Darwin" ]]; then
    url=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | python -c "import sys, json; print(next(item['browser_download_url'] for item in json.load(sys.stdin)['assets'] if 'macos' in item.get('browser_download_url', '')))")
elif [[ $(uname) == "Linux" ]]; then
    url=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | python -c "import sys, json; print(next(item['browser_download_url'] for item in json.load(sys.stdin)['assets'] if 'linux64' in item.get('browser_download_url', '')))")
else
    echo "can't determine OS"
    exit 1
fi

curl -s -L "$url" | tar -xz
chmod +x geckodriver
sudo mv geckodriver "$install_dir"
echo "installed geckodriver binary in $install_dir"

echo "Making necessary directories . . . "
mkdir testing
mkdir testing/configs/

echo "Copying config file . . . please fill out credentials accordingly . . ."
read -p "Press enter when ready . . ."
cp app-data/config-template.ini testing/configs/config.ini
nano testing/configs/config.ini