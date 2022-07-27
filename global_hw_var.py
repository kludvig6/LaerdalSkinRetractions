rapid_breath = True
subcostal_on = 0
substernal_on = 0
intercostal_on = 0
clavicular_on = 0
suprasternal_on = 0

## Retractions control
def set_rapid_breath(value):
    rapid_breath = value
def set_subcostal(value):
    subcostal_on = value
def set_substernal(value):
    substernal_on = value
def set_intercostal(value):
    intercostal_on = value
def set_clavicular(value):
    clavicular_on = value
def set_suprasternal(value):
    suprasternal_on = value

def get_rapid_breath():
    return rapid_breath
def get_subcostal():
    return subcostal_on
def get_substernal():
    return substernal_on
def get_intercostal():
    return intercostal_on
def get_clavicular():
    return clavicular_on
def get_suprasternal():
    return suprasternal_on