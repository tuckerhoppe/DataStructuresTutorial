from graphviz import Source

my_tree = '''
graph tree { 
  layout=dot
  node [shape=circle]
  "Ceo"--"Marketing"--"Tim"--"John"--"Sleek Comercial";
  "Tim"--"Harry";
  "Ceo"--"HR"--"Jill";
  "HR"--"Toby";
  "Ceo"--"Product Design"--"Michael"--"Joyce"--"New Tires";
  "Ceo"--"Product Development"--"Tucker"--"Self Driving Car code";
}'''
Source(my_tree)
