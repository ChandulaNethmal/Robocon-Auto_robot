class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = ["COMPLETED_TASK"]

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self):
       # try:
        handler = self.handlers[self.startState]
        #except:
        #    raise InitializationError("must call .set_start() before .run()")
        #if not self.endStates:
        #    raise  InitializationError("at least one state must be an end_state")
    
        while True:
            (newState) = handler()
            if newState.upper() in self.endStates:
                print("reached ", newState)
                break 
            else:
                handler = self.handlers[newState.upper()]   
