from expense import Expense
import calendar
import datetime
import streamlit as st

def main():
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = "./expenses.csv"
    budget = 2000
    input = st.checkbox("Enter Expense")
    Summary = st.checkbox("Expense Summary")
    # Get user input for expense.
    if input:
        expense = get_user_expense()
    elif Summary:
        summarize_expenses(expense_file_path, budget)
    # Write their expense to a file.
    

    # Read file and summarize expenses.
    


def get_user_expense():
    st.write("🎯 Getting User Expense")
    expense_name = st.text_input("enter name")
    expense_amount = st.number_input("enter amount")
    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

        #value_range = f"[1 - {len(expense_categories)}]"
    selected_category = st.selectbox("select category ",expense_categories)
   
    new_expense=Expense(expense_name,expense_amount,selected_category)
    
    if st.toggle("save"):
        save_expense_to_file(new_expense, "./expenses.csv")
    else:
        pass
    
    


def save_expense_to_file(expense: Expense, expense_file_path):
    st.write("🎯 Saving User Expense:")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")
    summarize_expenses(expense_file_path, 2000)


def summarize_expenses(expense_file_path, budget):
    st.write("🎯 Summarizing User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        st.write(f"  {key}: ₹{amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    st.write(f"💵 Total Spent: ₹{total_spent:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    remaining_budget = budget - total_spent
    st.write(f"✅ Budget Remaining: ₹{remaining_budget:.2f} ")
    st.write(f"⌛Remaining Days: {remaining_days}")

    

    daily_budget = remaining_budget / remaining_days
    st.write(f"👉 Budget Per Day: ₹{daily_budget:.2f}")


if __name__ == "__main__":
    main()