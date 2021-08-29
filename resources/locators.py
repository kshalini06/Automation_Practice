from selenium.webdriver.common.by import By


class Locators:
    # Home Page
    sign_in_link = (By.XPATH, "//a[@title='Log in to your customer account']")

    @staticmethod
    def product(product_name):
        return (By.XPATH, f"(//a[@title = '{product_name}'])[1]")

    @staticmethod
    def add_to_cart(product_name):
        return (By.XPATH, f"(//a[@title='{product_name}']/parent::h5/following-sibling::div/a[@title='Add to cart'])")

    continue_shopping = (By.XPATH, "//span[@title='Continue shopping']")
    proceed_to_checkout = (By.XPATH, "//a[@title='Proceed to checkout']")
    view_cart = (By.XPATH, "//a[@title = 'View my shopping cart']")
    cart_products = (By.XPATH, "//a[@class='cart_block_product_name']")

    @staticmethod
    def remove_product(product_name):
        return (By.XPATH, f"//a[@title = '{product_name}']/ancestor::div[@class='cart-info']/following-sibling::span[contains(@class,'remove_link')]")

    # Login Page
    create_account = (By.XPATH, "//*[text() = \"Create an account\"]")
    already_registered = (By.XPATH, "//*[text() = 'Already registered?']")
    email_create = (By.ID, "email_create")
    submit_create = (By.ID, "SubmitCreate")
    email_create_error = (By.ID, "create_account_error")
    incorrect_email_create = (By.XPATH, "//*[text() = \"An account using this email address has already been "
                                        "registered. Please enter a valid password or request a new one. \"]")
    enter_email = (By.ID, "email")
    password = (By.ID, "passwd")
    forgot_password = (By.LINK_TEXT, "Forgot your password?")
    submit_login = (By.ID, "SubmitLogin")

    # Registration Page
    your_personal_info = (By.XPATH, "//*[text()= \"Your personal information\"]")
    title_mr = (By.ID, "id_gender1")
    title_mrs = (By.ID, "id_gender2")
    customer_firstname = (By.ID, "customer_firstname")
    customer_lastname = (By.ID, "customer_lastname")
    customer_email = (By.ID, "email")
    customer_password = (By.ID, "passwd")
    dob_select_days = (By.ID, "days")
    dob_select_months = (By.ID, "months")
    dob_select_years = (By.ID, "years")
    checkbox_newsletter = (By.ID, "newsletter")
    checkbox_special_offers = (By.ID, "optin")
    label_your_address = (By.XPATH, "//*[text()='Your address']")
    your_add_firstname = (By.ID, "firstname")
    your_add_lastname = (By.ID, "lastname")
    your_add_company = (By.ID, "company")
    your_add_addline1 = (By.ID, "address1")
    your_add_addline2 = (By.ID, "address2")
    your_add_city = (By.ID, "city")
    your_add_state_dropdown = (By.ID, "id_state")
    your_add_postcode = (By.ID, "postcode")
    your_add_country_dropdown = (By.ID, "id_country")
    your_add_additional_info = (By.ID, "other")
    your_add_home_phn = (By.ID, "phone")
    your_add_mobile_phn = (By.ID, "phone_mobile")
    your_add_add_alias = (By.ID, "alias")
    register_button = (By.ID, "submitAccount")

    # My Account Page
    login_failed = (By.XPATH, "//*[@class='alert alert-danger']/ol/li")
    view_account = (By.CLASS_NAME, "account")
    sign_out = (By.CLASS_NAME, "logout")



