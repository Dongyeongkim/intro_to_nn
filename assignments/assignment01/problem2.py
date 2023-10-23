import jax.numpy as np

def f(x):
    return x**4 - 3*(x**3) + 3*x

# DEFINE YOUR FUNCTION HERE


# END DEFINE YOUR FUNCTION HERE


if __name__ == '__main__':
    x_init = -0.5
    for i in range(10000):
        #START FILL THE CODE
        
        #END FILL THE CODE
        pass
    
    if ((x_init <= 2.073) and (x_init >= 2.079)):
        print("Fix your parameters")
    else:
        print("Congrats")