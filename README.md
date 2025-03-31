# Sample CI Project

This repository contains a mock Python web application built using Flask. It was created to demonstrate foundational concepts in project setup, documentation, version control, and testing all within the context of Continuous Integration.

---

## Project Structure

```
sample-ci-project/
├── src/                 → Application source code (Flask app)
│   └── app.py
├── tests/               → Unit tests for Flask routes
│   └── test_app.py
├── docs/                → Testing plans and documentation
│   ├── integration_plan.md
│   └── uat_plan.md
├── LICENSE              → MIT license for open use
└── README.md            → Project overview and instructions
```

---

## How to Run the App

To run the Flask application:

1. Ensure you open with vs code and Flask is installed:

   ```
   in the terminal, run: pip install flask
   ```

2. Run the app:

   ```
   python src/app.py
   ```

3. Visit the following URL in your browser:
   ```
   http://127.0.0.1:5000/
   ```

---

## How to Run the Tests

This project includes unit tests for the Flask routes using Python's built-in `unittest` module.

To run the tests:

```
python -m unittest discover tests
```

You should see output confirming the successful execution of test cases.

---

## License

This project is licensed under the **MIT License**.

> The MIT License is simple and permissivel; It allows for broad reuse, modification, and distribution of the code with minimal restrictions, making it well-suited for this project

---

## Purpose of This Repository

This repository was created as part of the “Project Development” course assignment and is intended to demonstrate:

- Setting up a version-controlled repository using Git and GitHub
- Documenting projects through README files, licenses, and GitHub Wikis
- Implementing issue tracking
- Writing and organizing integration and UAT test plans
- Creating mock testable endpoints for learning CI/testing practices

---

## Related Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [unittest — Python Docs](https://docs.python.org/3/library/unittest.html)
