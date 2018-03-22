## Development and Testing

To run the project locally, clone the repository, and then create a virtual environment and install the dependencies.

First, ensure you have a version of every Python we support installed. Your versions may differ.

```sh
pyenv install 2.7.14
pyenv install 3.3.7
pyenv install ...
pyenv global 3.6.3 3.5.4 3.4.7 3.3.7 2.7.14   
```

Next ensure you create a virtual environment.

```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running tests

To run the tests against every supported Python version, use `tox`.

```sh
tox
```

Alternatively, to run tests just against a specific Python version, create coverage files, and watch for changes:

```sh
brew install fswatch
pyenv shell 2.7.14
make watch
```

### Using a library locally

To install a library locally, use `pip` to install the library in editable mode.

```sh
pip install -e .
```

This will make the current code available for editing and using in live scripts, for example.

```py
from amadeus import Client
```

### Releasing

[TBD]

## How to contribute to the Amadeus Ruby Gem

#### **Did you find a bug?**

* **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/amadeusdev/amadeus-python/issues).

* If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/amadeusdev/amadeus-python/issues/new). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.

#### **Did you write a patch that fixes a bug?**

* Open a new GitHub pull request with the patch.

* Ensure the PR description clearly describes the problem and solution. Include the relevant issue number if applicable.

#### **Do you intend to add a new feature or change an existing one?**

* Suggest your change [in a new issue](https://github.com/amadeusdev/amadeus-python/issues/new) and start writing code.

* Make sure your new code does not break any tests and include new tests.

* With good code comes good documentation. Try to copy the existing documentation and adapt it to your needs.

* Close the issue or mark it as inactive if you decide to discontinue working on the code.

#### **Do you have questions about the source code?**

* Ask any question about how to use the library by [raising a new issue](https://github.com/amadeusdev/amadeus-python/issues/new).

#### **Do you want to contribute to the documentation?**

[TBD]
