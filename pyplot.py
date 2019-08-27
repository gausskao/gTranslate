# python3
from matplotlib import pyplot
 
 
def example_algorithm():
  # Generate sample array
  # Method 1: ordered array
  target_array = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                  10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
 
  # Method 2: random array
  # import random
  # target_array = []
  # array_length = 100
  # for randoms in range(1, array_length):
  #   target_array.append(random.random() * 100)
 
  threshold = 0  # random.random() * 80
 
  log_line_counter = 0
  plot_array = []
  maximum_start = [0]
  maximum_end = [0]
  maximum_now = 0
  counting_sum = 0
 
  for every_values in target_array:
    log_line_counter += 1
 
    # Aggregate values into new array for plot.
    plot_array.append(every_values)  # - threshold)
 
    # Maximum Subarray Algorithm
    counting_sum += every_values - threshold
 
    if counting_sum >= maximum_now:
      maximum_now = counting_sum
 
      # Extending array tail.
      maximum_end.append(log_line_counter)
 
    elif counting_sum < 0:
      counting_sum = 0
 
      # Make new array start.
      maximum_start.append(log_line_counter + 1)
 
  # Get the correct 'start' before 'end'
  calibrated_start = 0
  for starts in range(1, len(maximum_start)):
    this_one = maximum_start.pop()
    if this_one <= maximum_end[-1]:
      calibrated_start = this_one
      break
 
  # Put original values in a maximum value subarray.
  log_line_counter = 0
  average_sum = 0
  average_counter = 0
  maximum_value_array = []
  for every_values in target_array:
    log_line_counter += 1
    if log_line_counter < calibrated_start:
      maximum_value_array.append(threshold)
    if calibrated_start <= log_line_counter <= maximum_end[-1]:
      maximum_value_array.append(float(every_values))
      average_sum += float(every_values)
      average_counter += 1
    if maximum_end[-1] <= log_line_counter:
      maximum_value_array.append(threshold)
 
  average_current = 0
  if not maximum_value_array:
    print("Empty maximum array.")
  elif not average_counter:
    print("Zero length.")
  else:
    average_current = average_sum/average_counter
    # print("***Average current is: {:.5f} ***".format(average_current))
 
  pyplot.rcParams["figure.dpi"] = 250
 
  pyplot.text(
      log_line_counter * 0.65,
      str(average_current*1.2),
      "Average current: {:.5f}".format(average_current)
  )
 
  pyplot.rc("lines", linewidth=3)
  pyplot.title("New Full & Maximum")
  pyplot.xlabel("Time")
  pyplot.ylabel("Value")
  pyplot.plot(plot_array, label='For plot')
  pyplot.plot(maximum_value_array, label='Maximum')
  pyplot.legend()
  pyplot.show()
 
  return
 
 
if __name__ == "__main__":
  example_algorithm()
  exit()