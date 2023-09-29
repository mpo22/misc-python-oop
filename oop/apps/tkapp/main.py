import logging
import logging.config
import tkinter
import tkinter.ttk

from oop.core.logging import LoggingInitializer
from oop.core.service1 import Service1BackwardDelegatee
from oop.core.service1 import Service1Delegator


def main():
    """dummy tkinter application"""

    LoggingInitializer().setup()

    delegator = Service1Delegator(Service1BackwardDelegatee())

    # https://docs.python.org/fr/3/library/tkinter.html#a-hello-world-program
    root_tk = tkinter.Tk()

    frame = tkinter.ttk.Frame(root_tk)
    frame.grid()

    tkinter.ttk.Label(frame, text="Input").grid(column=0, row=0)
    input_variable = tkinter.StringVar()
    input_entry = tkinter.ttk.Entry(frame, textvariable=input_variable)
    input_entry.grid(column=1, row=0)
    input_entry.focus()

    tkinter.ttk.Label(frame, text="Output").grid(column=0, row=1)
    output_variable = tkinter.StringVar()
    output_label = tkinter.ttk.Label(frame, textvariable=output_variable)
    output_label.grid(column=1, row=1)

    def compute(*args):
        try:
            input_value = input_variable.get()
            logging.info("input_value=%s", input_value)
            output_value = delegator.method1(input_value)
            logging.info("output_value=%s", output_value)
            output_variable.set(output_value)
        except Exception as exception:
            logging.exception(exception)

    input_entry.bind("<Return>", compute)

    tkinter.ttk.Button(frame, text="Quit", command=root_tk.destroy).grid(column=0, row=2)

    logging.debug("tk mainloop ...")
    root_tk.mainloop()

    logging.debug("done")


if __name__ == "__main__":
    main()
