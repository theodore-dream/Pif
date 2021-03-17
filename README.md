# Pif
this pi project allows you to output text to a SPI display 

### Notes
Using crontab, you can place the following line so that the script autostarts on reboot:

@reboot sudo python /home/pi/luma.examples/examples/pif.py -i spi -d ssd1351 --height 128 > /home/pi/log.txt

I am using luma project from: https://github.com/rm-hull/luma.examples.git this is a requirement for this to work. 

I placed pif.py (the main python script, adapted from luma examples) into /home/pi/luma.examples/examples/ and I also created a folder pif_poems into the same directory. Then, I put my poems/text blurbs into that folder.
