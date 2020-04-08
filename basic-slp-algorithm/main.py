## import SLPFunctions
import SLPFunctions as slp

## Magic Number -> Orange Attributes and Orange Class ##
orange_attribute_1 = 1
orange_attribute_2 = 0
orange_class       = 1

## Magic Number -> Apple Attributes and Apple Class ##
apple_attribute_1 = 0
apple_attribute_2 = 1
apple_class       = 0

## Magic Number -> Weight, Threshold Value ve Learning Coefficient ##
weight_value_1  = 1
weight_value_2  = 2
threshold_value = -1
learning_coefficient = 0.5

## Iteration Value ##
iteration_value = 0

while(True):
    print("------------------------------------")
    iteration_value += 1
    print(iteration_value, ". Iteration")
    print("------------------------------------")

    OrangeNET = slp.calculateNETValue(orange_attribute_1,orange_attribute_2,weight_value_1,weight_value_2)
    AppleNET = slp.calculateNETValue(apple_attribute_1,apple_attribute_2,weight_value_2,weight_value_2)

    print("NET Orange Value: ",OrangeNET)
    print("NET Apple Value : ",AppleNET)
    print("------------------------------------")

    if(OrangeNET == orange_class):
        if(slp.calculateThresholdValue(OrangeNET,AppleNET,threshold_value)):
            print("Output : Orange")
            if(AppleNET == apple_class):
                if(slp.calculateThresholdValue(OrangeNET,AppleNET,threshold_value)):
                    print("Output : Apple")
                    break
                else:
                    weight_value_1, weight_value_2 = slp.reductionWeight(weight_value_1, weight_value_2,
                                                                        learning_coefficient, apple_attribute_1,
                                                                        apple_attribute_2)
            else:
                weight_value_1, weight_value_2 = slp.reductionWeight(weight_value_1, weight_value_2,
                                                                    learning_coefficient, apple_attribute_1, apple_attribute_2)
        else:
            weight_value_1, weight_value_2 = slp.reductionWeight(weight_value_1, weight_value_2, learning_coefficient,apple_attribute_1, apple_attribute_2)
    else:
        weight_value_1, weight_value_2 = slp.reductionWeight(weight_value_1, weight_value_2, learning_coefficient,orange_attribute_1, orange_attribute_2)

print("------------------------")
print("Class Prediction")
print("Orange Class : ", OrangeNET)
print("Apple Class  : ", AppleNET)
print("Itration Value: ", iteration_value)
