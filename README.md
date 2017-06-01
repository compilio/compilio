# Compilio

[![Build Status](https://travis-ci.org/compilio/compilio.svg?branch=master)](https://travis-ci.org/compilio/compilio)

Compilio will be an online self-hostable modular compiler allowing you to compile files such as PDF LaTeX files and more.

Check out the [CONTRIBUTING.md file](https://github.com/compilio/compilio/blob/master/CONTRIBUTING.md) if you want to
install Compilio locally and contribute to the source code.

## Development

### Installation

To install the project and start the deployment environment, you need the following requirements:

- `Python 3.4` with `pip`
- `Node 6` with `npm`

Then, run the following commands:

```sh
pip install -r requirements.txt
npm install
```

### Running

To be able to run the project properly, you need to run the Webpack dev server first:

```sh
npm run server
```

You also need to run migrations and load fixtures:

```sh
./bin/reset
```

You can then run the python built-in server:

```sh
python manage.py runserver
```

### Deploying

You may use the basic deployment script:

```sh
sudo pip install virtualenv
./bin/deploy
```

Close your terminal instance when the following line appears:

```
nohup: ignoring input and appending output to ‘nohup.out’
```

### Testing

You can launch tests using the following commands:

```sh
python manage.py test
python manage.py test functional
```
