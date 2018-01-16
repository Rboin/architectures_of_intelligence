import nengo

def centered_square(a):
    return (a * a) - 0.5

model = nengo.Network()
with model:
    # We want 100 neurons in the same layer.
    n = 100
    d = 1
    
    # Add an input node.
    stimulus = nengo.Node([0])
    
    # Create layers.
    a = nengo.Ensemble(n_neurons=n, dimensions=d)
    b = nengo.Ensemble(n_neurons=n, dimensions=d)
    c = nengo.Ensemble(n_neurons=n, dimensions=d)
    
    # Connect first layer to the input.
    nengo.Connection(stimulus, a)
    
    # Connect layer A to B, passing the square centered around 0 
    # of layer A's input to B.
    nengo.Connection(a, b, function=centered_square)
    # Connect layer B to layer C, layer B passes half its input to C.
    nengo.Connection(b, c, transform=0.5)
    # Connect C to itself, creating a memory layer. It passes whatever value it 
    # currently holds to itself every 100ms.
    nengo.Connection(c, c, synapse=0.1)
