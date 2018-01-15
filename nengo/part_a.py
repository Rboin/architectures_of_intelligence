import nengo

def centered_square(x):
    return (x * x) - 0.5

model = nengo.Network()
with model:
    n = 100
    d = 1
    stimulus = nengo.Node([0])
    a = nengo.Ensemble(n_neurons=n, dimensions=d)
    b = nengo.Ensemble(n_neurons=n, dimensions=d)
    c = nengo.Ensemble(n_neurons=n, dimensions=d)
    
    nengo.Connection(stimulus, a)
    nengo.Connection(a, b, function=centered_square)
    nengo.Connection(b, c, transform=0.5)
    nengo.Connection(c, c, synapse=0.1)
