sed '1 s/Ref/Designator/' -i gerber/usbswitch-top-pos.csv
sed '1 s/PosX/Mid X/' -i gerber/usbswitch-top-pos.csv
sed '1 s/PosY/Mid Y/' -i gerber/usbswitch-top-pos.csv
sed '1 s/Rot/Rotation/' -i gerber/usbswitch-top-pos.csv
sed '1 s/Side/Layer/' -i gerber/usbswitch-top-pos.csv

head gerber/usbswitch-top-pos.csv

zip -r gerber.zip gerber
