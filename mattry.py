import matplotlib.pyplot as plt

# Both lists have 7 items
apple = [20, 10, 50, 90, 40, 25, 64]
orange = [100, 67, 34, 56, 23, 12, 3]

# Adjusted range to have 7 items (2000, 2001, 2002, 2003, 2004, 2005, 2006)
year = range(2000, 2007)

plt.plot(year, apple, label='Apples')
plt.plot(year, orange, label='Oranges')

# Add a legend so you know which line is which
plt.legend()

# CRITICAL: This opens the window in KDE
plt.show()

