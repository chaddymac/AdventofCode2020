import os



def main():
  #reading in the csv and appending all nums to one list
  f = open('day1.txt')
  text = f.readlines()
  depths = []
  new_list = []
  for x in text:
      x = x.strip("\n")
      x = int(x)
      depths.append(x)

  for i in range(len(depths) - 1):
    cur_num = depths[i]
    next_num = depths[i + 1]
    if next_num > cur_num:
      new_list.append("increase")
    else:
      new_list.append("decrease")
    num = new_list.count("increase")
  return num


def main_part_two():
  f = open('day1.txt')
  text = f.readlines()
  depths = []
  new_list = []
  for x in text:
      x = x.strip("\n")
      x = int(x)
      depths.append(x)

  for i in range(len(depths) - 3):
    depth_one = depths[i]
    depth_two = depths[i + 1]
    depth_three = depths[i + 2]
    depth_four = depths[i+3]
    win_one = depth_one + depth_two + depth_three
    win_two = depth_two + depth_three + depth_four
    
    if win_two > win_one:
      new_list.append("increase")
    else:
      new_list.append("decreased")
    num = new_list.count("increase")
  return num

run = main_part_two()
print(run)
