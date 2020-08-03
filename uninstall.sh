sudo rm -rf /overheat-notifier
sudo systemctl stop overheat-notifier.service
sudo systemctl disable overheat-notifier.service
sudo rm /etc/systemd/system/overheat-notifier.service
echo "Overheat-Notifier removed successfully. Thank You for trying."
