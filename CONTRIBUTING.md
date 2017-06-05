# Contributing to Compilio

Contributions to Compilio project are welcomed. You can help the project by reporting
any issue you may encounter, or fixing them in pull requests.

## Installation walkthrough

If you want to install the full Compilio stack on your computer, you can follow this short
tutorial to get your system ready.

**Be sure to also read the README.md file at the root of each project as instructions may be more
complete there.**

First, create a *compilio-project* folder on your system. You will need some dependencies (you may use
older/less dependencies if you install only a subpart of the project):

- Python 3.6
- Virtualenv (you can install it using `pip install virtualenv`)
- Docker (to be able to use advanced compilation tasks)
- Node.js and npm

### Compilio web platform

The Compilio web platform is stored on the current repository. Clone it on your *compilio-project* folder.

```sh
git clone https://github.com/compilio/compilio.git
cd compilio
```

You will need to create a `virtualenv` to install the required dependencies (this will also avoid you
polluting your system's packages list).

```
virtualenv env
source ./env/bin/activate
```

Be sure that Python 3.6 is used to build the `virtualenv` (you may run into compatibility issues
otherwise). You can also specify the path to Python 3.6 executable if it is not used by default:

```
virtualenv env --python=/usr/bin/python3.6
source ./env/bin/activate
```

Now, you can install the dependencies and run the reset script. It will create the sqlite
database and load fixtures (be sure that the virtualenv is activated, or run the `./env/bin/activate`
command).

```
pip install -r requirements.txt
./bin/reset
```

To be able to load the css files, you also need to install the node dependencies:

```
npm install
```

You're all set! You can start the two required servers using two different terminals:

For the python server (be sure to activate the virtualenv running the
`source ./env/bin/activate` command):

```
python manage.py runserver
```

For the webpack server:

```
npm run server
```

You now have Compilio running on your computer! You can access to the homepage at
http://127.0.0.1:8000

If you can't access to the homepage, check the python server is running and the logs
are not suspicious.

If there is no style on pages, make sure that the webpack server is running and the
compilation logs does not show anything strange.

**To be able to run compilation tasks, you must install Compilio-runner.**

### Compilio-runner

To install Compilio-runner, you first need to clone the repository on your *compilio-project*
folder:

```sh
git clone https://github.com/compilio/compilio-runner.git
cd compilio-runner
```

You need to create a new virtualenv here. You just have to follow the steps performed in
the previous section and create a new *env* virtualenv. Activate it and run the following commands:

```sh
pip install -r requirements.txt
python main.py
```

Compilio-runner is now operational! Compilio web platform will automatically talk with it when needed.
The runners are referenced in the fixtures file in your *compilio* directory (under
*compilio/compiler/fixtures/initial_data.yaml*). The runner is registered to be able to run the *ls*, *cat*
and *pdflatex* tasks.

If you want to be able to run *pdflatex* tasks on your computer, you will need to pull the image first, using
*docker pull blang/latex*. Wait for the download. You are now able to compile LaTeX files through your local
instance.

If tasks are failing, check the Compilio-runner logs.

### Compilio CLI

Compilio also provides a CLI to be able to compile files directly in the terminal. Commands must be recognized
by Compilio, or the command will be refused.

You can register new commands in the *initial_data.yaml* file described previously.

To install Compilio CLI on your computer (in **development** mode), it is the same way than before:
 
From your *compilio-project* folder:

```sh
git clone https://github.com/compilio/compilio-cli.git
cd compilio-cli
virtualenv env
source ./env/bin/activate
pip install -r requirements.txt
python compilio.py
```

**Be sure to change the CLI configuration under *compilio/config.yml* to set your local server instance to
`http://localhost:8000`**.

Thanks, you're now able to test or improve Compilio's source code!
