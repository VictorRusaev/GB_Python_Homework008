import view
import model
import logger


def run():
    while True:
        choice = view.choose_mode()
        if choice == 1:
            example = view.user_input()
            ans = model.execute_example(example)
            view.print_ans(example, ans)
            logger.log_to_file(example, ans)
        elif choice == 2:
            example = view.user_input()
            ans = model.execute_equasion(example)
            view.print_x(ans)
            logger.log_to_file(example, ans)
        elif choice == 3:
            example = view.user_input()
            ans = model.simplification(example)
            view.print_ans(example, ans)
            logger.log_to_file(example, ans)
        elif choice == 4:
            history = logger.get_history()
            view.print_history(history)
        else:
            view.error_message(choice)
