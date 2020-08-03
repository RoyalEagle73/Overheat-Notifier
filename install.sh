echo "Downloading Repo"
git clone https://github.com/RoyalEagle73/Overheat-Notifier.git
echo "Repository Downloaded"
cd Overheat-Notifier
echo "Checking/Installing dependencies"
sudo pip3 install -r requirements.txt
echo "Dependencies Installed Succesfully."
echo "Copying current folder into root directory."
echo "NOTE: Do not delete the folder afterwards."
cp -r $PWD /
echo "Folder Copied Successfully."
echo "Making program to boot at startup."
sudo cp overheat-notifier.service /etc/systemd/system/overheat-notifier.service
echo "Starting service"
sudo systemctl enable overheat-notifier
sudo systemctl start overheat-notifier
echo "Service started "
echo "Installation Successfull..."
