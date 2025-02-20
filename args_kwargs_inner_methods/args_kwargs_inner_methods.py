import sys
def testFunction(parameter1, parameter2, parameter3, *args, **kwargs):
    print(parameter1)
    print(parameter2)
    print(parameter3)
    print(args)
    print(kwargs)
    
def generate_calculation(exponent):
    def calculate(base, addition):
        return base ** exponent + addition
    return calculate

    
if __name__ == "__main__":
    try:
        #testFunction(1,2, *(4,5,6), **{"key1": 7, "key2": 8})
        
        # für Parameter1 gibt es mehrere Werte
        #testFunction(1,2, *(4,5,6), **{"parameter1": 7, "key2": 8})
        
        #testFunction( *(4,5,), **{"parameter3": 7, "key2": 8})
        
        #testFunction(3, **{"parameter3": 7, "parameter2": 8},)
        
        calculation = generate_calculation(2)
        print(calculation(4, 3))
        # 4^2 + 3 = 16 + 3 = 19
        
        calc_func = lambda  exponent, base, addition: base ** exponent + addition
        print(calc_func(2, 4, 3))
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
        