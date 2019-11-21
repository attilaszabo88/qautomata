# Welcome to QAutomata!

This repository is designed for automated test cases using `selenium`.


Setup:

0. Open the project with `PyCharm`.

1. Make sure to create a `virtualenv` specifically for this project.

2. Once you did that, open a new terminal. Make sure it's on the new virtualenv you created.

3. Install the requirements using `pip install -r requirements.txt`

4. Make sure to have the `chromedriver` executable in your PATH variable.
The PATH is a list of directories where OS looks when executing commands.
You can check the list of dirs with `echo $PATH`.
Create a symbolic link for the `chromedriver` into `/bin` using the following command, and make sure to use absolute paths(right-click on `chromedriver` in PyCharm and select Copy Path)

    `sudo ln -s <your_path>/qautomata/chromedriver /bin`

