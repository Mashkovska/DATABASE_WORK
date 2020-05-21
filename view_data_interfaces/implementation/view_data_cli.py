import view_data_interfaces.view_data as v


class Cli(v.ViewDataInterface):

    def view_data(self):
        print(self, flush=True)
        pass
