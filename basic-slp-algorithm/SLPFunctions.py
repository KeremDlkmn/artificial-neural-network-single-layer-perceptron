def calculateNETValue(attribute_1,attribute_2,weight_1,weight_2):
    valueNET = (attribute_1*weight_1) + (attribute_2 * weight_2)
    return valueNET

def reductionWeight(weight_1,weight_2,learning_coefficient,attribute_1,attribute_2):
    newWeightValue_1 = weight_1 - (learning_coefficient * attribute_1)
    newWeightValue_2 = weight_2 - (learning_coefficient * attribute_2)
    return newWeightValue_1, newWeightValue_2

def calculateThresholdValue(orange_net_value,apple_net_value,threshold_value):
    if(orange_net_value > threshold_value and apple_net_value > threshold_value):
        return True
    else:
        return False
