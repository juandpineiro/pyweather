# PyWeather

A Python 3 GUI application (made with Tkinter) that uses the [OpenWeatherMap](https://openweathermap.org/) API to present current weather conditions in the entered city.

Based on [this video tutorial](https://youtu.be/D8-snVfekto) by Keith Galli ([Github repo](https://github.com/KeithGalli/GUI) | [Twitter](https://twitter.com/keithgalli))

!["PyWeather app"](./img/app.png)

## Development

Verify that you have Python 3 and install `pip` and `virtualenv`:

```bash
$ which python3
/usr/bin/python3
$ sudo apt install python3-pip
$ pip3 install virtualenv
```

Clone the repo

```bash
$ git clone git@github.com:juandpineiro/pyweather.git
```

Enter the directory, create the Python virtual environment and install the requirements:

```bash
$ cd pyweather
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Run the app:

```bash
(venv) $ ./pyweather.py
```
