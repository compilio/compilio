# Compilio

Compilio will be an online self-hostable modular compiler allowing you to compile files such as PDF LaTeX files and more.

More information coming soon...

## Development

### Installation

To install the project and start the deployment environment, you need the following requirements:

- `Python 3.5` with `pip`
- `Node 6` with `npm`

Then, run the following commands:

```sh
pip install Django
npm install
```

### Running

To be able to run the project properly, you need to run the Webpack dev server first:

```sh
./node_modules/.bin/webpack-dev-server
```

You can then run the python build-in server:

```sh
python manage.py runserver
```
