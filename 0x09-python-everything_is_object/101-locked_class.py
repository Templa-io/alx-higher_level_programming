def setattr(self, name, value):
if name != "first_name":
raise AttributeError("Cannot set attribute other than 'first_name'.")
super().setattr(name, value)
