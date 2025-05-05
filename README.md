# 🧪 QTest Selenium Reporting

> Automated Web UI Testing Framework using **PyTest**, **Selenium**, and **Beautiful HTML Reporting** for https://automationexercise.com

---

## 📖 Project Description

**QTest Selenium Reporting** is a Python-based automated testing framework designed to validate the UI functionality of the [Automation Exercise](https://automationexercise.com) website. The project uses **Selenium WebDriver** to simulate user interactions and **PyTest** for structuring and executing test cases. It also integrates HTML reporting to track test execution and outcomes.

---

## 🚀 What We Achieved

- ✅ Automated login and registration flow testing.
- ✅ Dynamic test reporting with HTML output.
- ✅ Real-time browser automation and interaction verification.
- ✅ Reusable Page Object Model (POM) architecture.
- ✅ Easy integration into CI/CD pipelines.

---

## 🛠️ Tech Stack & Tools Used

| Technology | Purpose                         |
|------------|----------------------------------|
| **Python 3.12** | Core programming language |
| **Selenium** | Browser automation |
| **PyTest** | Test execution framework |
| **pytest-html** | Generates beautiful HTML reports |
| **WebDriverWait & Expected Conditions** | Synchronization and stability |
| **Page Object Model (POM)** | Clean test structure |

---

## 🧰 Features

- 📄 Modular Page Object Model (POM) design
- 🧪 Test case separation with `tests/` directory
- 🗂️ `pages/` folder for reusable UI interaction classes
- 📑 Configurable test setup via `pytest.ini`
- 📊 Auto-generated HTML reports (`report.html`)
- 🖥️ Headed browser mode for real-time feedback

---

## 📂 Project Structure

```bash
QTest_Selenium-Reporting/
│
├── pages/
│   ├── login_page.py
│   └── register_page.py
│
├── tests/
│   ├── test_login.py
│   └── test_search.py
│
├── conftest.py         # Browser fixture
├── requirements.txt    # Dependencies
├── pytest.ini          # PyTest configuration
├── report.html         # Test results
└── README.md           # Project description

