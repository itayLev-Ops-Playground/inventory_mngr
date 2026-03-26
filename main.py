
# Main application file for the inventory manager.
# This script initializes the application, loads data, and runs the main menu loop.

from render_menu import show_main_menu as show_main_menu
from render_menu import get_main_menu_options as get_main_menu_options

from helpers import intake_user_choice as intake_user_choice
from helpers import get_data_base as get_data_base
from helpers import set_data_base as set_data_base
from helpers import set_dummy_data as set_dummy_data
from helpers import get_dummy_data as get_dummy_data

from display_menu import display_menu as display_menu
from update import update_manu as update_manu
from add import add_menu as add_menu
from delete import delete_menu as delete_menu


is_saved = False
on = True

# Initiate dummy-data to data-base 
data_base = get_data_base()
set_dummy_data(data_base)

print("\n\nWELCOME TO INVENTORY MNGR")

while on:

    show_main_menu()

    menu = get_main_menu_options()
    user_choice = intake_user_choice(menu)

    if user_choice == 1: # DISPLAY -> Display menu -> 1.By system menu, 2.By model menu
        display_menu()
        
    if user_choice == 2: # UPDATE -> Choose model -> Choose system -> Choose inventory property -> Approve
        update_manu()

    if user_choice == 3: # ADD -> 
        add_menu()

    if user_choice == 4:  # DELETE
        delete_menu()

    if user_choice == 5: # SAVE
        dummy_data = get_dummy_data()
        continue_choice = input("Are you sure you want to commit data permanently?\nTHESE ACTION IS PERMANENT !\nEnter y for yes or press enter to abort")
        if continue_choice == 'y':
            set_data_base(dummy_data)
            is_saved = True

    if user_choice == 6: # EXIT
        if is_saved:
            message = "Thank you for using INVENTORY MNGR"
            print(f"\n\n{'=' * len(message)}\n{message}\n{'=' * len(message)}\n\n")
        else:
            exit_save_choice = input("\n* The changes you maid were not saved !\nDo you want to save the changes ?\nEnter YES to save or NO to exit INVENTORY MNGR.\n").lower()
            if exit_save_choice == 'YES':
                set_data_base(dummy_data)

        on = False
        
