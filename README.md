# Scripts, Configs etc.

### hibpwned.py
This script checks the [pwned passwords API](https://haveibeenpwned.com/API/v2) by haveibeenpwned.com for compromised passwords.
 ``` bash
$ python hibpwned.py $PWD
 ```

### euribor
Calls API for current EURIBOR rates

### emacs
Personal config files for emacs, to be used in combination with prelude.

 ``` bash
$ git clone git@github.com:Korving-F/scripts-configs.git
$ cp scripts-configs/emacs/* ~/.emacs.d/personal/
 ```

### GPG Converter
Meh script to convert GPG keys produced by QtPass to CSV file for import into 3rd party password manager. Also an excuse to learn about click / jinja2 etc.
``` bash
$ python converter.py --help
```

### ESP32 / DHT22 Humidity/Temperature Sensor
Quickly playing with ESP32 for the first time in a while using DHT22 sensor.

Libraries:

* [Adafruit DHT Humidity & Temperature Sensor Library ](https://github.com/adafruit/DHT-sensor-library)
* [Adafruit Unified Sensor Driver](https://github.com/adafruit/Adafruit_Sensor)
* [ESPAsyncWebServer](https://github.com/me-no-dev/ESPAsyncWebServer)
* [AsyncTCP](https://github.com/me-no-dev/AsyncTCP)

See also [this](https://randomnerdtutorials.com/esp32-dht11-dht22-temperature-humidity-web-server-arduino-ide/) tutorial. 

<img src="hhttps://raw.githubusercontent.com/Korving-F/scripts-configs/master/dht22-webserver/breadbord.jpg?sanitize=true" alt="ESP32" height="10%" width="10%">
