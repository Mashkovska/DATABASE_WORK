import view_data_interfaces.view_data as view_data
from azure.eventhub import  EventData
from connections import event_hub_client, eventhub_name


class EventHub(view_data.ViewDataInterface):

    def view_data(self, client=event_hub_client):
        print("Adding the message...")
        ev_dt_batch = client.create_batch()
        ev_dt_batch.add(EventData(self))
        client.send_batch(ev_dt_batch)
        print("+")
