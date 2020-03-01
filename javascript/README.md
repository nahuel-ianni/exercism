# JavaScript
>JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification. JavaScript is high-level, often just-in-time compiled, and multi-paradigm. It has curly-bracket syntax, dynamic typing, prototype-based object-orientation, and first-class functions.
>
>Alongside HTML and CSS, JavaScript is one of the core technologies of the World Wide Web. JavaScript enables interactive web pages and is an essential part of web applications. The vast majority of websites use it for client-side page behavior, and all major web browsers have a dedicated JavaScript engine to execute it.
>
>As a multi-paradigm language, JavaScript supports event-driven, functional, and imperative programming styles. It has application programming interfaces (APIs) for working with text, dates, regular expressions, standard data structures, and the Document Object Model (DOM). However, the language itself does not include any input/output (I/O), such as networking, storage, or graphics facilities, as the host environment (usually a web browser) provides those APIs.
>
>Originally used only in web browsers, JavaScript engines are also now embedded in server-side website deployments and non-browser applications.

## Installing Javascript
There are a couple of ways to install [NodeJS](https://nodejs.org/):
- via an [Installer or Binary](https://nodejs.org/en/download/)
- via a [package manager](https://nodejs.org/en/download/package-manager/)

Both options support Windows, MacOS, and Linux. If you don't know what to do, using an installer is the easier.

Exercism recommends using the LTS version. This is also indicated as recommended on the [NodeJS](https://nodejs.org/) website "for most users".
Follow the instructions on the webpage and/or during the installer and install [NodeJS](https://nodejs.org/).

After the installer is done, or the package manager has completed, or the binary has been copied and the instructions have been followed, it's good to test if everything is alright.

- Open up a terminal (Terminal, cmd, Powershell, bash, ...)
- `node -v`
The version should match the one on the website.

Note: It is important to open a new terminal window. Any open terminal windows might not have been refreshed after the installation completed. This means that the open terminals don't know that a new program was installed.

## Test management
Each assignment needs some tools to run the tests. They can be installed running this command within each assignment directory:

`$ npm install`

This works because *npm* is a package manager that comes bundled with *NodeJS*, which has been installed per the steps above. The `npm` command looks for a *package.json* file, which is present in each assignment folder. This file lists the *dependencies* above, which are then downloaded by *npm* and placed into the *node_modules* folder.

The scripts in the *package.json* use the binaries from the local *node_modules* folder, and its these scripts that are used to run the tests, as listed in the exercise description.

## Running the tests
Yarn can easily execute all tests in a file by executing the `npm test` command from the test file's directory where the `package.json` file resides.

If you want to execute all tests on a particular file, the command accepts a path as a parameter: `npm test <filename>.spec.js`.

---

## Helpful resources
*Nothing to show yet*