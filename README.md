# Python API Test Automation Framework

A production-style test automation framework built with **Python**, **Pytest**, **Requests**, and **Playwright**.

The project is designed to validate API workflows, browser interactions, authentication, CRUD operations, and data-driven scenarios while supporting automated execution through **GitHub Actions CI/CD**.

---

## Purpose

The goal of this project is to demonstrate a structured approach to automated software testing using modern Python tooling.

The framework focuses on:

- API test automation
- UI/browser validation
- reusable test components
- data-driven testing
- clean test architecture
- automated reporting
- CI/CD integration

---

## Tech Stack

- Python
- Pytest
- Requests
- Playwright
- Pytest HTML
- GitHub Actions

---

## Project Structure

```text
Course_Python_API/
│
├── .github/
│   └── workflows/
│       └── api-tests.yml
│
├── data/
│   └── test_file_users/
│
├── helpers/
│   └── validators.py
│
├── page_objects/
│   └── users.py
│
├── tests/
│   ├── conftest.py
│   ├── test_crud_user.py
│   ├── test_first_get.py
│   ├── test_login.py
│   ├── test_login_products.py
│   ├── test_register_users.py
│   └── test_resposes.py
│
├── pytest.ini
├── requirements.txt
└── README.md
