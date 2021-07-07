my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 #pounds

print "Let's talk about %s" % my_name
print "He's %d inches tall." % my_height
print "I can add %d and %d to get the number %d" % (
  my_age, my_height, my_age + my_height )

my_kilo_weight = my_weight / 2.2
my_metric_height = my_height * 2.54 / 100

print "In kilos my weight is %s" % round(my_kilo_weight, 2)
print "In centimeters my height is %s meters" % round(my_metric_height, 2)
