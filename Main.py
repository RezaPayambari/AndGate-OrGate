from AndGate import AndGate
from OrGate import OrGate

print("AndGate example: \n")
n=AndGate(True,True)
n.execute()
n.show()


c=AndGate()
c.Input0=False
c.Input1=True
c.execute()
c.show()

print("\nOrGate example: \n")
o=OrGate(False,False)
o.execute()
o.show()


o1=OrGate()
o1.Input1=True
o1.Input0=False
o1.execute()
o1.show()
