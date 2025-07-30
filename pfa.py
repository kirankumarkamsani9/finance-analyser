import os
from datetime import datetime

st.subheader("📁 Save This Month’s Data")

# Get current month and year
current_month = datetime.now().strftime("%B %Y")

# Save button
if st.button("💾 Save Data"):
    data = {
        "Month": current_month,
        "Income": monthly_income,
        **expenses,  # unpack expense categories
        "Total Expenses": total_expenses,
        "Savings": savings
    }

    df_new = pd.DataFrame([data])

    file_path = "finance_data.csv"

    if os.path.exists(file_path):
        # If file exists, append to it
        df_existing = pd.read_csv(file_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_csv(file_path, index=False)
    else:
        # If not, create a new file
        df_new.to_csv(file_path, index=False)

    st.success(f"Data saved for {current_month}!")
