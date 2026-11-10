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

- Work date input and format validation.
- Work entry and exit time registration and validation.
- Support for multiple break intervals.
- At least one break interval required per workday.
- Break start and end time validation.
- Chronological validation of work schedules and break intervals.
- Rejection of zero-duration break intervals.
- Automatic re-prompting when invalid date, time, or chronological values are entered.
- Input validation for yes/no confirmations.
- Automatic calculation of total working hours, excluding break intervals.
- Work duration displayed in hours and minutes.
- Optional workday notes (one note per workday).
- Overnight work shifts are not supported in the current version.

## Roadmap

- [ ] Complete workday summary and data review.
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

### Pr