from die import Die
import pygal

die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
	result = die1.roll()+die2.roll()
	results.append(result)

frequencies = []
for value in range(2,die1.num_sides+die2.num_sides):
	frequency = results.count(value)
	frequencies.append(frequency)
#绘制直方图
hist = pygal.Bar()
hist.title = "Result of rolling two D6 1000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6',frequencies)
hist.render_to_file('die_visual.svg')