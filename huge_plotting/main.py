from matplotlib import pyplot as plt

plt.xkcd()
app_update_33 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

bugs_found_33 = [25, 20, 18, 15, 12, 10, 8, 5, 4, 3, 2, 1]
plt.plot(app_update_33, bugs_found_33, color ='blue', marker = '.', linestyle = '--' ,label = 'updates')


ram_usage_31 = [2, 4, 6, 8, 10, 12, 14, 16]

system_lag_ms_31 = [10, 12, 15, 25, 50, 120, 450, 1200]

plt.plot(ram_usage_31,system_lag_ms_31,marker = 'o', label = 'Python')



book_pages_57 = [1, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

reading_days_57 = [2, 5, 8, 12, 18, 25, 30, 35, 42, 50]
plt.plot(book_pages_57,reading_days_57, marker ='+',  label = 'reading')

plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.grid()

plt.tight_layout()

plt.savefig('plot.png')
plt.show()