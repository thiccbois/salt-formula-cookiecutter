# cookiecutter-salt-formula

[Cookiecutter](https://github.com/audreyr/cookiecutter) repository for generating saltstack formula repository skeleton.

## Install cookiecutter

- Install cookiecutter: [howto](http://cookiecutter.readthedocs.org/en/latest/installation.html)
- Read about Cookiecutter's [features](https://github.com/audreyr/cookiecutter#features)

## Usage

```bash
cd ${DIRECTORY_YOU_WISH_TO_CREATE_THE_SALT-FORMULA_IN}
```

Run

```bash
cookiecutter https://github.com/thiccbois/salt-formula-cookiecutter.git
```

This will clone `cookiecutter-salt-formula` in your `~/.cookiecutters` directory and prompts you for some new-project related questions.
Once you've answered those, a skeleton project directory will have been created for you. 

Once the first clone is done you can simply run:

```bash
cookiecutter ~/.cookiecutters/cookiecutter-salt-formula
```

### Create a new saltstack formula

```bash
cd ${DIRECTORY_YOU_WISH_TO_CREATE_THE_SALT-FORMULA_IN}
cookiecutter ~/.cookiecutters/cookiecutter-salt-formula
```

Follow the prompts for the win!

### Salt tests prerequisites

Before executing `make setup` ensure that

- bundler in installed: `gem install bundler`
- virtualenv is installed: `pip install virtualenv`

Before you execute `make tests` ensure that `docker` is up'n'running.

### Local configuration

You can also create your own ```cookiecutter``` configuration in ```~/.cookiecutterrc```:

```bash
default_context:
    full_name: "Johnny Bravo"
    email: "johnny.bravo@gmail.com"
    github_username: "johnnybravo"
```

