class Control():
    def __init__(self,rapid_breath):
        self.rapid_breath = rapid_breath
        self.subcostal_on = 0
        self.substernal_on = 0
        self.intercostal_on = 0
        self.clavicular_on = 0
        self.suprasternal_on = 0

    def set_subcostal(self, value):
        self.subcostal_on = value
    def set_substernal(self, value):
        self.substernal_on = value
    def set_intercostal(self, value):
        self.intercostal_on = value
    def set_clavicular(self, value):
        self.clavicular_on = value
    def set_suprasternal(self, value):
        self.suprasternal_on = value

    def get_subcostal(self):
        return self.subcostal_on
    def get_substernal(self):
        return self.substernal_on
    def get_intercostal(self):
        return self.intercostal_on
    def get_clavicular(self):
        return self.clavicular_on
    def get_suprasternal(self):
        return self.suprasternal_on