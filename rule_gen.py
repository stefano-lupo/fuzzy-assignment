def parse(x):
  x.rstrip()
  x = x.lower()
  x = x.split(' ')
  x[-1] = x[-1].rstrip()
  return x[1:]


def gen_rules(mem_funcs, ctrl):
  with open("rulebase.txt") as f:
      content = f.readlines()
  content = [parse(x) for x in content] 

  rules = []
  for line in content:
    rules.append(ctrl.Rule(
      mem_funcs[0][line[0]] & mem_funcs[1][line[1]] & mem_funcs[2][line[2]],
      mem_funcs[3][line[3]]))

  return rules