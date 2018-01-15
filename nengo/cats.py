import nengo
import nengo.spa as spa
import random

D = 32  # the dimensionality of the vectors


#function that randomly presents a cat, a tiger, or nothing ('0')
#updates every .5 seconds
cur_time = -1
cur_stim = '0'
stims = []
def input_to_vision(t):
    global cur_time
    global cur_stim
    global stims
    
    #updates every .5 seconds
    if int(t*2) > cur_time:

        #fill list if empty
        if len(stims) < 1:
            stims = ['CAT', 'TIGER', '0'] #possible stims
            random.shuffle(stims)

        #select item
        cur_stim = stims.pop()
        
        #store current time
        cur_time = t*2
    
    #return current stimulus
    return cur_stim
        
#model definition: uses spa.SPA because we use semantic pointers
model = spa.SPA()
with model:

    model.vision = spa.State(D)
    model.motor = spa.State(D)
    
    #spa Input node that presents cat, tiger, or nothing, based on input_to_vision
    model.stim = spa.Input(vision=input_to_vision) 
    
    actions = spa.Actions(
        'dot(vision, CAT) --> motor=PET',
        'dot(vision, TIGER) --> motor=RUN',
        '0.5 --> motor=STARE'
        )
    
    model.bg = spa.BasalGanglia(actions)
    model.thal = spa.Thalamus(model.bg)


