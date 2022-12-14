import view
import logger
import model


def run():
    cont = 'yes'
    while cont == 'да' or cont == 'yes':
        mode = view.choice_mode()
        if mode == 1:
            new = view.get_new_contact()
            logger.write_new_contact(new)
            cont = view.continue_work_book()
        if mode == 2:
            name = view.get_name()
            base = logger.read_mode_phone_book()
            result = model.check_name(base, name)
            view.print_result(result)
            cont = view.continue_work_book()
        if mode == 3:
            print(logger.read_phone_book())
            cont = view.continue_work_book()
        if mode == 4:
            name = view.delit_contact()
            base = logger.read_mode_phone_book()
            logger.clear_book()
            result = model.check_name_for_del(base, name)
            logger.record(result)
            cont = view.continue_work_book()
