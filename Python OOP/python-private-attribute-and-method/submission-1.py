class PasswordManager:
    def __init__(self, password: str):
        self.__password = password 
    
    # TODO: Implement the verify_password method
    def verify_password(self, p_try: str) -> bool:
        # if p_try == self.__password:
        #     return True
        # return False
        return p_try == self.__password



# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
