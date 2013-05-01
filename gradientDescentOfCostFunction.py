def gradientDescent(theta0, theta1, alpha, trainingSet):
    sumTheta0, sumTheta1 = 0, 0

    # Compute the sum apart from the other stuff
    for trainingExample in trainingSet:
        sumTheta0 += (theta0 + (theta1*trainingExample[0]) - trainingExample[1])
        sumTheta1 += (theta0 + (theta1*trainingExample[0]) - trainingExample[1])*trainingExample[0]

    tempTheta0 = theta0 - (alpha/len(trainingSet)) * sumTheta0
    tempTheta1 = theta1 - (alpha/len(trainingSet)) * sumTheta1

    return tempTheta0, tempTheta1

def costFunction(theta0, theta1, alpha, trainingSet):
    sumCostFunction = 0
    
    for trainingExample in trainingSet:
        sumCostFunction += ((theta0 + (theta1*trainingExample[0]) - trainingExample[1]))**2

    total = ((alpha*sumCostFunction)/(2*len(trainingSet)))
    return total
    
