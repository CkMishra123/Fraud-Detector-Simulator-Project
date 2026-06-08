# Function to convert time into 24-hour format
def convert_to_24hr(time_str):
    time, period = time_str.split()
    hour, minute = map(int, time.split(":"))

    if period.lower() == "pm" and hour != 12:
        hour += 12
    elif period.lower() == "am" and hour == 12:
        hour = 0
    return hour


# Safe locations list
safe_locations = {"India","USA","Dubai","Nepal","Iran","Israel","Russia",
                  "Kuwait","Bahrain","Mauritius","China","Vietnam","Brazil","Kenya"}

# Input number of transactions
x = int(input("Enter the Number of Transactions: "))
Transactions = []

for i in range(x):
    
    print(f"\nTransaction {i+1}")

    user = input("Enter the User name: ")
    amount = int(input("Enter the Amount (₹): "))
    location = input("Enter the Location: ")
    time = input("Enter the time (HH:MM AM/PM): ")
    transactions_count = int(input("Transactions in last 2 minutes: "))
    account_age = int(input("Account age (days): "))
    failed_attempts = int(input("Failed login attempts: "))
    new_device = input("New device? (yes/no): ")

    hour = convert_to_24hr(time)

    # Store transaction
    Transaction = {
        "User": user,
        "Amount": amount,
        "Location": location,
        "Time": time,
        "Hour": hour
    }
    Transactions.append(Transaction)

    # Fraud detection is starting from here
    risk_score = 0

    print("\n--- Fraud Analysis ---")


#Implementing varieties of conditions to detect a fraud in the transaction
    
    # 1. Location Check
    if location not in safe_locations:
        print("⚠ Suspicious Location")
        risk_score += 25
    else:
        print("Safe Location")

    # 2. Amount Check
    if amount > 200000:
        print("⚠ High Amount")
        risk_score += 20
    else:
        print("Normal Amount")

    # 3. Time Check
    if 0 <= hour <= 4:
        print("⚠ Odd Transaction Time")
        risk_score += 10

    # 4. Velocity Check
    if transactions_count > 5:
        print("⚠ Too Many Transactions Quickly")
        risk_score += 20

    # 5. New Account Check
    if account_age < 7:
        print("⚠ New Account Risk")
        risk_score += 15

    # 6. Failed Attempts
    if failed_attempts >= 3:
        print("⚠ Multiple Failed Attempts")
        risk_score += 15

    # 7. New Device
    if new_device.lower() == "yes":
        print("⚠ New Device Used")
        risk_score += 10

    # Final Conclusion about your detection of the Fraud in Transaction
    print("\nTotal Risk Score:", risk_score)

    if risk_score >= 50:
        print("🚨 FRAUD DETECTED")
    elif risk_score >= 30:
        print("⚠ SUSPICIOUS TRANSACTION")
    else:
        print("✅ SAFE TRANSACTION")

    print("\n-----------------------------")

# Final Report
print("\n===== ALL TRANSACTIONS SUMMARY =====")
for i, t in enumerate(Transactions, start=1):
    print(f"{i}. {t['User']} | ₹{t['Amount']} | {t['Location']} | {t['Time']}")
