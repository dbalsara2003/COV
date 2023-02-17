from getting_data import x, y, x_test, x_train ,y_pred, y_test
import matplotlib.pyplot as plt

# Compare the estimated floor area with the actual floor area
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Floor Area")
plt.ylabel("Estimated Floor Area")
plt.title("Actual vs Estimated Floor Area")
plt.show()

