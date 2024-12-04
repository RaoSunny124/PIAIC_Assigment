def calculate_weight_on_planets(): 
        gravity_constants =  {
                "Mercury": 0.376,
                "Venus": 0.889,
                "Mars": 0.378,
                "Jupiter": 2.360,
                "Saturn": 1.081,
                "Uranus": 0.815,
                "Neptune": 1.140
        }
        earth_weight = float(input('\033[1;3mEnter your weight:\033[0m')) 
        planet = input('\033[34mEnter your planet\033[0m:').capitalize()
        if planet in gravity_constants:
            weight_on_planet = earth_weight * gravity_constants[planet]
            print(f'\033[1;3mYour weight on {planet} is : {weight_on_planet}\033[0m')
        else:
            print("⚠️Invalid planet name.🚀")  

calculate_weight_on_planets()