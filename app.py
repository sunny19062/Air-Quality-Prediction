import pickle

# Load the Random Forest model
with open('RF.pkl', 'rb') as file:
    rf_model = pickle.load(file)

# Load the Logistic Regression model
with open('LGR.pkl', 'rb') as file:
    lg_model = pickle.load(file)

# Load the Decision Tree model
with open('DT.pkl', 'rb') as file:
    dt_model = pickle.load(file)

# Function to get user input
def get_user_input():
    n1 = float(input("Enter SO2 value: "))
    n2 = float(input("Enter NO2 value: "))
    n3 = float(input("Enter RSPM value: "))
    n4 = float(input("Enter SPM value: "))
    n5 = float(input("Enter PM2.5 value: "))
    return [[n1,n2,n3,n4,n5]]

# Function to make predictions
def predict(model, input_data):
    # input_data = [[pm2_5, pm10, no2]]
    predictions = model.predict(input_data)
    return predictions[0]

# Loop to take input and make predictions until a certain key is pressed
while True:
    print("Select a model: ")
    print("1. Random Forest")
    print("2. Logistic Regression")
    print("3. Decision Tree")
    print("Press 'q' to quit...")
    choice = input("Enter your choice: ")

    if choice == 'q':
        break

    elif choice == '1':
        print("Random Forest model selected.")

        data = get_user_input()
        result = predict(rf_model, data)
        print("Predicted value:", result)

    elif choice == '2':
        print("Logistic Regression model selected.")

        data = get_user_input()
        result = predict(lg_model, data)
        print("Predicted value:", result)

    elif choice == '3':
        print("Decision Tree model selected.")

        data = get_user_input()
        result = predict(dt_model, data)
        print("Predicted value:", result)

    else:
        print("Invalid choice. Please try again.")

    print()

print("Program terminated.")
