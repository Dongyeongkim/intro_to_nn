import jax.numpy as np

def f(x):
    return 1e-4*(x**2)

# START DEFINE YOUR FUNCTION HERE


# END DEFINE YOUR FUNCTION HERE


if __name__ == '__main__':
    x_init = 50000
    for i in range(10000):
        #START FILL THE CODE

        #END FILL THE CODE
        pass
    
    if abs(x_init) <= 1e-5:
        print("Congrats!")
    else:
        print("Fix your parameters")


