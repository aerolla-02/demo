class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.is_on = False  # Initialize state
    
    def turn_on(self) -> None:
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} microwave is now ON.")
        else:
            print(f"{self.brand} microwave is already ON.")

    def turn_off(self) -> None:
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} microwave is now OFF.")
        else:
            print(f"{self.brand} microwave is already OFF.")
    
    def set_timer(self, minutes: int) -> None:
        if not self.is_on:
            print("Please turn on the microwave first.")
        else:
            print(f"Setting timer for {minutes} minutes.")

smeg: Microwave = Microwave('Smeg', '800W')
smeg.turn_off()
smeg.turn_on()
smeg.set_timer(5)
smeg.turn_off()
smeg.set_timer(5)
smeg.turn_on()
smeg.set_timer(5)
