# CHRONOS – Work Hours Tracker

**CHRONOS** is a Python-based work hours tracking application designed to help independent contractors manage and track their daily working hours.

The project focuses on implementing practical business rules, reliable data validation, and time calculation logic while following software development best practices.

## Project Goals

- Record daily work schedules.
- Manage multiple break intervals within a workday.
- Calculate total working hours automatically.
- Ensure data consistency through input validation and business rules.
- Persist work records in a database.

## Current Features

- Work date input and validation.
- Work entry time input and validation.
- Support for multiple break intervals.
- Break start and end time input.
- Automatic re-prompting when invalid date or time formats are entered.
- At least one break interval per workday.

## Roadmap

- [ ] Work exit time registration.
- [ ] Chronological validation of work schedules.
- [ ] Break interval validation, including zero-duration rejection.
- [ ] Automatic calculation of total working hours.
- [ ] Optional workday notes.
- [ ] PostgreSQL database integration.
- [ ] Workday management and data reset functionality.
- [ ] Automated tests.
- [ ] Graphical user interface.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Git | Version control |
| GitHub | Source code hosting |
| PostgreSQL | Planned database |

## Project Structure

The application is currently under development, starting with input handling and core business logic. Its structure will evolve as new features are implemented.

## Getting Started

### Prerequisites

- Python 3.x
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/hmachado-henrique/chronos.git
```

Navigate to the project directory:

```bash
cd chronos
```

Run the application using Python 3:

```bash
python3 chronos.py
```

## Project Status

**In Development**

CHRONOS is an ongoing project. Features are being implemented incrementally, with an emphasis on learning, code quality, maintainability, and practical software engineering principles.

## Purpose

This project serves two purposes:

1. Building a practical tool for independent contractor work hours tracking.
2. Demonstrating software development skills through the design and implementation of a real-world application.
