from argparse import ArgumentParser
from .taskcontroller import TaskController
def main():
    controller = TaskController('task.txt')
    parser = ArgumentParser(description='Simple Task Manager')
    subparsers = parser.add_subparsers()
    add_task = subparsers.add_parser('add', help='Add task')
    add_task.add_argument('title',help='Title of the task',type=str)
    add_task.add_argument('-d','--description',help='Short description of the task',type=str,default=None)
    add_task.add_argument('-s','--start_date',help='Date to begin the task',type=str,default=None)
    add_task.add_argument('-e','--end_date',help='Date to end the task',type=str,default=None)
    add_task.add_argument('--done',help='Check the task is done or yet',default=False)
    add_task.set_defaults(func = controller.add_task)

    list_task = subparsers.add_parser('list', help='List of unfinished tasks')
    list_task.add_argument('-a','--all',help='List of all task',action='store_true')
    list_task.set_defaults(func = controller.display)

    check_task = subparsers.add_parser('check', help='Check the given task')
    check_task.add_argument('-t' , '--task' , help='Number of task to be done. If not specified last task will be removed', type=int)
    check_task.set_defaults(func= controller.ckeck_task)

    remove = subparsers.add_parser('remove' , help='Remove a task')
    remove.add_argument('-t','--task',help='The task to be removed (Number)',type=int)
    remove.set_defaults(func= controller.remove)

    reset = subparsers.add_parser('reset' , help='Remove all tasks')
    reset.set_defaults(func=controller.reset)

    args = parser.parse_args()
    args.func(args)
    


if __name__ == '__main__':
    main()