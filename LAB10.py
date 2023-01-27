//
import re
def isVariable(x):
return len(x) == 1 and x.islower() and x.isalpha()
def getAttributes(string):
expr = &#39;\([^)]+\)&#39;
matches = re.findall(expr, string)
return matches
def getPredicates(string):
expr = &#39;([a-z~]+)\([^&amp;|]+\)&#39;
return re.findall(expr, string)
class Fact:
def __init__(self, expression):
self.expression = expression
predicate, params = self.splitExpression(expression)
self.predicate = predicate
self.params = params
self.result = any(self.getConstants())
def splitExpression(self, expression):
predicate = getPredicates(expression)[0]
params = getAttributes(expression)[0].strip(&#39;()&#39;).split(&#39;,&#39;)
return [predicate, params]
def getResult(self):
return self.result
def getConstants(self):
return [None if isVariable(c) else c for c in self.params]
def getVariables(self):
return [v if isVariable(v) else None for v in self.params]
def substitute(self, constants):
c = constants.copy()
f = f&quot;{self.predicate}({&#39;,&#39;.join([constants.pop(0) if isVariable(p) else p for p in
self.params])})&quot;

return Fact(f)
class Implication:
def __init__(self, expression):
self.expression = expression
l = expression.split(&#39;=&gt;&#39;)
self.lhs = [Fact(f) for f in l[0].split(&#39;&amp;&#39;)]
self.rhs = Fact(l[1])
def evaluate(self, facts):
constants = {}
new_lhs = []
for fact in facts:
for val in self.lhs:
if val.predicate == fact.predicate:
for i, v in enumerate(val.getVariables()):
if v:
constants[v] = fact.getConstants()[i]
new_lhs.append(fact)
predicate, attributes = getPredicates(self.rhs.expression)[0],
str(getAttributes(self.rhs.expression)[0])
for key in constants:
if constants[key]:
attributes = attributes.replace(key, constants[key])
expr = f&#39;{predicate}{attributes}&#39;
return Fact(expr) if len(new_lhs) and all([f.getResult() for f in new_lhs]) else None
class KB:
def __init__(self):
self.facts = set()
self.implications = set()
def tell(self, e):
if &#39;=&gt;&#39; in e:
self.implications.add(Implication(e))
else:
self.facts.add(Fact(e))
for i in self.implications:
res = i.evaluate(self.facts)
if res:
self.facts.add(res)
def query(self, e):
facts = set([f.expression for f in self.facts])
i = 1
print(f&#39;Querying {e}:&#39;)
for f in facts:
if Fact(f).predicate == Fact(e).predicate:
print(f&#39;\t{i}. {f}&#39;)
i += 1
def display(self):

print(&quot;All facts: &quot;)
for i, f in enumerate(set([f.expression for f in self.facts])):
print(f&#39;\t{i+1}. {f}&#39;)
kb = KB()
kb.tell(&#39;missile(x)=&gt;weapon(x)&#39;)
kb.tell(&#39;missile(M1)&#39;)
kb.tell(&#39;enemy(x,America)=&gt;hostile(x)&#39;)
kb.tell(&#39;american(West)&#39;)
kb.tell(&#39;enemy(Nono,America)&#39;)
kb.tell(&#39;owns(Nono,M1)&#39;)
kb.tell(&#39;missile(x)&amp;owns(Nono,x)=&gt;sells(West,x,Nono)&#39;)
kb.tell(&#39;american(x)&amp;weapon(y)&amp;sells(x,y,z)&amp;hostile(z)=&gt;criminal(x)&#39;)
kb.query(&#39;criminal(x)&#39;)
kb.display()
kb_ = KB()
kb_.tell(&#39;king(x)&amp;greedy(x)=&gt;evil(x)&#39;)
kb_.tell(&#39;king(John)&#39;)
kb_.tell(&#39;greedy(John)&#39;)
kb_.tell(&#39;king(Richard)&#39;)
kb_.query(&#39;evil(x)&#39;)
