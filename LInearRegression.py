from numpy import *


def compute_error_for_given_points(initail_b, inital_m, points):
    totalError = 0
    for i in range(0,len(points)):
        x = points[i,0];
        y = points[i,1];
        totalError += (y-(inital_m*x+initail_b))**2

        return  totalError/float(len(points))


def step_gradient(b_current, m_current, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    N= float(len(points))
    for i in range(0,len(points)):
        x = points[i,0]
        y = points[i,1]
        b_gradient += -(2/N)*(y-((m_current*x)+b_current))
        m_gradient += -(2/N)*x*(y-((m_current*x)+b_current))

    new_b = b_current - (learning_rate*b_gradient)
    new_m = m_current - (learning_rate*m_gradient)
    return [new_b,new_m]



def gradient_decent_runner(points, starting_m, starting_b, learning_rate, num_iterations):
    b = starting_b
    m = starting_m

    for i in range(num_iterations):
        b,m = step_gradient(b,m,array(points),learning_rate)
    return [b,m]



def run():
    points = genfromtxt('data.csv',delimiter=',')
    learning_rate = 0.0001
    initiall_b = 0
    initial_m = 0
    num_iterations = 1000
    print"Starting gradient decent at b= {0} and m = {1} and error = {2}".format(initial_b,initial_m,compute_error_for_given_points(initial_b,initial_m,points))
    [b,m] = gradient_decent_runner(points,initial_m,initial_b,learning_rate,num_iterations)
    print"Ending gradient decent at b={0},m={1},and error = {2}".format(b,m,compute_error_for_given_points(b,m,points))

if '__name__' == '__main__':
    run()