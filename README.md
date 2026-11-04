# Rule-Based Fraud Detection System

A command-line Python tool that scores financial transactions against seven risk rules and classifies each one as **Safe**, **Suspicious**, or **Fraud**. It is built for learning and demonstration, using explainable logic rather than a trained model.

## Features

- Accepts any number of transactions through interactive input
- Converts 12-hour time (AM/PM) into 24-hour format for time-based checks
- Applies 7 weighted risk rules and prints which ones triggered
- Produces a total risk score and a final verdict per transaction
- Prints a summary of all transactions at the end

## How It Works

Each transaction starts with a risk score of 0. Every triggered rule adds points:

| # | Rule | Condition | Points |
|---|------|-----------|--------|
| 1 | Location check | Location not in the safe list | +25 |
| 2 | Amount check | Amount above ₹2,00,000 | +20 |
| 3 | Time check | Transaction between 12:00 AM and 4:59 AM | +10 |
| 4 | Velocity check | More than 5 transactions in the last 2 minutes | +20 |
| 5 | New account | Account age under 7 days | +15 |
| 6 | Failed attempts | 3 or more failed login attempts | +15 |
| 7 | New device | Transaction made from a new device | +10 |

### Classification

| Risk Score | Result |
|------------|--------|
| 50 and above | 🚨 FRAUD DETECTED |
| 30 to 49 | ⚠ SUSPICIOUS TRANSACTION |
| Below 30 | ✅ SAFE TRANSACTION |

## Safe Locations

India, USA, Dubai, Nepal, Iran, Israel, Russia, Kuwait, Bahrain, Mauritius, China, Vietnam, Brazil, Kenya

Any other location is flagged as suspicious. The list can be edited in the `safe_locations` set.

## Requirements

- Python 3.6 or higher
- No external libraries needed

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
2. Run the script:
   ```bash
   python fraud_detection.py
   ```
3. Enter the details when prompted.

## Input Fields

| Field | Format | Example |
|-------|--------|---------|
| Number of transactions | Integer | 2 |
| User name | Text | Rahul |
| Amount (₹) | Integer | 250000 |
| Location | Text (case-sensitive) | Nigeria |
| Time | HH:MM AM/PM | 02:30 AM |
| Transactions in last 2 minutes | Integer | 7 |
| Account age (days) | Integer | 3 |
| Failed login attempts | Integer | 4 |
| New device | yes / no | yes |

## Sample Output
Transaction 1
Enter the User name: Rahul
Enter the Amount (₹): 250000
Enter the Location: Nigeria
Enter the time (HH:MM AM/PM): 02:30 AM
Transactions in last 2 minutes: 7
Account age (days): 3
Failed login attempts: 4
New device? (yes/no): yes

--- Fraud Analysis ---
⚠ Suspicious Location
⚠ High Amount
⚠ Odd Transaction Time
⚠ Too Many Transactions Quickly
⚠ New Account Risk
⚠ Multiple Failed Attempts
⚠ New Device Used

Total Risk Score: 115
🚨 FRAUD DETECTED



## Limitations

- Rules and thresholds are fixed and not learned from data
- Location matching is case-sensitive (e.g., "india" will not match "India")
- Input is not validated, so invalid entries may cause errors
- Transactions are not saved to a file or database

## Future Improvements

- Add input validation and case-insensitive location matching
- Save results to CSV or a database
- Replace fixed thresholds with a machine learning model trained on real data
- Build a dashboard for visualizing flagged transactions

## Tech Stack

Python (core language, no external dependencies)

## Author

**Chandrakant Mishra**
MSc Mathematics and Computing, Central University of Andhra Pradesh
